<template>
  <div>
    <div class="row">
      <div class="col-12">
        <div class="card mb-4">
          <div class="card-body">
            <h2>New product</h2>
            <hr class="my-3">
          </div>
        </div>
      </div>

      <div class="col-8">
        <div v-for="(fieldset, index) in fieldsets" :key="fieldset.id" :class="{ 'mt-2': index > 0 }" class="card">
          <div class="card-body">
            <p class="font-weight-bold">{{ fieldset.description }}</p>
            <div v-for="field in fieldset.fields" :key="field.id" class="form-group">

              <input v-model="currentChanges[field.name]" v-if="field.type=='text'" :type="field.type" :placeholder="field.placeholder" class="form-control">
              <input v-model.number="currentChanges[field.name]" v-else-if="field.type=='number'" :type="field.type" :placeholder="field.placeholder" class="form-control">
            </div>
          </div>
        </div>
      </div>

      <div class="col-4">
        <div class="card">          
          <div class="card-body">

          </div>
        </div>

        <div class="card mt-2">
          <div class="card-header">
            <p class="font-weight-bold m-0">Additional details</p>
          </div>       
          
          <div class="card-body">

          </div>
        </div>
      </div>
    </div>

    <div class="row mt-2 text-right">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <button @click="$router.go(-1)" class="btn btn-md btn-danger">
              Cancel
            </button>

            <button class="btn btn-md btn-secondary">
              Save draft
            </button>

            <button @click="saveCurrentChanges" class="btn btn-md btn-primary">
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var _ = require('lodash')

export default {
  name: 'Create',
  title () {
    return 'Create new - Dashboard'
  },
  data () {
    return {
      currentProduct: {},
      fieldsets: [
        { id: 1, description: 'Description', fields: [{ id: 1, name: 'name', type: 'text', placeholder: 'Name' }] },
        { id: 2, description: 'Another one', fields: [{ id: 1, name: 'age', type: 'number', placeholder: 'Age' }]}
      ],
      currentChanges: {}
    }
  },
  beforeMount () {
    _.forEach(this.fieldsets, (fieldset) => {
      _.forEach(fieldset.fields, (field) => {
        this.currentChanges[field.name] = null
      })
    })
  },
  methods: {
    saveCurrentChanges () {
      this.$store.commit('itemsModule/newItem', { id: 2 })
      this.$router.push({ name: 'tables' })
    }
  }
}
</script>
