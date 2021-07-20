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

    <!-- Companies -->
    <div id="banner p-4 mt-4 mb-4">
      <div class="container">
        <p class="text-muted text-uppercase m-0">Trusted by product-led innovators around the world</p>
        <div class="icons d-flex justify-content-between">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/60b19e258e93f171e18a3308_clearbit.svg" height=50 width=120 alt="clearbit">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/60b423729024d61e9a81a7be_logmein.svg" height=50 width=120 alt="log-me-in">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/6058c083201c15c0fa471850_privy-2021.svg" height=50 width=120 alt="privy">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/60b19e426ec9b0001bdb875c_codepen.svg" height=50 width=120 alt="codepen">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/60b19e0ae1947a43717e46e7_amplitude.svg" height=50 width=120 alt="Amplitude">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/60b19e8407fc3fd1a197b1b4_adroll.svg" height=50 width=120 alt="adroll">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/605105a4d0533067cfafabd2_profitwell-2021.svg" height=50 width=120 alt="profitwell">
          <img src="https://assets.website-files.com/5c7d318eeaea1d6e1198d906/60b19e3d86ed89aec212c20e_lyft.svg" height=50 width=120 alt="lyft">
        </div>
      </div>
    </div>

    <!-- Testimonials -->
    <Testimonials />

    <div class="container">
      <hr class="mb-5">
      
      <!-- Details -->
      <Boxes />

      <!-- CTA -->
      <base-secondary-cta />
    </div>

    <router-view name="footer" class="mt-4" />
  </div>
</template>

<script>
import Boxes from '@/components/hero/sections/Boxes.vue'
import Testimonials from '@/components/hero/sections/Testimonials.vue'

export default {
  name: 'Home',
  
  components: {
    Testimonials,
    Boxes
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
      margin-top: -58.59px;
    }
  }
</style>
