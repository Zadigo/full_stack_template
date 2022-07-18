<template>
  <router-view />
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
</style>
