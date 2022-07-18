<template>
  <base-jumbotron :page-description="pageDescription" :page-title="pageTitle" section-id="prices">

    <!-- Prices -->
    <div class="container">
      <section id="prices" class="text-center">
        <div class="btn-group mt-4 mb-4" role="group" aria-label="Choose billing type">
          <button :class="{ 'active': isMonthly }" type="button" class="btn btn-primary ripple-surface" style="min-width: 150px;" @click="isMonthly=true">
            Monthly billing
          </button>

          <button :class="{ 'active': !isMonthly }" type="button" class="btn btn-primary ripple-surface" style="min-width: 232px;" @click="isMonthly=false">
            Annual billing <small>(2 months FREE)</small>
          </button>
        </div>

        <div class="row gx-lg-5">
          <base-pricing-card v-for="subscription in subscriptions" :key="subscription.id" :subscription="subscription" :is-monthly="isMonthly" />
        </div>
      </section>

      <hr class="my-4">

      <!-- FAQ -->
      <section id="faq" class="mb-4">
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
import SubscriptionsData from '@/data/subscriptions.json'

export default {
  name: 'PricingView',
  title () {
    return 'Pricing'
  },
  components: {
    BasePricingCard
  },
  data () {
    return {
      subscriptions: SubscriptionsData,
      isMonthly: true,

      pageTitle: 'Plans and prices',
      pageDescription: 'Whether your time-saving automation needs are large or small, we’re here to help you scale.'
    }
  }
}
</script>
