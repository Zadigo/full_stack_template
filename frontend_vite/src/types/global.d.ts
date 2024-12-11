import { AxiosInstance } from 'axios'
import dayjs from 'dayjs'

declare module '@vue/runtime-core' {
    interface ComponentCustomProperties {
        $client: AxiosInstance
        $date: dayjs.Dayjs
    }
}
