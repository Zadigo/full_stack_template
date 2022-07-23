<template>
  <div class="row">
    <div class="col-12">
      <div v-for="field in formFields" :key="field.id" class="form-group mt-2">
        <label v-if="field.label !== null" :for="field.name" class="mt-3 mb-2 fw-bold">
          {{ field.label }}
        </label>
        <input :type="field.type" :value="field.value" :autocomplete="field.autocomplete" :aria-label="field.aria" class="form-control p-3" @keyup="$emit('start-action', [field.name, $event.target.value])">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FieldsIterator',
  props: {
    formFields: {
      type: Array,
      required: true
    }
  },
  emits: {
    'start-action': (value) => {
      console.log(value)
      return true
    }
  }
}
</script>
