import { mount } from '@vue/test-utils';
import { describe, expect, it } from "vitest";

import HomePage from "@/pages/HomePage.vue";

describe('HomePage', () => {
    it('can render page', async () => {
        const component = mount(HomePage)
        expect(component.exists()).toBeTruthy()
    })
})
