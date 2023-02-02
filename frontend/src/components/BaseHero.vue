<template>
  <div id="hero">
    <header>
      <slot name="navigation"></slot>
      
      <div ref="intro" :class="{ 'fullpage': !fullPage }" class="bg-image shadow-2-strong" id="intro">
        <div class="mask">
          <div class="container h-100 d-flex align-items-center justify-content-center text-center">
            <slot name="lead"></slot>
          </div>
        </div>
      </div>
    </header>

    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'BaseHero',
  props: {
    image: String,
    fullPage: Boolean,
    navbarDark: Boolean
  },

  mounted () {
    this.$refs.intro.style.backgroundImage = `url(${this.image})`
  }
}
</script>

<style scoped>
  #intro {
    height: 100vh;
  }

  /* Height for devices larger than 576px */
  @media (min-width: 992px) {
    .fullpage {
      /* margin-top: -58.59px; */
      margin-top: -70px;
    }
  }
</style>
