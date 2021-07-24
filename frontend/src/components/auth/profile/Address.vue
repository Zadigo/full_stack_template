<template>
  <section id="addresses">
    <!-- Add new -->
    <base-card v-if="addresses.length===0 && !addNew">
      <b-card-body class="text-center">
        <h2 class="mb-4">You have no addresses</h2>
        <img src="../../../assets/hello.svg" alt="addresses" class="img-fluid">
        <button @click="addNew=true" class="btn btn-primary btn-lg m-0 mt-4">Add new</button>
      </b-card-body>
    </base-card>

    <!-- Update/Creation form -->
    <base-card v-else-if="addNew">
      <div class="form-group">
        <input v-model="newAddress['street_address']" type="text" class="form-control" id="street-address" placeholder="1 rue de Rivoli" autocomplete="address-line1">
      </div>

      <div class="form-group mt-2">
        <input v-model="newAddress['city']" type="text" class="form-control" id="address2" placeholder="City" autocomplete="address-level2">
      </div>

      <div class="form-group mt-2">
        <input v-model="newAddress['zip_code']" type="text" class="form-control" id="postal-code" placeholder="75001" autocomplete="postal-code">
      </div>

      <div class="form-group mt-2">
        <input v-model="newAddress['country']" type="text" class="form-control" id="country" placeholder="France" autocomplete="country-name">
      </div>

      <template v-slot:cardFooter>
        <button @click="sendChanges" v-if="createMode" class="btn btn-primary btn-md">
          <font-awesome-icon icon="check"></font-awesome-icon>
          Validate
        </button>

        <button @click="updateAddress" v-else class="btn btn-primary btn-md">
          <font-awesome-icon icon="check"></font-awesome-icon>
          Update
        </button>

        <button @click="$router.go(-1)" class="btn btn-outline-primary btn-md">
          <font-awesome-icon icon="check"></font-awesome-icon>
          Cancel
        </button>
      </template>
    </base-card>
    
    <!-- Cards -->
    <div v-else class="row">
      <div class="col-12">
        <base-card v-for="(address, index) in addresses" :key="address.id" :class="{ 'mt-2': index >= 1 }">
          <b-card-body>
            {{ address.street_address }}, {{ address.zip_code }}

            <b-checkbox @change="mainAddress(address.id)" :id="`address_${address.id}`" :checked="address.is_main">
              <span class="ml-2">Use as main address</span>
            </b-checkbox>
          </b-card-body>

          <template v-slot:cardFooter>
            <footer class="card-footer">
              <button @click="deleteAddress(address.id)" class="card-footer-item">
                <font-awesome-icon icon="trash"></font-awesome-icon>
              </button>

              <button @click="retrieveAddressToUpdate(address.id)" class="card-footer-item">
                <font-awesome-icon icon="pen"></font-awesome-icon>
              </button>
            </footer>
          </template>
        </base-card>

        <!-- Creation -->
        <base-card class="text-center mt-2">
          <button @click="addNew=true" class="btn btn-lg btn-primary">
            Create new
          </button>
        </base-card>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState } from 'vuex'

var _ = require('lodash')

export default {
  name: 'Addresses',
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
  
  computed: {
    ...mapState('profileModule', {
      addresses: (state) => { return state.userDetails.addresses }
    })
  },
  
  methods: {
    sendChanges () {
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

    deleteAddress (id) {
      this.$api.profile.removeAddress({ id: id })
      .then((response) => {
        response
        this.$store.dispatch('profileModule/deleteAddress', id)
      })
      .catch((error) => {
        console.error(error)
      })
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

    updateAddress() {
      // Finalizes the updating of the address
      // by sending the request to the server
      // this.$store.dispatch('profileModule/updateAddress', this.newAddress)
      this.$api.profile.modifyAddress(this.newAddress)
      .then((response) => {
        this.$store.dispatch('profileModule/updateAddress', response)
        this.createMode = true
        this.addNew = false
      })
      .catch((error) => {
        console.log(error)
      })
    },

    mainAddress(id) {
      this.$store.commit('profileModule/chooseMainAddress', id)
    }
  }
}
</script>
