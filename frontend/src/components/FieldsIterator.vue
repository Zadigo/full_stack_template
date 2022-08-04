<template>
  <div class="row">
    <div class="col-12">
      <div v-for="field in formFields" :key="field.id" class="form-group mt-2">
        <label v-if="field.label !== null" :for="field.name" class="mt-3 mb-2 fw-bold">
          {{ field.label }}
        </label>
        <!-- @keyup="$emit('start-action', [field.name, $event.target.value])" -->
        <input v-model="fieldUpdates[field.name]" :type="field.type" :autocomplete="field.autocomplete" :aria-label="field.aria" class="form-control p-3" @keyup="$emit('start-action', fieldUpdates)">
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
    },
    initialValues: {
      type: Object,
      default: () => {}
    }
  },
  emits: {
    'start-action': () => true
  },
  data () {
    return {
      fieldUpdates: {}
    }
  },
  created () {
    this.fieldUpdates = Object.assign(this.initialValues, this.fieldUpdates)
  }
}
</script>
