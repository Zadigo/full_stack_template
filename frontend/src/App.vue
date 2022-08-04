<template>
  <router-view v-slot="{ Component }">
    <transition name="slide" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
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
</style>
