<template>
  <section id="details">
    <b-card v-for="fieldset in fieldsets" :key="fieldset.position">
      <fields-iterator :fields="fieldset.fields" />
    </b-card>
  </section>
</template>

<script>
import FieldsIterator from './FieldsIterator.vue'

export default {
  props: {
    fieldsets: {
      type: Array,
      required: true
    }
  },
  components: {
    'fields-iterator': FieldsIterator
  }
}
</script>
