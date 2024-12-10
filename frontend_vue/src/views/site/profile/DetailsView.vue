<doc>
  Allows the user to change certain details on their profile
</doc>

<template>
  <section>
    <base-validation-card :position="0" @validateAction="update">
      <template #cardHeader>
        <header class="card-header">
          <img :src="'https://images.pexels.com/photos/1447885/pexels-photo-1447885.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=100&w=100'" alt="avatar">
        </header>
      </template>

      <fields-iterator :form-fields="fields" :initial-values="initialValues" @start-action="changeItems" />
    </base-validation-card>
  </section>
</template>

<script>
import BaseValidationCard from '@/layouts/BaseValidationCard.vue'
import FieldsIterator from '@/components/FieldsIterator.vue'
import useProfileComposable from '@/composables/profile'
import { useAuthentication } from '@/store/authentication'
import { storeToRefs } from 'pinia'

export default {
  name: 'DetailsView',
  components: {
    FieldsIterator,
    BaseValidationCard
  },
  setup () {
    const store = useAuthentication()
    const { user } = storeToRefs(store)
    const { getFields, getInitialValues } = useProfileComposable()
    const fields = getFields('details')
    const initialValues = getInitialValues('details', store.user.myuser)
    return {
      initialValues,
      fields,
      user,
      getInitialValues,
      getFields
    }
  },
  data () {
    return {
      updatedFields: {}
    }
  },
  methods: {
    async update () {
      try {
        await this.$http.post('accounts/profile/update', { method: 'details', myuser: this.updatedFields })
      } catch(error) {
        console.error(error)
      }
    },
    changeItems (data) {
      this.updatedFields = data
    }
  }
}
</script>
