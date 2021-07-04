<template>
  <b-card>
    <h2 class="h4 mb-4">{{ title }}</h2>
    <p>
      {{ content }}
    </p>
    <button class="btn btn-outline-primary text-center mt-5">
      {{ buttonTitle }}
    </button>
  </b-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: true 
    },
    buttonTitle: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
  .card {
    height: 400px;
    min-height: 400px;
  }
</style>
