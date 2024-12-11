<template>
  <Suspense>
    <template #default>
      <AsyncWelcomeBlock />
    </template>

    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>

<script setup lang="ts">
import { useHead } from 'unhead';
import { defineAsyncComponent } from 'vue';

useHead({
  title: 'Posts',
  meta: [
    {
      key: 'description',
      content: 'Some quick posts'
    }
  ]
})

const AsyncWelcomeBlock = defineAsyncComponent({
  loader: async () => import('@/components/WelcomeBlock.vue')
})
</script>
