<template>
<<<<<<< HEAD
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
=======
  <router-view v-slot="{ Component }">
    <transition name="slide" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
</template>

<script>
export default {
  name: 'App'
  // mounted () {
  //   this.$session.create('something', 1)
  // }
}
</script>

<style>
<<<<<<< HEAD
  @import url('https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900');
  /* @import url('https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css'); */
  @import url('https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css');
  @import url('https://cdn.jsdelivr.net/npm/mdbvue/lib/css/mdb.min.css');
=======
@import url('./assets/style.css');

* {
  font-family: 'Ubuntu', 'Roboto', sans-serif;
}

.slide-enter-active,
.slide-leave-active {
  transition: all .3s ease-in-out;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translate(-10px);
}

.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translate(0px);
}
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
</style>
