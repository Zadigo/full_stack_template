<template>
  <b-card class="mt-4 mb-5">
    <b-card-body>
      <div class="row">
        <div class="col-sm-12 col-md-5 offset-md-1">
          <h3>Try {{ companyDetails.name }} for 14 days</h3>
          <p>No credit card required. No obligations or fixed-term contracts.</p>
        </div>

        <div class="col-sm-12 col-md-5">
          <div class="form-group">
            <input v-model="email" type="email" id="email" class="form-control" placeholder="Email" autocomplete="email">
            <privacy-text class="mt-2" />
          </div>
        </div>
      </div>
    </b-card-body>
  </b-card>
</template>

<script>

export default {
  data() {
    return {
      email: null
    }
  },

  components: {
    
  }
}
</script>
