<template>
  <article class="col-lg-3 col-md-6 mb-4">
    <div :class="{ 'border border-primary': subscription.highlight }" class="card">
      <div class="card-header bg-white py-3">
        <p class="text-uppercase small mb-2"><strong>{{ subscription.name }}</strong></p>

        <h5 v-if="isMonthly" class="mb-0">{{ subscription.prices.monthly }}/month</h5>
        <h5 v-else class="mb-0">{{ subscription.prices.yearly }}/year</h5>
      </div>

      <div class="card-body">
        <ul class="list-group list-group-flush">
          <li v-for="feature in subscription.features" :key="feature" class="list-group-item">
            {{ feature }}
          </li>
        </ul>
      </div>

      <div class="card-footer bg-white py-3">
        <button type="button" :class="[subscription.highlight ? 'btn-primary' : 'btn-secondary']" class="btn btn-sm" @click="finalize">
          Get it
        </button>
      </div>
    </div>
  </article>
</template>

<script>
import { useAuthentication } from '@/store/authentication'
import { useSubscriptions } from '@/store/subscriptions'
import { storeToRefs } from 'pinia'

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
  setup () {
    const store = useAuthentication()
    const subscriptionStore = useSubscriptions()
    const { isAuthenticated } = storeToRefs(store)
    return {
      subscriptionStore,
      isAuthenticated
    }
  },
  methods: {
    finalize () {
      const redirectLink = this.isAuthenticated ? 'profile_subscriptions_view' : 'login_view'
      const data = { subscription: this.subscription, isMonthly: this.isMonthly }
      this.subscriptionStore.chooseSubscription(data)
      this.$localstorage.create('selectedSubscription', data)
      this.$router.push({ name: redirectLink, query: { subscription: this.subscription.name, monthly: this.isMonthly } })
    }
  }
}
</script>
