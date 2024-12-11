<template>
  <div class="card">
    <div class="card-body">
      {{ posts }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { Post } from '@/types';
import { useSessionStorage } from '@vueuse/core'

import usePosts from '@/stores/posts'
import { storeToRefs } from 'pinia';

const store = usePosts()
const { hasPosts } = storeToRefs(store)
const posts = useSessionStorage('posts', [], {
  serializer: {
    read (raw) {
      return JSON.parse(raw)
    },
    write (value) {
      return JSON.stringify(value)
    },
  }
})

console.log(hasPosts)

if (posts.value.length === 0) {
  store.getPosts((data: Post[]) => {
    posts.value = data
  })
}
</script>
