<template>
  <div class="row">
    <div class="col-12">
      <!-- Header -->
<<<<<<< HEAD:frontend/src/components/admin/Products.vue
      <PageHeader @doSearch="searchItems" homePageName="Dashboard" currentPageName="Products" />
      
      <div v-if="items.length > 0" class="card">
=======
      <PageHeader v-if="products.length > 0" home-page-name="Dashboard" current-page-name="Products" @doSearch="searchItems" />

      <div v-if="products.length > 0" class="card">
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09:frontend/src/views/admin/ProductsView.vue
        <div class="card-header">
          <v-menu transition="slide-y-transition">
            <template v-slot:activator="{ on, attrs }">
              <v-btn v-on="on" v-bind="attrs" color="primary">
                Actions
                <v-icon class="ml-2">mdi-chevron-down</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item-group>
                <v-list-item @click="action.func" v-for="(action, index) in actions" :key="index">
                  {{ action.name }}
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-menu>
        </div>

        <div class="card-body">
<<<<<<< HEAD:frontend/src/components/admin/Products.vue
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">
                    Name
                  </th>
                  <th class="text-left">
                    price
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in items" :key="index">
                  <td scope="row">
                    <router-link :to="{ name: 'admin_product', params: { id: item.id } }">
                      {{ item.name }}
                    </router-link>
                  </td>
                  <td>{{ item.price }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
          <!-- <v-data-table :headers="headers" :items="items" :items-per-page="10" class="elevation-1"></v-data-table> -->
=======
          <!-- Table -->
          <table class="table">
            <thead>
              <tr>
                <th>
                  <b-form-checkbox id="select-all"></b-form-checkbox>
                </th>
                <th>Name</th>
                <th>Price</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="product in searchedProducts" :key="product.id">
                <td>
                  <b-form-checkbox v-model="selected" :value="product.id"></b-form-checkbox>
                </td>
                <td scope="row">
                  <router-link :to="{ name: 'admin_product', params: { id: product.id } }">
                    {{ product.name }}
                  </router-link>
                </td>
                <td>{{ product.price }}</td>
              </tr>
            </tbody>
          </table>
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09:frontend/src/views/admin/ProductsView.vue
        </div>
      </div>

      <div v-else class="text-center">
        <div class="row">
          <div class="col-12">
            <img :src="require('@/assets/no_data.svg')" class="img-fluid" alt="no-products" height="200" width="auto" role="img">
          </div>
        </div>
        
        <router-link :to="{ name: 'admin_product_create' }" class="btn btn-lg btn-primary mt-4" role="link">
          Create new
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD:frontend/src/components/admin/Products.vue
var _ = require('lodash')
import { mapState } from 'vuex'
=======
import _ from 'lodash'
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09:frontend/src/views/admin/ProductsView.vue

import PageHeader from '@/components/admin/nav/PageHeader.vue'

export default {
  name: 'ProductsSection',
  title () {
    return 'Products - Dashboard'
  },
  components: {
    PageHeader
  },
  data () {
    return {
      selected: [],
      searchedItem: null,
      headers: [
        {
          text: 'name',
          value: 'name'
        },
        {
          text: 'price',
          value: 'price'
        }
      ],
      actions: [
        { name: 'Activate', func: () => { alert('something') }},
        { name: 'Deactivate', func: () => { alert('something') }},
        { name: 'Duplicate', func: () => { alert('something') }},
        { name: 'Delete', func: () => { alert('something') }}
      ]
    }
  },
<<<<<<< HEAD:frontend/src/components/admin/Products.vue

  components: {
    PageHeader
  },
  
=======
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09:frontend/src/views/admin/ProductsView.vue
  computed: {
    searchedProducts () {
      if (this.searchedItem) {
        return this.products
      } else {
        return _.filter(this.products, (product) => {
          return product.name.includes(this.searchedItem)
        })
      }
    },
    
    ...mapState('shopModule', ['items']),

    numberOfSelections () {
      return this.selected.length
    }
  },
  methods: {
    searchItems (term) {
      this.searchedItem = term
    }
  }
}
</script>
