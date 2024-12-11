import { App } from "vue";
import { useCookies } from '@vueuse/integrations/useCookies'
import './fontawesome'

import axios, { AxiosInstance } from 'axios'
import WebFont from "webfontloader";
import dayjs from 'dayjs'

export interface AuthenticationApiResponse {
    access: string
    refresh: string
}

export type RefreshApiResponse = Pick<AuthenticationApiResponse, 'access'>

export function useAxios() {
    const cookie = useCookies(['authentication'], {
        autoUpdateDependencies: true
    })

    function getBaseUrl(path?: string | null, url?: string | null) {
        let baseUrl = url ? url : import.meta.env.VITE_BASE_API_DOMAIN
        
        const baseLoc = import.meta.env.DEV ? 'http' : 'https'
        const basePath = path ? path : '/'

        if (baseUrl) {
            if (!baseUrl.startsWith('http')) {
                baseUrl = `${baseLoc}://${baseUrl}`
            }
        }

        if (!baseUrl) {
            return ''
        } else {
            const instance = new URL(basePath, baseUrl)
            return instance.toString()
        }

    }

    function createClient(path?: string | null, url?: string | null): AxiosInstance {
        const client = axios.create({
            baseURL: getBaseUrl(path, url),
            headers: { 'Content-Type': 'application/json' },
            timeout: 10000
        })

        return client
    }

    function defaultClient(bearer: string = 'Token') {
        const client = createClient()

        client.interceptors.request.use(
            request => {
                const accessToken = cookie.get<string>('access')

                if (accessToken) {
                    request.headers.Authorization = `${bearer} ${accessToken}`
                }

                return request
            },
            error => {
                return Promise.reject(error)
            }
        )

        client.interceptors.response.use(
            (response) => {
                return response
            },
            async (error) => {
                // Sequence that refreshes the access token when
                // we get a 401 code trying to access a page

                const originalRequest = error.config
                
                if (error.response.status === 401 && !originalRequest._retry) {
                    originalRequest._retry = true

                    try {
                        const refreshClient = createClient('/auth/v1/')
                        const response = await refreshClient.post<RefreshApiResponse>('/token/refresh', {
                            refresh: cookie.get<string>('refresh')
                        })
                        originalRequest.headers.Authorization = `${bearer} ${response.data.access}`
                        return client(originalRequest)
                    } catch (refreshError) {
                        return Promise.reject(refreshError)
                    }
                }
                return Promise.reject(error)
            }
        )
        return client
    }

    return {
        getBaseUrl,
        createClient,
        defaultClient
    }
}

export default function installPlugins() {
    WebFont.load({
        google: {
            families: ['Roboto']
        },
        fontactive(_familyName, _fvd) {
            // pass
        }
    })

    return {
        install(app: App) {
            const { defaultClient } = useAxios()

            app.provide('$client', defaultClient())
            app.provide('$date', dayjs())
        }
    }
}
