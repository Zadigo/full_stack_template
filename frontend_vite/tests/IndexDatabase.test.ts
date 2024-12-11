import useIndexDatabase from "@/plugins/db";
import { describe, it } from "vitest";

describe('IndexDatabase', () => {
    it('can connect to database', async () => {
        const { createConnection } = useIndexDatabase()
        const awaitable = createConnection('testing')
        // expectTypeOf(awaitable).resolves.toBeFunction
        console.log(awaitable)
    })
})
