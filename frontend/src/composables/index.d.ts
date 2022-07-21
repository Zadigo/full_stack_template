import { ComponentPublicInstance, Ref } from 'vue'

declare type VueInstance = ComponentPublicInstance

declare interface DefaultOptions {
    clientId?: string
    scope?: string,
    discoveryDocs?: object
}

/**
 * Use Google authentication 
 */
declare module socials {
    declare function useGoogleAuthentication (instance: VueInstance, options?: DefaultOptions):  {
        authentifiedUser: {
            userid: null,
            email: null,
            emailVerified: null,
            name: null,
            pictureUrl: null
        }
        isAuthorized: Ref<boolean>
        load (): void
        authenticate (accessToken: string): void
        signin (success: () => any, error: (response: boolean) => any): Awaited<Promise<boolean>>
    }
}
