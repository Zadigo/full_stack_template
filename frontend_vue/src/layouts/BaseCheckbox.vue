<template>
  <div class="form-check">
    <input :id="id" v-model="state" class="form-check-input" type="checkbox" @change="$emit('change', state)" />
    <label class="form-check-label" :for="id">{{ label }}</label>
  </div>
</template>

<script>
export default {
  name: 'BaseCheckbox',
  props: {
    id: {
      type: String,
      required: true
    },
    label: {
      type: String,
      required: true
    }
  },
  emits: {
    change: () => true
  },
  data () {
    return {
      state: false
    }
  }
}
</script>
