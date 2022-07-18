<template>
  <section id="home">
    <!-- Navbar -->
    <base-navbar-vue />

    <!-- Main -->
    <div role="main">
      <slot></slot>
    </div>

    <!-- Floating button -->
    <transition name="slide">
      <button v-if="scrollY > 100" type="button" class="btn btn-floating btn-lg btn-dark" @click="scrollToTop">
        <font-awesome-icon icon="fa-solid fa-arrow-up" />
      </button>
      <!-- <teleport to="body">
      </teleport> -->
    </transition>

    <!-- Footer -->
    <base-footer-vue />
  </section>
</template>

<script>
import BaseNavbarVue from '@/layouts/BaseNavbar.vue'
import BaseFooterVue from '@/components/BaseFooter.vue'
import { useScroll } from '@vueuse/core'
import { ref } from 'vue'
import { scrollToTop } from '../utils'

export default {
  name: 'BaseSite',
  components: {
    BaseNavbarVue,
    BaseFooterVue
  },
  setup () {
    const target = ref(null)
    const { y, directions } = useScroll(target)
    return {
      target,
      directions,
      scrollY: y,
      scrollToTop
    }
  },
  mounted () {
    this.target = window.document
  }
}
</script>

<style scoped>
.btn-floating {
  position: fixed;
  transition: all .3s ease;
  right: 1%;
  bottom: 1%;
}
</style>
