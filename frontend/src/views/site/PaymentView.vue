<template>
  <section id="payment" class="mt-4 pt-4">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-4 offset-md-3">
          <h3 class="py-4">
            <a href="http://stripe.com/" target="_blank" rel="noopener noreferrer">
              <img :src="require('@/assets/stripe/svg/black.svg')" class="img-fluid" alt="stripe">
            </a>
          </h3>
        </div>

        <div class="col-sm-12 col-md-4 offset-md-3">
          <b-card>
            <b-card-body>
              <div class="form-group my-3">
                <b-checkbox id="register"><span class="m-3">Register for future payments</span></b-checkbox>
              </div>

              <button type="button" class="btn btn-lg btn-block btn-primary" @click="requestPayment">
                Pay - $0
              </button>
            </b-card-body>

            <template #footer>
              <i class="fa fa-cc-visa mr-2"></i>
              <i class="fa fa-cc-mastercard mr-2"></i>
            </template>
          </b-card>

          <b-card class="mt-2">
            <b-card-text>
              By doing this you are aggreeing with
              <router-link :to="{ name: 'terms_of_use' }" target="_blank">CGV</router-link> and
              <router-link :to="{ name: 'terms_of_conditions' }" target="_blank">CGU</router-link>
            </b-card-text>
          </b-card>
        </div>

        <div class="col-3">
          <b-card>
            <b-card-text>
              Lorem ipsum dolor sit amet consectetur
              adipisicing elit. Architecto nobis tempore
              qui excepturi necessitatibus maiores ducimus
              nostrum, sequi similique illo, ipsa dolorum
              voluptas, amet a libero commodi impedit iste
              inventore?
            </b-card-text>
          </b-card>

          <div class="row mt-3 text-muted">
            <div class="col-12">
              <i class="fa fa-lock fa-2x"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'PaymentView',
  data() {
    return {
      completed: false
    }
  },
  methods: {
    requestPayment() {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>
