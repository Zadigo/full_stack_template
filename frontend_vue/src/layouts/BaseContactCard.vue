<template>
  <div class="card h-100">
    <div class="card-body">
      <h4 class="card-title mb-4">{{ title }}</h4>

      <p class="card-text fw-light">
        {{ content }}
      </p>
    </div>

    <div class="card-footer border-0 text-center p-3">
      <button type="button" class="btn btn-outline-primary text-center">
        {{ buttonTitle }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseCard',
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
