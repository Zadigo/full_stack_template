<template>
  <div class="row">
    <div v-for="post in posts" :key="post.useId" class="col-sm-12 col-md-12">
      <div class="card mb-1 shadow-sm">
        <div class="card-body">
          {{ post.body }}
        </div>
      </div>
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
const posts = useSessionStorage<Post[]>('posts', [], {
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
