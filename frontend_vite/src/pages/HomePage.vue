<template>
  <div class="section my-5">
    <div class="row">
      <div class="col-sm-12 col-md-4 offset-md-4">
        <Suspense>
          <template #default>
            <AsyncWelcomeBlock />
          </template>

          <template #fallback>
            Loading...
          </template>
        </Suspense>
      </div>
    </div>
  </div>
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
