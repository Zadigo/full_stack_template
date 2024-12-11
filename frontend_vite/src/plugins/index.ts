import { App } from "vue";

import './fontawesome'

import axios, { AxiosInstance } from 'axios'
import WebFont from "webfontloader";
import dayjs from 'dayjs'

export function useAxios() {
    function getBaseUrl(url?: string | null, path?: string | null) {
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

    function createClient(url?: string | null, path?: string | null): AxiosInstance {
        const client = axios.create({
            baseURL: getBaseUrl(url, path),
            headers: { 'Content-Type': 'application/json' },
            timeout: 10000
        })

        return client
    }

    function defaultClient() {
        const client = createClient()

        client.interceptors.request.use(
            request => {
                return request
            },
            error => {
                return Promise.reject(error)
            }
        )

        client.interceptors.response.use(
            response => {
                return response
            },
            error => {
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
            app.config.globalProperties.$client = defaultClient()
            app.config.globalProperties.$date = dayjs()
        }
    }
}
