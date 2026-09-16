import { StandardEvents } from '@shopify/events';

/**
 * Reveals the declarations belonging to the selected variant.
 *
 * Net quantity, MRP, packing date and best before are printed per pack, so a
 * 250 g and a 1 kg of the same product carry different figures. Horizon updates
 * variant-dependent blocks in place rather than re-rendering the section, so
 * without this the panel would keep declaring the first pack's net quantity
 * after a customer picked a different one.
 *
 * Every pack's rows are rendered server-side from its own metafields; this only
 * chooses which is visible. Nothing is read from the event except the id.
 */
class ComplianceDeclarationsComponent extends HTMLElement {
  /** @type {Element | null} */
  #target = null;

  connectedCallback() {
    this.#target = this.closest('[id*="ProductInformation-"], [id*="QuickAdd-"], product-card');
    if (!this.#target) return;
    this.#target.addEventListener(StandardEvents.productSelect, this.#handleProductSelect);
  }

  disconnectedCallback() {
    if (!this.#target) return;
    this.#target.removeEventListener(StandardEvents.productSelect, this.#handleProductSelect);
    this.#target = null;
  }

  /** @param {{ promise: Promise<{ detail?: any }> }} event */
  #handleProductSelect = (event) => {
    event.promise
      .then(({ detail }) => {
        if (!detail) return;

        const { newProduct, resource } = detail;
        if (newProduct) this.dataset.productId = String(newProduct.id);

        if (detail.productId != null && String(detail.productId) !== this.dataset.productId) return;
        if (!resource) return;

        this.#select(resource.id);
      })
      .catch((error) => {
        if (error?.name !== 'AbortError') console.warn('[compliance-declarations] Event promise rejected:', error);
      });
  };

  /**
   * Shows the pack matching `variantId` and hides the rest.
   * @param {string | number | undefined | null} variantId
   */
  #select(variantId) {
    if (variantId == null) return;

    const id = String(variantId);
    const packs = this.querySelectorAll('[data-variant-id]');

    // An id we did not render is not a reason to hide every pack: leaving the
    // panel as served declares the first pack, which is wrong for one variant.
    // Hiding all of them declares nothing at all, which is wrong for the page.
    if (![...packs].some((pack) => pack.dataset.variantId === id)) return;

    for (const pack of packs) {
      pack.hidden = pack.dataset.variantId !== id;
    }
  }
}

if (!customElements.get('compliance-declarations-component')) {
  customElements.define('compliance-declarations-component', ComplianceDeclarationsComponent);
}
