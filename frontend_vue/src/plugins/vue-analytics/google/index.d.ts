/**
 * Create a Google Analytics instance
 * 
 * @param {String} tag - Google Analytics tag
 * @param {Object} options - Options for the instance
 */
declare interface AnalyticsOptions {
    /** Currency to use (defaults: EUR) */
    currency?: string
}

export type DEFAULT_CURRENCY = 'EUR'

export type DEFAULT_BRAND = unknown

export enum DEFAULT_DIMENSIONS {
    Affiliation = 'affiliation',
    Coupon = 'coupon',
    Currency = 'currency',
    Discount = 'discount',
    Index = 'index',
    ItemId = 'item_id',
    ItemBrand = 'item_brand',
    ItemCategory = 'item_category',
    ItemCategory2 = 'item_category_2',
    ItemCategory3 = 'item_category_3',
    ItemCategory4 = 'item_category_4',
    ItemCategory5 = 'item_category_5',
    ItemLocationId = 'item_location_id',
    ItemListId = 'item_list_id',
    ItemListName = 'item_list_name',
    ItemName = 'item_name',
    ItemVariant = 'item_variant',
    Price = 'price',
    Quantity = 'quantity'
}

enum ContentTypes {
    ImageJPG = 'image/jpg',    
    ImageJPEG = 'image/jpeg',
}

declare interface Product {
    name: string,
    price: number
}

declare interface PromotionOptions {
    promotionId: number,
    promotionName: string,
    creativeSlot: string,
    locationId: string
}

declare interface ItemOptions {
    item: string,
    listName: string,
    listId: number | string
}

/**
 * Create a Google Analytics instance
 * 
 * @param {String} tag - Google Analytics tag
 * @param {Object} options - Options for the instance
 */
export declare function createGoogleAnalytics(tag: String, options?: AnalyticsOptions): () => Object

export declare function useAnalytics(): void

export declare module functions {
    export declare function createProduct(id: string | number, name: string, price: string | number, category: string, discount: string | number, coupon: string, index: string | number): Object
    /**
     * Resets the datalayer container
     */
    export declare function reset(): void
    /**
     * Creates a login signal
     * 
     * @param {String} method - 
     */
    export declare function login(method: string): void
    /**
     * Creates a signup signal
     * 
     * @param {String} method - 
     */
    export declare function signup(method: string): void
    /**
     * Creates a signal for when a content
     * is shared from the website
     * 
     * @param {String} method - 
     * @param {String} contentType - 
     * @param {String|Number} itemId - 
     */
    export declare function share(method: string, contentType: ContentTypes, itemId: string | number): void
    /**
     * Creates a signal for when the page
     * was vieweed
     * 
     * @param {String} path - 
     * @param {String} title - 
     */
    export declare function pageView(path: string, title: string): void
    /**
     * Creates a signal for when a search is
     * completed on the website
     * 
     * @param {String} searchTerm - 
     */
    export declare function search(searchTerm: string): void
    /**
     * Used to create a custom event
     * 
     * @param {String} event - 
     * @param {String} eventCategory - 
     * @param {String} payload - 
     */
    export declare function createEvent (event: string, eventCategory: string, payload: object): void
    /**
     * Generates a view for when the
     * user see's an item
     * 
     * @param {String} item - 
     * @param {String} listName - 
     * @param {String|Number} listId - 
     */
    export declare function selectItem(ItemOptions): void
    /**
     * Generates a view for when the
     * user see's an item
     * 
     * @param {String} item - 
     * @param {String} listName - 
     * @param {String|Number} listId - 
     */
    export declare function viewItem(ItemOptions): void
    /**
     * Event for multiple products
     * 
     * @param {Array} items - List of products
     * @param {Object} currentItem - Current product
     */
    export declare function viewItems (items: Product[], currentItem: Product): void
    /**
    * Event for visiting the cart page
    * 
    * @param {Array} items - List of products
    */
    export declare function viewCart (items: Product[]): void
    /**
    * Event for viewing a promotion
    * 
    * @param {String|Number} promotionId - The promotion's ID 
    * @param {String} promotionName - The name of the promotion
    * @param {String} creativeSlot - 
    * @param {String} locationId - The location of the promotion on the page
    */
    export declare function viewPromotion(PromotionOptions): void
     /**
     * Event for clicking on a promotion
     * 
     * @param {String|Number} promotionId - The promotion's ID 
     * @param {String} promotionName - The name of the promotion
     * @param {String} creativeSlot - 
     * @param {String} locationId - The location of the promotion on the page
    */
    export declare function selectPromotion(PromotionOptions): void
    /**
     * Event for when the user select's an
     * element of somekind on the page
     * 
     * @param {String} contentType - The element's content type
     * @param {String|Number} itemId - The element's ID
    */
    export declare function selectContent (contentType: ContentTypes, itemId: number): void
    /**
     * Trigger for when the user adds an item
     * to the cart
     * 
     * @param {Object} contentType - Product
     * @param {String|Number} value - The total value of the cart
    */
    export declare function addToCart(item: Product, value: number): void
    /**
     * Trigger for when the user removes an item
     * from the cart
     * 
     * @param {Object} item - Product
     * @param {String|Number} value - The total value of the cart
    */
    export declare function removeFromCart(item: Product, value: number): void
    /**
     * Trigger for when the user adds an item
     * to his wishlist
     * 
     * @param {Object} contentType - Products
     * @param {String|Number} value - The total value of the wishlist
    */
    export declare function addToWishlist(item: Product, value: number): void
    /**
     * Event for checkout begin
     * 
     * @param {Array} items - Products
     * @param {String|Number} value - The total value of the cart
    */
    export declare function beginCheckout(items: Product[], value: number): void
    /**
     * Event for clearing a cart
     * 
     * @param {Array} items - Products
     * @param {String|Number} value - The total value of the cart
    */
    export declare function clearCart (items: Product[], value: number): void
    /**
     * Event for adding shipping infos
     * 
     * @param {Array} items - Products
     * @param {String|Number} value - The total value of the cart
    */
    export declare function addShippingInfo (items: Product[], value: number): void
    /**
     * Event for adding billing infos
     * 
     * @param {Array} items - Products
     * @param {String|Number} value - The total value of the cart
    */
    export declare function addBillingInfo (items: Product[], value: number): void
    /**
     * Event for purchasing a product
     * 
     * @param {Array} items - Products
     * @param {String|Number} value - The total value of the cart
     * @param {String} transactionId - The ID of the transaction
    */
    export declare function purchase(items: Product[], value: number, transactionId: string): void
    /**
     * Event for reaching the success page
     * 
     * @param {Array} items - Products
     * @param {String|Number} value - The total value of the cart
    */
    export declare function successPage(items: Product[], value: number): void
    /**
     * Measure page timing
     * 
     * @param {String} eventCategory -
    */
    export declare function measureTiming(eventCategory: string)
    /**
     * Event for creating and exception
     * 
     * @param {String} description - Description of the exception
     * @param {String} fatal - The number of the exception
    */
    export declare function exception (description: string, fatal: number)
}
