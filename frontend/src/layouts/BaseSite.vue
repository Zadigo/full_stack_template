<template>
  <section id="home">
    <!-- Navbar -->
    <base-navbar-vue />

    <!-- Main -->
    <slot></slot>
    
    <!-- Footer -->
    <base-footer-vue />
  </section>
</template>

<script>
import BaseNavbarVue from '@/layouts/BaseNavbar.vue'
import BaseFooterVue from '@/components/BaseFooter.vue'

export default {
  name: 'BaseSite',
  components: {
    BaseNavbarVue,
    BaseFooterVue
  }
}
</script>
