<template>
  <div class="py-5 shadow-sm text-center">
    <h1 class="display-5 fw-bold">
      {{ catchPhrase }}
    </h1>

    <div class="col-lg-6 mx-auto">
      <p v-if="lead" class="lead mb-4">{{ lead }}</p>

      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseIntro',
  props: {
    catchPhrase: {
      type: String,
      default: null
    },
    lead: {
      type: String,
      default: null
    }
  }
}
</script>
