<template>
  <base-jumbotron :pageDescription="pageDescription" :pageTitle="pageTitle" sectionId="prices">

     <!-- Prices -->
    <div class="container">
      <section class="text-center" id="prices">
        <div class="btn-group mt-4 mb-4" role="group" aria-label="Choose billing type">
          <button @click="isMonthly=true" :class="{ 'active': isMonthly }" type="button" class="btn btn-primary ripple-surface" style="min-width: 150px;">
            Monthly billing
          </button>

          <button @click="isMonthly=false" :class="{ 'active': !isMonthly }" type="button" class="btn btn-primary ripple-surface" style="min-width: 232px;">
            Annual billing <small>(2 months FREE)</small>
          </button>
        </div>

        <div class="row gx-lg-5">
          <base-pricing-card v-for="subscription in subscriptions" :key="subscription.id" :subscription="subscription" :isMonthly="isMonthly" />
        </div>
      </section>

      <hr class="my-4">

      <!-- FAQ -->
      <section class="mb-4" id="faq">
        <div class="row">
          <!-- FAQ -->
          <base-small-faq />
        </div>
      </section>
    </div>
    
  </base-jumbotron>
</template>

<script>
import BasePricingCard from '@/components/pricing/BasePricingCard.vue'
import SubscriptionsData from '../data/subscriptions.json'

export default {
  name: 'Pricing',
  
  title () {
    return 'Pricing'
  },

  components: {
    BasePricingCard
  },

  data() {
    return {
      subscriptions: SubscriptionsData,
      isMonthly: true,

      pageTitle: 'Plans and prices',
      pageDescription: 'Whether your time-saving automation needs are large or small, we’re here to help you scale.'
    }
  }
}
</script>
