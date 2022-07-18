<template>
  <div id="hero">
    <header>
      <div ref="intro" class="bg-image shadow-2-strong" id="intro">
        <div class="mask d-flex align-items-center">
          <div class="container h-100">
            <router-view />
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'RegistrationHero',

  mounted () {
    this.$refs.intro.style.backgroundImage = "url(https://images.unsplash.com/photo-1512850071827-9242a6124c50?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80)"
  }
}
</script>

<style scoped>
  #intro {
    height: 100vh;
  }
</style>
