<template>
  <div class="row">
    <div class="col-12">
      <div v-for="field in fields" :key="field.id" class="form-group mt-2">
        <label v-if="field.label" :for="field.name" class="mt-3 mb-2">{{ field.label_text }}</label>
        <input @change="$emit('startAction', field.name, $event.target.value)" :type="field.type|defaulType" :value="field.value" :id="field.name" :autocomplete='field.autocomplete' :placeholder="field.placeholder" :aria-label="field.aria" class="form-control">
      </div>
    </div>
  </div>
</template>

<script>
export default {
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
