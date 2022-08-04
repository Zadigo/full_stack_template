<template>
  <div class="card">
    <slot name="cardHeader"></slot>

    <div class="card-body">
      <slot></slot>
    </div>

    <slot name="cardFooter">
      <footer class="card-footer bg-white text-right">
        <button type="button" class="btn btn-primary mr-2" aria-label="Validate" @click="$emit('validate-action', position)">
          <font-awesome-icon icon="fa-solid fa-check" />
          {{ buttonName }}
        </button>
      </footer>
    </slot>
  </div>
</template>

<script>
export default {
  name: 'BaseValidationCard',
  props: {
    position: {
      type: Number,
      default: 0
    },
    buttonName: {
      type: String,
      default: 'Validate'
    }
  },
  emits: {
    'validate-action': () => true
  }
}
</script>
