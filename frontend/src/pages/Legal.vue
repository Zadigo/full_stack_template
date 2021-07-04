<template>
  <div class="container">
    <section class="section mt-3 pt-3">
      <div class="row">
        <div class="col-sm-12 col-md-8 offset-md-2">
          <b-card>
            <b-breadcrumb :items="items" role="navigation"></b-breadcrumb>
          </b-card>
        </div>

        <div class="col-sm-12 col-md-8 offset-md-2">
          <router-view />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { text: 'Home', to: { name: 'home'} },
        { text: this.$route.meta.verboseName, active: true },
      ]
    }
  }
}
</script>
