<template>
  <section id="dashboard" style="z-index:150;">
    <base-header />
    
    <main style="margin-top:58px;">
      <div class="container pt-4">
        <router-view :key="$route.name" />
      </div>
    </main>
  </section>
</template>

<script>
import BaseHeader from '@/components/admin/nav/BaseHeader.vue'
export default {
  name: 'DashboardSite',
  components: {
    BaseHeader
  }
}
</script>

<style>
/* @import url('@/assets/admin.css'); */
</style>
