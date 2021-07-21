<template>
  <base-card class="mt-4 mb-5">
    <div class="row">
      <div class="col-sm-12 col-md-5 offset-md-1">
        <h3>Try {{ companyDetails.name }} for 14 days</h3>
        <p>No credit card required. No obligations or fixed-term contracts.</p>
      </div>

      <div class="col-sm-12 col-md-5">
        <div class="form-group">
          <input @keypress.enter="subscribeUser" v-model="email" type="email" id="email" class="form-control" aria-label="Email" placeholder="Email" autocomplete="email">
          <base-privacy-text class="mt-2" />
        </div>
      </div>
    </div>
  </base-card>
</template>

<script>
export default {
  name: 'BaseSecondaryCTA',
  data() {
    return {
      email: null
    }
  },

  methods: {
    subscribeUser() {
      this.$api.subscribe(this.email)
      .then((response) => {
        console.log(response)
        this.email = null
      })
      .catch((error) => {
        console.error(error)
      })
    }
  }
}
</script>
