<template>
  <section class="site">
    <BaseNavbar />
    
    <div class="container">
      <RouterView />
    </div>
  </section>
</template>

<script setup lang="ts">
import BaseNavbar from '@/components/BaseNavbar.vue';
</script>
