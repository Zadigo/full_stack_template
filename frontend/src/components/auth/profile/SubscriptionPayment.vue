<template>
  <div class="row">
    <div class="col-sm-12 col-md-12 mt-3">
      <h3 class="py-4">
        <a href="http://stripe.com/" target="_blank">
          <img :src="require('../../../assets/stripe/svg/black.svg')" class="img-fluid" alt="stripe">
        </a>
      </h3>
    </div>
    
    <div class="col-12">
      <base-card>
        <div class="form-group my-3">
          <b-checkbox id="register"><span class="m-3">Register for future payments</span></b-checkbox>
        </div>

        <button @click="requestPayment" class="btn btn-lg btn-block btn-primary">
          Pay - $0
        </button>

        <template v-slot:cardFooter>
          <i class="fa fa-cc-visa mr-2"></i>
          <i class="fa fa-cc-mastercard mr-2"></i>
        </template>
      </base-card>

      <base-card class="mt-2">
        By doing this you are aggreeing with
        <router-link :to="{ name: 'terms_of_use' }" target="_blank">CGV</router-link> and
        <router-link :to="{ name: 'terms_of_conditions' }" target="_blank">CGU</router-link>
      </base-card>
    </div>

    <div class="col-3">
      <div class="row mt-3 text-muted">
        <div class="col-12">
          <i class="fa fa-lock fa-2x"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SubscriptionPayment',
  data() {
    return {
      completed: false
    }
  },
  
  methods: {
    requestPayment() {
      this.$router.push({ name: 'profile_subscriptions' })
    }
  }
}
</script>
