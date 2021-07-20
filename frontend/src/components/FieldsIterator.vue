<template>
  <div class="row">
    <div class="col-12">
      <div v-for="field in fields" :key="field.id" class="form-group mt-2">
        <label v-if="field.label !== null" :for="field.name" class="mt-3 mb-2 font-weight-bold">
          {{ field.label }}
        </label>
        <input @keyup="$emit('startAction', field.name, $event.target.value)" :type="field.type|defaulType" :value="field.value" :id="field.name" :autocomplete='field.autocomplete' :placeholder="field.placeholder" :aria-label="field.aria" class="form-control">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FieldsIterator',
  props: {
    fields: {
      type: Array,
      required: true
    }
  },
  
  filters: {
    defaulType (value) {
      if (value === null | value === undefined) {
        return 'text'
      } else {
        return value
      }
    }
  }
}
</script>
