<template>
  <section id="pricing">
    <header>
      <!-- Jumbotron -->
      <div id="intro" class="p-5 text-center bg-light">
        <h1 class="mb-3 font-weight-bold">Plans & Pricing</h1>
        <p class="font-weight-bold">
          Whether your time-saving automation needs are large or small, we’re here to help you scale.
        </p>
      </div>
    </header>

    <!-- Prices -->
    <div class="container">
      <section class="text-center" id="prices">
        <!-- <h4 class="mb-4"><strong>Pricing</strong></h4> -->

        <div class="btn-group mt-4 mb-4" role="group" aria-label="Choose billing type">
          <button @click="isMonthly=true" :class="{ 'active': isMonthly }" type="button" class="btn btn-primary ripple-surface" style="min-width: 150px;">
            Monthly billing
          </button>

          <button @click="isMonthly=false" :class="{ 'active': !isMonthly }" type="button" class="btn btn-primary ripple-surface" style="min-width: 232px;">
            Annual billing <small>(2 months FREE)</small>
          </button>
        </div>

        <div class="row gx-lg-5">
          <PricingCard v-for="subscription in subscriptions" :key="subscription.id" :subscription="subscription" :isMonthly="isMonthly" />
        </div>
      </section>

      <!-- FAQ -->
      <hr class="my-4">

      <section class="mb-4" id="faq">
        <div class="row">
          <small-faq />
        </div>
      </section>
    </div>    
  </section>
</template>

<script>
import PricingCard from '@/components/pricing/Card.vue'

export default {
  name: 'Pricing',
  
  title () {
    return 'Pricing'
  },

  components: {
    PricingCard
  },

  data() {
    return {
      subscriptions: [
        { id: 1, name: 'Free', features: ['Feature1', 'Feature2', 'Feature3'], prices: { monthly: 19, yearly: 24 }, highlight: false },
        { id: 2, name: 'Essential', features: ['Feature1', 'Feature2', 'Feature3', 'Feature4'], prices: { monthly: 22, yearly: 26 }, highlight: true },
        { id: 3, name: 'Advanced', features: ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'], prices: { monthly: 83, yearly: 75 }, highlight: false },
        { id: 4, name: 'Enterprise', features: ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5', 'Feature6'], prices: { monthly: 129, yearly: 79 }, highlight: false },
      ],
      isMonthly: true
    }
  }
}
</script>

<style scoped>
  /* #intro {
    margin-top: 58px;
  } */

  /* Margin to fix overlapping fixed navbar */
  /* @media (max-width: 991px) {
    #intro {
      margin-top: 45px;
    }
  } */
</style>
