<template>
  <div id="app">
    <!-- <keep-alive> -->
      <!-- Nav -->
      <router-view name="nav" class="navbar-light" />
    <!-- </keep-alive> -->

    <!-- <transition name="general-transition" mode="out-in"> -->
      <!-- Content -->
      <router-view :key="$route.name"></router-view>
    <!-- </transition> -->

    <!-- <keep-alive> -->
      <!-- Footer -->
      <router-view name="footer" />
    <!-- </keep-alive> -->
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
  @import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');
  /* @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'); */
  @import url('https://cdn.jsdelivr.net/npm/mdbvue/lib/css/mdb.min.css');
</style>
