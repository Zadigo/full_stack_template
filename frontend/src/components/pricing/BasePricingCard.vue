<template>
  <div class="col-lg-3 col-md-6 mb-4">
    <div :class="{ 'border border-primary':  subscription.highlight }" class="card">
      <div class="card-header bg-white py-3">
        <p class="text-uppercase small mb-2"><strong>{{ subscription.name }}</strong></p>
        
        <h5 v-if="isMonthly" class="mb-0">{{ subscription.prices.monthly|currency }}/month</h5>
        <h5 v-else class="mb-0">{{ subscription.prices.yearly|currency }}/year</h5>
      </div>

      <div class="card-body">
        <ul class="list-group list-group-flush">
          <li v-for="feature in subscription.features" :key="feature" class="list-group-item">
            {{ feature }}
          </li>
        </ul>
      </div>

      <div class="card-footer bg-white py-3">
        <button @click="finalizeSubscription" type="button" :class="{ 'btn-primary': subscription.highlight, 'btn-success': !subscription.highlight }" class="btn btn-sm">
          Get it
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  name: 'BasePricingCard',
  props: {
    subscription: {
      type: Object,
      required: true
    },
    isMonthly: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    ...mapGetters('authenticationModule', [
      'isAuthenticated'
    ]),

    buttonLink() {
      return this.isAuthenticated ? 'profile_subscriptions' : 'signin'
    }
  },
  methods: {
    ...mapMutations('subscriptionsModule', [
      'chooseSubscription'
    ]),

    finalizeSubscription() {
      this.chooseSubscription({ subscription: this.subscription, isMonthly: this.isMonthly })
      this.$router.push({ name: this.buttonLink, query: { subscription: this.name, monthly: this.isMonthly } })
    }
  }
}
</script>
