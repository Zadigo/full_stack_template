<template>
  <div style="margin-top: 4rem;" id="product">
    <div class="row">
      <div class="col-12">
        <v-card>
          <v-card-text>
            <h1>{{ currentProduct.name }}</h1>

            <hr>

            <v-btn :to="{ name: 'admin_product', params: { id: getPrevious() } }" icon><v-icon>mdi-arrow-left</v-icon></v-btn>
            <v-btn :to="{ name: 'admin_product', params: { id: getNext() } }" icon><v-icon>mdi-arrow-right</v-icon></v-btn>
          </v-card-text>
        </v-card>
      </div>

      <div class="col-8">
        <div v-for="(fieldset, index) in fieldsets" :key="fieldset.id" :class="{ 'mt-2': index > 0 }" class="card">
          <div class="card-body">

            <p class="font-weight-bold">{{ fieldset.description }}</p>

            <div v-for="field in fieldset.fields" :key="field.id" class="form-group">
              <v-text-field v-model="currentChanges[field.name]" :type="field.type" :placeholder="field.placeholder"></v-text-field>

              <!-- <input v-model="currentChanges[field.name]" v-if="field.type=='text'" :type="field.type" :placeholder="field.placeholder" class="form-control"> -->
              <!-- <input v-model.number="currentChanges[field.name]" v-else-if="field.type=='number'" :type="field.type" :placeholder="field.placeholder" class="form-control"> -->
            </div>
          
          </div>
        </div>
      </div>

      <div class="col-4"></div>
    </div>

    <div class="row mt-2">
      <div class="col-12">
        <div class="card">
          <div class="card-body text-right">
            <button @click="$router.go(-1)" class="btn btn-lg btn-danger">
              Cancel
            </button>

            <button @click="saveCurrentChanges" class="btn btn-lg btn-primary">
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD:frontend/src/components/admin/Product.vue
var _ = require('lodash')
import fieldsets from './fieldsets.json'
=======
import _ from 'lodash'
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09:frontend/src/views/admin/ProductView.vue

export default {
  name: 'ProductView',
  beforeRouterEnter(to, from, next) {
    var currentProduct = this.$store.getters['itemsModule/getItem'](this.$route.params.id)
    if (!currentProduct) {
      next('login')
    } else {
      next(vm => {
        vm.setData('currentProduct', currentProduct)
      })
    }
  },
  beforeRouteUpdate(to, from, next) {
    var currentProduct = this.$store.getters['itemsModule/getItem'](this.$route.params.id)
    this.setData('currentProduct', currentProduct)
    next()
  },
  data() {
    return {
      currentProduct: {},
      // fieldsets: [
      //   { id: 1, description: 'Description', fields: [{ id: 1, name: 'name', type: 'text', placeholder: 'Name' }] },
      //   { id: 2, description: 'Another one', fields: [{ id: 1, name: 'age', type: 'number', placeholder: 'Age' }]}
      // ],
      fieldsets: fieldsets,
      currentChanges: {}
    }
  },
<<<<<<< HEAD:frontend/src/components/admin/Product.vue

  beforeRouteEnter (to, from, next) {
    next(vm => {
      vm.currentProduct = vm.$store.getters['shopModule/getProduct'](to.params.id)
    })
  },
  
  beforeRouteUpdate(to, from, next) {
    var currentProduct = this.$store.getters['itemsModule/getItem'](this.$route.params.id)
    this.setData('currentProduct', currentProduct)
    next()
  },
  
  mounted() {
=======
  beforeMount() {
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09:frontend/src/views/admin/ProductView.vue
    _.forEach(this.fieldsets, (fieldset) => {
      _.forEach(fieldset.fields, (field) => {
        this.currentChanges[field.name] = this.currentProduct[field.name]
      })
    })
  },

  methods: {
    saveCurrentChanges () {
      this.$store.commit('itemsModule/newItem', { id: 2 })
      this.$router.push({ name: 'tables' })
    },

    getNext () {
      return this.$store
    },

    getPrevious () {
      return 
    }
  }
}
</script>
