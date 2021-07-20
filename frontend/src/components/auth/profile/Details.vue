<template>
  <validation-card @validateAction="sendChanges" :position="0">
    <fields-iterator @startAction="changeItems" :fields="fields" />
  </validation-card>
</template>

<script>
var _ = require('lodash')

import ValidationCard from './ValidationCard.vue'
import FieldsIterator from "../../FieldsIterator.vue"

export default {
  name: 'ProfileIndex',
  components: { FieldsIterator, ValidationCard },

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

  beforeRouteLeave(to, from, next) {
    if (Object.keys(this.changedValues).length > 0) {
      console.log('You have unfinished unsaved data')
    }
    next()
  },
  
  mounted () {
    var userDetails = this.$store.state.profileModule.userDetails
    _.forEach(this.fields, (field) => {
      if (field.prefilled) {
        // field['value'] = userDetails[field['name']]
        // this.changedValues[field.name] = userDetails[field.name]
        field['value'] = userDetails[field.name]
      }
    })
  },
  
  methods: {
    changeItems (field, value) {
      this.changedValues[field] = value
    },
    
    sendChanges (position) {
      this.$store.dispatch(
      'profileModule/updatePersonalDetails', 
        { position: position, content: this.changedValues }
      )
      
      this.changedValues = {}
      this.$buefy.snackbar.open({
        message: 'Données mis à jour',
        type: 'is-warning',
        position: 'is-top-right',
        actionText: 'Cancel',
        indefinite: false,
        duration: 3500,
        onAction: () => {
          // this.$buefy.toast.open({
          //   message: 'Action pressed',
          //   queue: false
          // })
          console.log('This message')
        } 
      })
    }
  }
}
</script>
