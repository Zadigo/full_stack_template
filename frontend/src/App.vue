<template>
  <div id="app">
    <!-- <v-app> -->
      <!-- Nav -->
      <router-view name="nav" class="navbar-light" />

      <!-- Content -->
      <transition name="general-transition" mode="out-in">
        <router-view :key="$route.name"></router-view>
      </transition>

      <!-- Footer -->
      <router-view name="footer" />
    <!-- </v-app> -->
  </div>
</template>

<script>
// import { isUndefined } from 'lodash'

export default {
  name: 'App'
  // beforebRouteEnter (to, from, next) {
  //   next(vm => {
  //     var cachedToken = localStorage.getItem('tok')
  //     var isAuthenticated = vm.$store.getters['authenticationModule/isAuthenticated']
  //     if (!isUndefined(cachedToken) && isAuthenticated) {
  //       return true
  //     }
  //     if (isAuthenticated) {
  //       return true
  //     }
  //     return 'signin'
  //   })
  // }
  // beforeMount() {
  //   this.runStripe('js.stripe.com/v3/', function (vm) {
  //     console.log(vm)
  //   })
  // }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900');
  @import url('https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css');
  @import url('https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css');
  @import url('https://cdn.jsdelivr.net/npm/mdbvue/lib/css/mdb.min.css');

  html, body {
    font-family: 'Roboto', sans-serif;
  }

  #app {
    font-family: 'Roboto', sans-serif;
  }
</style>
