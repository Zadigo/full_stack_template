<template>
  <profile-card @validateAction="sendChanges" :position="0">
      <fields-iterator @startAction="changeItems" :fields="fields" />
  </profile-card>
</template>

<script>
var _ = require('lodash')

import ProfileCard from './ProfileCard.vue'
import FieldsIterator from "../../FieldsIterator.vue"

export default {
  name: 'ProfileIndex',
  components: { FieldsIterator, 'profile-card': ProfileCard },
  data () {
    return {
      changedValues: {},
      fields: [
        { id: 1, type: 'text', name: 'firstname', placeholder: 'Firstname', autocomplete: 'given-name', value: null, prefilled: true },
        { id: 2, type: 'text', name: 'lastname', placeholder: 'Lastname', autocomplete: 'family-name', value: null, prefilled: true },
        { id: 3, type: 'email', name: 'email', placeholder: 'Email', autocomplete: 'email', value: null, prefilled: true },
      ]
    }
  },
  mounted () {
    var userDetails = this.$store.getters['authenticationModule/getUserDetails']
    _.forEach(this.fields, (field) => {
      if (field.prefilled) {
        field['value'] = userDetails[field['name']]
      }
    })
  },
  methods: {
    changeItems (field, value) {
      this.changedValues[field] = value
    },
    sendChanges (position) {
      console.log(position)
      this.$store.commit('authenticationModule/updateUserDetails', this.changedValues)
    }
  }
}
</script>
