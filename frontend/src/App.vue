<template>
  <router-view v-slot="{ Component }">
    <transition name="slide" mode="in-out">
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
  transition: all .3s ease;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: scale(1, 1);
}

.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: scale(.9, .9);
}
</style>
