<template>
  <base-hero :image="image">
    <template v-slot:navigation>
      <BaseNavigation :navbarDark="true" />
    </template>

    <template v-slot:lead>

       <div class="text-white">
        <h1 class="display-4 font-weight-bold mb-3" :aria-label="lead">{{ lead }}</h1>
        <hr class="divider-light">
        <h5 class="mb-4" :aria-label="description">{{ description }}</h5>
        
        <!-- Call to action -->
        <router-link :to="{ name: 'signin' }" class="btn btn-outline-light btn-lg m-2" role="button" rel="nofollow">
          Start tutorial
        </router-link>      
      </div>

    </template>

    <template>
      <Companies />

      <CTA class="pink darken-3" />


      <div class="container">
        <Testimonials />

        <AdditionalBenefits />

        <Team />

        <BaseSecondaryCTA />
      </div>
    </template>
  </base-hero>
</template>

<script>
import BaseHero from '../components/BaseHero.vue'
import BaseNavigation from '../components/BaseNavigation.vue'
import AdditionalBenefits from '../components/hero/sections/AdditionalBenefits.vue'
import Testimonials from '../components/hero/sections/Testimonials.vue'
import CTA from '../components/hero/sections/CTA.vue'
import Companies from '../components/hero/sections/Companies.vue'
import Team from '../components/hero/sections/Team.vue'
import BaseSecondaryCTA from '../components/BaseSecondaryCTA.vue'

export default {
  name: 'TestHome',
  components: { BaseHero, BaseNavigation, BaseSecondaryCTA, AdditionalBenefits, CTA, Companies, Testimonials, Team },

  title () {
    return 'Home'
  },

  data () {
    return {
      lead: 'Create simple templates with Zappier',
      description: 'The best way to create websites with us',
      image: 'https://images.unsplash.com/photo-1575939238474-c8ada13b2724?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
    }
  }
}
</script>
