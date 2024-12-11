import { defineStore } from 'pinia'
import { computed, ref } from "vue"
import { useAxios } from "../plugins"
import { Post } from "../types"

export default defineStore('posts', () => {
    const posts = ref<Post[]>([])

    const hasPosts = computed(() => {
        return posts.value.length > 0
    })

    async function getPosts (callback?: (data: Post[]) => void) {
        const { createClient } = useAxios()
        const client = createClient()
        const response = await client.get<Post[]>('/posts')
        posts.value = response.data
        
        if (callback && typeof callback === 'function') {
            callback(posts.value)
        }
    }

    return {
        posts,
        hasPosts,
        getPosts
    }
})
