<template>
  <base-site-vue>
    <template #default>
      <base-intro-vue class="border-bottom mb-4" height="50vh">
        <template #default>
          <div class="py-5 my-5 text-center">
            <h1 class="display-5 fw-bold">Centered hero</h1>
            <div class="col-lg-6 mx-auto">
              <p class="lead mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
            </div>
          </div>
        </template>
      </base-intro-vue>

      <!-- Prices -->
      <div class="container">
        <section id="prices" class="text-center">
          <div class="btn-group my-4" role="group" aria-label="Choose billing type">
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
        <section id="faq" class="mb-5">
          <div class="row">
            <div class="col-sm-12 col-md-8 offset-md-2">
              <h2 class="font-weight-bold my-5 text-center">Frequently Asked Questions</h2>
              <base-accordion-vue :items="faq" />
            </div>
          </div>
        </section>
      </div>
    </template>
  </base-site-vue>
</template>

<script>
import BaseAccordionVue from '@/layouts/BaseAccordion.vue'
import BaseIntroVue from '@/layouts/BaseIntro.vue'
import BasePricingCard from '@/components/pricing/BasePricingCard.vue'
import BaseSiteVue from '@/layouts/BaseSite.vue'
import SubscriptionsData from '@/data/subscriptions.json'

import faq from '@/data/faq.json'

export default {
  name: 'PricingView',
  title () {
    return 'Pricing'
  },
  components: {
    BaseAccordionVue,
    BaseIntroVue,
    BasePricingCard,
    BaseSiteVue
  },
  setup () {
    return {
      faq
    }
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
