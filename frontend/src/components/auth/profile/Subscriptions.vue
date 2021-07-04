<template>
  <section class="section" id="subscriptions">
    <b-card v-if="!hasSubscription" class="text-center">
      <b-card-body>
        <h2 v-if="!hasSelectedSubscription" class="mb-4">You have no subscriptions</h2>
        <h2 v-else class="mb-4">Purchase <strong>{{ selectedSubscription.subscription.name }}</strong></h2>

        <img v-if="!hasSelectedSubscription" src="../../../assets/hello.svg" alt="payments" class="img-fluid">
        <img v-else src="../../../assets/payment.svg" alt="payments" class="img-fluid">
        
        <router-link :to="{ name: 'pricing'}" v-if="!hasSelectedSubscription" class="btn btn-primary btn-lg m-0 mt-4" role="link">
          Add new
        </router-link>

        <button @click="proceedToPayment" v-else class="btn btn-primary btn-lg m-0 mt-4" role="button">
          Proceed to payment - {{ subscriptionPrice|currency }}
        </button>
      </b-card-body>
    </b-card>

    <b-card v-else>
      <b-card-body>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla sed, aliquid debitis nemo aspernatur veniam itaque iusto! Excepturi laudantium commodi cupiditate, delectus repudiandae suscipit, quis quidem odio nostrum rem nam?
        <button class="btn btn-sm btn-danger">Delete account</button>
      </b-card-body>
    </b-card>

    <router-view name="content"></router-view>
  </section>
</template>

<script>
export default {
  name: 'Subscriptions',
  computed: {
    hasSubscription() {
      return this.$store.getters['subscriptionsModule/hasSubscription']
    },
    selectedSubscription() {
      return this.$store.state.subscriptionsModule.selectedSubscription
    },
    hasSelectedSubscription() {
      return this.$store.getters['subscriptionsModule/hasSelectedSubscription']
    },
    subscriptionPrice() {
      if (this.hasSelectedSubscription) {
        if (this.selectedSubscription.isMonthly) {
          return this.selectedSubscription.subscription.prices.monthly
        } else {
          return this.selectedSubscription.subscription.prices.yearly
        }
      } else {
        return 0
      }
    }
  },
  methods: {
    proceedToPayment() {
      this.$store.commit('addToCart', this.selectedSubscription)
      this.$router.push({ name: 'profile_subscription_payment' })
    }
  }
}
</script>
