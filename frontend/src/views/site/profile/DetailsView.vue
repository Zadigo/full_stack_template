<template>
  <section>
    <base-validation-card :position="0" @validateAction="sendChanges">
      <template #cardHeader>
        <header class="card-header">
          <b-image :src="'https://images.pexels.com/photos/1447885/pexels-photo-1447885.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=100&w=100'" alt="avatar" ratio="1by1" :rounded="true"></b-image>
        </header>
      </template>

      <fields-iterator :form-fields="fields" @startAction="changeItems" />
    </base-validation-card>
  </section>
</template>

<script>
import _ from 'lodash'

import BaseValidationCard from '../../../components/auth/profile/BaseValidationCard.vue'
import FieldsIterator from '@/components/FieldsIterator.vue'

export default {
  name: 'DetailsSection',
  components: { FieldsIterator, BaseValidationCard },
  beforeRouteLeave(to, from, next) {
    if (Object.keys(this.changedValues).length > 0) {
      console.log('You have unfinished unsaved data')
    }
    next()
  },
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
  mounted () {
    // Prefills the form fields with their respective
    // values from the backend database
    var userDetails = this.$store.state.profileModule.userDetails.myuser
    _.forEach(this.fields, (field) => {
      field.value = userDetails[field.name]
    })
  },
  
  methods: {
    async sendChanges (position) {
      this.$api.profile.updateDetails(position, this.changedValues) 
      .then((response) => {
        this.changedValues = {}
        this.$store.dispatch('profileModule/updatePersonalDetails', response)
      })
      .catch((error) => {
        console.error(error)
      })
    }
  },
  changeItems (field, value) {
    this.changedValues[field] = value
  }  
}
</script>
