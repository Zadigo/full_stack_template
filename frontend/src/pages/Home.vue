<template>
  <div id="hero">
    <header>
      <router-view name="nav" class="navbar-dark" />

      <div class="bg-image shadow-2-strong" id="intro">
        <div class="mask">
          <div class="container h-100 d-flex align-items-center justify-content-center text-center">
            <router-view lead="Create your beautiful templates with Vue" description="Simple templates for Vue" />
          </div>
        </div>
      </div>
    </header>

    <CTA class="blue darken-3" />

    <!-- Companies -->
    <div class="p-4 mt-2 mb-4 text-center" id="banner">
      <div class="container">
        <p class="text-muted text-uppercase mb-3">Trusted by product-led innovators around the world</p>
        <div class="icons d-flex justify-content-between d-wrap">
          <img v-for="company in companies" :key="company.alt" :src="company.image" :alt="company.alt" height=50 width=120>
        </div>
      </div>
    </div>

    <!-- Testimonials -->
    <Testimonials />

    <div class="container">
      <hr class="mb-5">
      
      <!-- Details -->
      <Boxes />

      <!-- Cta -->
      <base-secondary-cta />
    </div>

    <router-view name="footer" class="mt-4" />
  </div>
</template>

<script>
import Boxes from '@/components/hero/sections/Boxes.vue'
import Testimonials from '@/components/hero/sections/Testimonials.vue'
import CTA from '../components/hero/sections/CTA.vue'

import companies from '../data/companies.json'

export default {
  name: 'Home',
  
  components: {
    Testimonials,
    Boxes,
    CTA
  },

  data () {
    return {
      companies: companies
    }
  }
}
</script>

<style scoped>
  #intro {
    background-image: url("https://images.unsplash.com/photo-1492633423870-43d1cd2775eb?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1280&q=80");
    height: 100vh;
  }

  /* Height for devices larger than 576px */
  @media (min-width: 992px) {
    #intro {
      /* margin-top: -58.59px; */
      margin-top: -70px;
    }
  }
</style>
