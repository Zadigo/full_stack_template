<doc>
  Allows the user to change certain details on their profile
</doc>

<template>
  <section>
    <base-validation-card :position="0" @validateAction="sendChanges">
      <template #cardHeader>
        <header class="card-header">
          <img :src="'https://images.pexels.com/photos/1447885/pexels-photo-1447885.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=100&w=100'" alt="avatar">
        </header>
      </template>

      <fields-iterator :form-fields="getFields('details')" @start-action="changeItems" />
    </base-validation-card>
  </section>
</template>

<script>
// import _ from 'lodash'

import BaseValidationCard from '@/layouts/BaseValidationCard.vue'
import FieldsIterator from '@/components/FieldsIterator.vue'
import useProfileComposable from '@/composables/profile'

export default {
  name: 'DetailsView',
  components: {
    FieldsIterator,
    BaseValidationCard
  },
  setup () {
    const { getFields } = useProfileComposable()
    return {
      getFields
    }
  },
  // beforeRouteLeave(to, from, next) {
  //   if (Object.keys(this.changedValues).length > 0) {
  //     console.log('You have unfinished unsaved data')
  //   }
  //   next()
  // },
  data () {
    return {
      updatedFields: {}
    }
  },
  mounted () {
    // Prefills the form fields with their respective
    // values from the backend database
    // var userDetails = this.$store.state.profileModule.userDetails.myuser
    // _.forEach(this.fields, (field) => {
    //   field.value = userDetails[field.name]
    // })
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
    },
    changeItems (data) {
      this.updatedFields[data[0]] = data[1]
    }  
  }
}
</script>
