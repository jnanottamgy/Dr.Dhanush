#!/usr/bin/env python3
"""Build a self-contained -print.html with Google Fonts inlined as data URIs.

The client documents (quotation, owner's manual, money-explained) are rendered
to PDF with headless Chromium.  Chromium's print path will not reliably fetch a
remote stylesheet before it paints, so a document that links Google Fonts
renders in a fallback face with no error -- the PDF simply comes out in the
wrong typeface.  The fix is to inline every font file into the HTML before
rendering.

Usage:
    python3 scripts/build_print_html.py owner-manual.html
    python3 scripts/build_print_html.py owner-manual.html -o owner-manual-print.html

Then:
    /opt/pw-browsers/chromium --headless --disable-gpu --no-sandbox \
      --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
      --no-pdf-header-footer \
      --print-to-pdf=Malnad-Products-Owner-Manual.pdf \
      "file://$PWD/owner-manual-print.html"

Two things this script is careful about:

  * It sends a modern browser User-Agent.  Google Fonts serves whatever format
    the caller's UA supports; without one it hands back TTF, which inflates the
    file several times over for no gain.
  * It stamps data-theme="light" on <html>.  The source documents carry a
    prefers-color-scheme dark palette, and a print run that picks it up produces
    white text on a white page.
"""

import argparse
import base64
import pathlib
import re
import sys
import urllib.request

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
)

LINK_RE = re.compile(
    r'[ \t]*<link[^>]*href="(https://fonts\.googleapis\.com/css2\?[^"]+)"[^>]*>\n?'
)
PRECONNECT_RE = re.compile(r'[ \t]*<link[^>]*rel="preconnect"[^>]*>\n?')
TITLE_RE = re.compile(r"<title>(.*?)</title>\s*\n?", re.S)
FONT_URL_RE = re.compile(r"url\((https://fonts\.gstatic\.com/[^)]+)\)")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def inline_fonts(css: str) -> str:
    """Replace every gstatic url() in the CSS with a base64 data URI."""
    cache: dict[str, str] = {}
    urls = FONT_URL_RE.findall(css)
    uniq = list(dict.fromkeys(urls))
    print(f"  {len(uniq)} font files to inline", file=sys.stderr)

    for i, url in enumerate(uniq, 1):
        blob = fetch(url)
        ext = url.rsplit(".", 1)[-1].lower()
        mime = {"woff2": "font/woff2", "woff": "font/woff", "ttf": "font/ttf"}.get(
            ext, "application/octet-stream"
        )
        cache[url] = f"data:{mime};base64,{base64.b64encode(blob).decode('ascii')}"
        if i % 10 == 0 or i == len(uniq):
            print(f"  {i}/{len(uniq)}", file=sys.stderr)

    return FONT_URL_RE.sub(lambda m: f"url({cache[m.group(1)]})", css)


def build(src: pathlib.Path, out: pathlib.Path) -> None:
    html = src.read_text(encoding="utf-8")

    links = LINK_RE.findall(html)
    if not links:
        sys.exit(f"{src}: no Google Fonts stylesheet link found — nothing to inline")

    font_css = []
    for url in links:
        print(f"fetching {url}", file=sys.stderr)
        font_css.append(inline_fonts(fetch(url).decode("utf-8")))

    # Strip the remote font links; they are now redundant and Chromium would
    # still try to reach them, delaying the paint.
    body = LINK_RE.sub("", html)
    body = PRECONNECT_RE.sub("", body)

    title_match = TITLE_RE.search(body)
    title = title_match.group(1) if title_match else src.stem
    body = TITLE_RE.sub("", body, count=1)

    out.write_text(
        '<!doctype html><html lang="en" data-theme="light"><head>'
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{title}</title>\n"
        "<style>\n" + "\n".join(font_css) + "\n</style>\n"
        "</head><body>\n" + body.lstrip("\n") + "</body></html>",
        encoding="utf-8",
    )

    kb = out.stat().st_size / 1024
    print(f"wrote {out} ({kb:,.0f} KB)", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=pathlib.Path, help="the document to build, e.g. owner-manual.html")
    ap.add_argument("-o", "--out", type=pathlib.Path, help="output path (default: <source>-print.html)")
    args = ap.parse_args()

    out = args.out or args.source.with_name(f"{args.source.stem}-print.html")
    build(args.source, out)


if __name__ == "__main__":
    main()
