import { App, ComponentCustomProperties, Ref } from 'vue'

declare type DictionnaryKey = {
    key: string
}

/** Creates a VueLocalStorage instance that can be used by a Vue app */
export declare function createLocalStorage(options?: BaseOptions): VueLocalStorage

/** Creates a VueSession instance that can be used by a Vue app */
export declare function createVueSession(options?: VueSessionOptions): VueSession

export declare interface BaseOptions {
    /** The default session key (default: vue-session) */
    sessionKey?: number
    /** Initial values with which to initialize the storage */
    initial?: object
}

/** 
 * VueLocalStorage allows serializing and deserializing
 * data in the base Window locale storage
 */
export declare interface VueLocalStorage {
    /** The default session key (defaults: vue-session) */
    readonly DEFAULT_KEY_NAME: string
    /**
     * Returns all items saved in the localStorage
     *
     * @returns dictionnary
     */
    readonly data: object

    constructor(options?: BaseOptions): void
    /**
     * Returns the value store under a given key
     *
     * @param key - key to use
     * @returns an object, a number or an array
     */
    retrieve (key: DictionnaryKey): object | string | number
    /**
     * Creates a new record under the given key
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    create(key: DictionnaryKey, value: unknown): void
    /**
     * Removes an element stored under a given key
     *
     * @param key key of the element to remove
     * @returns null
     */
    remove(key: DictionnaryKey): void
    /**
     * Saves an item globally in the local storage
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    save(key: DictionnaryKey, value: unknown): void
    /**
     * Returns a value saved globally and not under the session key
     *
     * @param key - key under which to save the element
     * @returns number, array or dictionnary
     */
    getValue(key: DictionnaryKey): object | string | number

    install(app: App): void
}

/** Possible options for VueSession */
export declare interface VueSessionOptions extends BaseOptions {
    /** Persist the data in the local storage */
    persistent?: boolean
}

/** 
 * VueSession allows serializing and deserializing
 * data easily in the base Window session storage
 */
export declare interface VueSession {
    /** The default session key (defaults: vue-session) */
    readonly DEFAULT_KEY_NAME: string
    /**
     * Returns all items saved in the storage
     *
     * @returns dictionnary
     */
    readonly data: object

    constructor(options?: VueSessionOptions): void
    /**
     * Creates a new record under the given global key
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    create(key: DictionnaryKey, value: unknown): void
    /**
     * Returns the value store under a given key
     *
     * @param key - key to use
     * @returns an object, a number or an array
     */
    retrieve(key: DictionnaryKey): number | string | number[] | string[]
    /**
     * Removes an element stored under a given key
     *
     * @param key key of the element to remove
     * @returns null
     */
    remove(key: DictionnaryKey): void
    /**
     * Renews the session key
     */
    renew(): void
    /**
     * Clears all data stored under the global key
     */
    clear(): void
    /**
     * Checks whether a key exists in the storage
     *
     * @param key key of the element to remove
     * @returns Boolean
     */
    contains(key: DictionnaryKey): boolean
    /**
     * Destroys the session
     */
    destroy(): void
    /**
     * Tries to get a key and eventually creates
     * a new record with the given value if it
     * does not exist
     *
     * @param key - key of the element to remove
     * @param defaultValue - key of the element to remove
     */
    getOrCreate(key: DictionnaryKey, defaultValue: unknown): number | object
    /**
     * Tries to push the incoming element to an 
     * array stored under the given key
     *
     * @param key - key of the element to remove
     * @param value - value to add
     */
    updateArray(key: DictionnaryKey, value: unknown): void
    /**
     * Toggle a boolean stored under a given key
     * 
     * @param key - key of the element to toggle
     */
    toggle(key: DictionnaryKey): void

    install(app: App): void
}

declare module '@vue/runtime-core' {
    export interface ComponentCustomProperties {
        /** Current data saved under the VUE_SESSION_KEY */
        localStorage: object
        /** Current data saved under VUE_SESSION_KEY */
        sessionStorage: object
        /** The VueLocalStorage instance */
        $localstorage: VueLocalStorage
        /** The VueSession instance */
        $session: VueSession
    }
}
