<template>
  <div id="app">
    <v-app>
      <!-- Nav -->
      <router-view name="nav" />

      <!-- Content -->
      <transition name="general-transition" mode="out-in">
        <router-view :key="$route.name"></router-view>
      </transition>

      <!-- Footer -->
      <router-view name="footer" />
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900');
  /* @import url('https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css'); */
  @import url('https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css');
  @import url('https://cdn.jsdelivr.net/npm/mdbvue/lib/css/mdb.min.css');
</style>
