<template>
  <section id="addresses">
    <!-- Update/Creation form -->
    <div v-if="addresses.length===0 && !addNew" class="card">
      <div class="card-body text-center">
        <h2 class="mb-4">You have no addresses</h2>
        <img :src="require('@/assets/hello.svg')" alt="addresses" class="img-fluid">
        <button type="button" class="btn btn-primary btn-lg m-0 mt-4" @click="addNew=true">
          Add new
        </button>
      </div>
    </div>

    <base-validation-card-vue v-else-if="addNew">
      <input id="street-address" v-model="newAddress.street_address" type="text" class="form-control p-3" placeholder="1 rue de Rivoli" autocomplete="address-line1">
      
      <div class="d-flex justify-content-between my-2">
        <input id="address2" v-model="newAddress.city" type="text" class="form-control p-3 me-2" placeholder="City" autocomplete="address-level2">
        <input id="postal-code" v-model="newAddress.zip_code" type="text" class="form-control p-3" placeholder="75001" autocomplete="postal-code">
      </div>
      
      <input id="country" v-model="newAddress.country" type="text" class="form-control w-50 p-3" placeholder="France" autocomplete="country-name">

      <template #cardFooter>
        <div class="card-footer">
          <button v-if="createMode" type="button" class="btn btn-primary btn-md" @click="sendChanges">
            <font-awesome-icon icon="fa-solid fa-check" class="me-2" />
            Validate
          </button>

          <button v-else type="button" class="btn btn-primary btn-md" @click="updateAddress">
            <font-awesome-icon icon="fa-solid fa-check" class="me-2" />
            Update
          </button>

          <button type="button" class="btn btn-outline-primary btn-md mx-2" @click="addNew=false">
            <!-- <font-awesome-icon icon="fa-solid fa-check" class="me-2" /> -->
            Cancel
          </button>
        </div>
      </template>
    </base-validation-card-vue>

    <!-- Cards -->
    <div v-else class="row">
      <div class="col-12">
        <base-card v-for="(address, index) in addresses" :key="address.id" :class="{ 'mt-2': index >= 1 }">
          <b-card-body>
            {{ address.street_address }}, {{ address.zip_code }}

            <b-checkbox :id="`address_${address.id}`" :checked="address.is_main" @change="mainAddress(address.id)">
              <span class="ml-2">Use as main address</span>
            </b-checkbox>
          </b-card-body>

          <template v-slot:cardFooter>
            <footer class="card-footer">
              <button type="button" class="card-footer-item" @click="deleteAddress(address.id)">
                <font-awesome-icon icon="trash"></font-awesome-icon>
              </button>

              <button type="button" class="card-footer-item" @click="retrieveAddressToUpdate(address.id)">
                <font-awesome-icon icon="pen"></font-awesome-icon>
              </button>
            </footer>
          </template>
        </base-card>

        <!-- Creation -->
        <base-card class="text-center mt-2">
          <button type="button" class="btn btn-lg btn-primary" @click="addNew=true">
            Create new
          </button>
        </base-card>
      </div>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'

import BaseValidationCardVue from '@/layouts/BaseValidationCard.vue'

import { useAuthentication } from '@/store/authentication'

export default {
  name: 'AddressesSection',
  components: {
    BaseValidationCardVue
  },
  setup () {
    const store = useAuthentication()
    const addresses = store.user.addresses || []
    return {
      addresses
    }
  },
  title () {
    return 'Addresses'
  },
  data () {
    return {
      addNew: false,
      newAddress: { is_main: false },
      createMode: true
    }
  },
  methods: {
    async sendChanges () {
      this.addNew = false
      this.$api.profile.createAddress(this.newAddress)
      .then((response) => {
        this.$store.dispatch('profileModule/newAddress', response)
      })
      .catch((error) => {
        console.log(error)
      })
      this.newAddress = {}
    },
    async deleteAddress (id) {
      // Allows the user to delete an address
      // from the backend
      this.$api.profile.removeAddress({ id: id })
      .then(() => {
        this.$store.dispatch('profileModule/deleteAddress', id)
      })
      .catch((error) => {
        console.error(error)
      })
    },
    async updateAddress() {
      // Finalizes the updating of the address
      // by sending the request to the server
      // this.$store.dispatch('profileModule/updateAddress', this.newAddress)
      // this.$api.profile.modifyAddress(this.newAddress)
      // .then((response) => {
      //   this.$store.dispatch('profileModule/updateAddress', response)
      //   this.createMode = true
      //   this.addNew = false
      // })
      // .catch((error) => {
      //   console.log(error)
      // })
    },
    retrieveAddressToUpdate(id) {
      // Initiates the updating of the address by
      // prefilling the update fields with the the
      // address details
      var address = this.$store.getters['profileModule/getAddress'](id)
      _.forEach(Object.keys(address), (key) => {
        this.newAddress[key] = address[key]
      })
      this.createMode = false
      this.addNew = true
    },
    mainAddress(id) {
      this.$store.commit('profileModule/chooseMainAddress', id)
    }
  }
}
</script>
