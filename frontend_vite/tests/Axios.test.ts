import { Post } from "@/types";
import { describe, expect, it } from "vitest";
import { useAxios } from "../src/plugins";

describe("Use Axios", () => {
    it.todo('returns environment API url', () => {
        const { getBaseUrl } = useAxios()
        const result = getBaseUrl()

        expect(result).toContain('jsonplaceholder.typicode.com')
        expect(result.startsWith('http')).toBeTruthy()
    })

    it('can return custom url', async () => {
        const { getBaseUrl } = useAxios()
        let result = getBaseUrl('http://example.com')

        expect(result).toEqual('http://example.com/')

        result = getBaseUrl('http://example.com', 'api/v1/')
        expect(result).toContain('/api/v1/')
    })

    it.skip('can return client', async () => {
        const { createClient } = useAxios()
        const client = createClient()
        const result = await client.get<Post[]>('/posts')
        expect(result.data.length > 0).toBeTruthy()
    })
})
