<template>
  <section class="section">
    <div class="row">
      <div class="col-12">
        <b-card>
          <b-card-body>
            <h2>Welcome <strong>{{ firstName }},</strong></h2>
          </b-card-body>
        </b-card>
      </div>
      
      <div class="col-12">
        <b-card class="mt-2">
          <b-card-body>
            <img src="../../../assets/hello.svg" class="img-fluid" alt="overview" role="img" aria-label="Account overview">
          </b-card-body>
        </b-card>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  computed: {
    firstName() {
      return this.$store.state.profileModule.userDetails.firstname
    }
  }
}
</script>
