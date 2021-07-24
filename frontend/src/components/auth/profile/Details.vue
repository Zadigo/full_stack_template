<template>
  <section>
    <base-validation-card @validateAction="sendChanges" :position="0">
      <template v-slot:cardHeader>
        <header class="card-header">
          <b-image :src="'https://images.pexels.com/photos/1447885/pexels-photo-1447885.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=100&w=100'" alt="avatar" ratio="1by1" :rounded="true"></b-image>
        </header>
      </template>

      <fields-iterator @startAction="changeItems" :formFields="fields" />
    </base-validation-card>
  </section>
</template>

<script>
var _ = require('lodash')

import BaseValidationCard from './BaseValidationCard.vue'
import FieldsIterator from "../../FieldsIterator.vue"

export default {
  name: 'ProfileIndex',
  components: { FieldsIterator, BaseValidationCard },

  data () {
    return {
      changedValues: {},
      fields: [
        { id: 1, type: 'text', name: 'firstname', placeholder: 'Firstname', label: 'Firstname', autocomplete: 'given-name', value: null, prefilled: true },
        { id: 2, type: 'text', name: 'lastname', placeholder: 'Lastname', label: 'Lastname', autocomplete: 'family-name', value: null, prefilled: true },
        { id: 3, type: 'email', name: 'email', placeholder: 'Email', label: 'Email', autocomplete: 'email', value: null, prefilled: true },
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
    // Prefills the form fields with their respective
    // values from the backend database
    var userDetails = this.$store.state.profileModule.userDetails.myuser
    _.forEach(this.fields, (field) => {
      field['value'] = userDetails[field.name]
    })
  },
  
  methods: {
    changeItems (field, value) {
      this.changedValues[field] = value
    },
    
    sendChanges (position) {
      this.$api.profile.updateDetails(position, this.changedValues) 
      .then((response) => {
        this.changedValues = {}
        // this.$buefy.snackbar.open({
        //     message: 'Yellow button and positioned on top, click to close',
        //     type: 'is-warning',
        //     position: 'is-top',
        //     actionText: 'Cancel',
        //     indefinite: true,
        //     onAction: () => {
        //         this.$buefy.toast.open({
        //             message: 'Action pressed',
        //             queue: false
        //         })
        //     }
        // })
        this.$store.dispatch('profileModule/updatePersonalDetails', response)
      })
      .catch((error) => {
        console.error(error)
      })
    }
  }
}
</script>
