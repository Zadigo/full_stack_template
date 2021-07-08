<template>
  <div class="row">
    <div class="col-12">
      <!-- Header -->
      <PageHeader @doSearch="searchItems" v-if="products.length > 0" homePageName="Dashboard" currentPageName="Products" />
      
      <div v-if="products.length > 0" class="card">
        <div class="card-header">
          <!-- Actions -->
          <!-- <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Actions
              <span class="badge badge-pill">{{ numberOfSelections }}</span>
            </button>

            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </div> -->
          <b-dropdown id="table-actions" text="Actions">
            <b-dropdown-item>Activate</b-dropdown-item>
            <b-dropdown-item>Deactivate</b-dropdown-item>
            <b-dropdown-item>Duplicate</b-dropdown-item>
            <!-- <b-dropdown-item active>Active action</b-dropdown-item> -->
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item>Delete</b-dropdown-item>
          </b-dropdown>
        </div>

        <div class="card-body">
          <!-- Table -->
          <table class="table">
            <thead>
              <tr>
                <th><b-form-checkbox id="select-all"></b-form-checkbox></th>
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
                <td>{{ product.price|currency }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div v-else class="text-center">
        <div id="image">
          <img src="../../assets/no_data.svg" alt="no-products" height="300" width="auto" role="img">
        </div>
        <router-link :to="{ name: 'admin_product_create' }" class="btn btn-lg btn-primary mt-4" role="link">
          Create new
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
var _ = require('lodash')

import PageHeader from './nav/PageHeader.vue'

export default {
  name: 'Products',
  title () {
    return 'Products - Dashboard'
  },
  data () {
    return {
      selected: [],
      searchedItem: null
    }
  },
  components: {
    PageHeader
  },
  computed: {
    searchedProducts () {
      if (this.searchedItem === null | this.searchedItem === '') {
        return this.products
      } else {
        return _.filter(this.products, (product) => {
          return product.name.includes(this.searchedItem)
        })
      }
    },
    products () {
      return this.$store.getters['itemsModule/getItems']
    },
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
