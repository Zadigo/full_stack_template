<template>
  <section id="subscriptions">

    <!-- New subscription -->
    <b-card v-if="!hasSubscription" class="text-center">
      <b-card-body>
        <h2 v-if="!hasSelectedSubscription" class="mb-4">You have no subscriptions</h2>
        <h2 v-else class="mb-4">Purchase <strong>{{ selectedSubscription.subscription.name }}</strong></h2>

        <img v-if="!hasSelectedSubscription" src="../../../assets/hello.svg" alt="payments" class="img-fluid">
        <img v-else src="../../../assets/payment.svg" alt="payments" class="img-fluid">

        <router-link v-if="!hasSelectedSubscription" :to="{ name: 'pricing'}" class="btn btn-primary btn-lg m-0 mt-4" role="link">
          Add new
        </router-link>

        <button v-else type="button" class="btn btn-primary btn-lg m-0 mt-4" @click="proceedToPayment">
          Proceed to payment - {{ subscriptionPrice }}
        </button>
      </b-card-body>
    </b-card>

    <!-- Active subscriptions -->
    <b-card v-else>
      <b-card-body>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla sed, aliquid debitis
        nemo aspernatur veniam itaque iusto! Excepturi laudantium commodi cupiditate,
        delectus repudiandae suscipit, quis quidem odio nostrum rem nam?

        <button type="button" class="btn btn-sm btn-danger">Delete subscription</button>
      </b-card-body>
    </b-card>

    <!-- Stripe -->
    <transition name="general">
      <router-view :price="subscriptionPrice" name="content"></router-view>
    </transition>

  </section>
</template>

<script>
import { useSubscriptions } from '@/store/subscriptions'
export default {
  name: 'SubscriptionsIterator',
  setup () {
    const store = useSubscriptions()
    return {
      store
    }
  },
  computed: {
    // ...mapGetters('subscriptionsModule', [
    //   'hasSubscription', 'hasSelectedSubscription'
    // ]),

    // ...mapState('subscriptionsModule', [
    //   'selectedSubscription'
    // ]),

    subscriptionPrice() {
      if (this.hasSelectedSubscription) {
        const { monthly, yearly } = this.selectedSubscription.subscription.prices
        return this.selectedSubscription.isMonthly ? monthly : yearly
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
