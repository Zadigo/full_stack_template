<template>
  <section class="section" id="addresses">
    <!-- Add new -->
    <b-card v-if="addresses.length===0 && !addNew">
      <b-card-body class="text-center">
        <h2 class="mb-4">You have no addresses</h2>
        <img src="../../../assets/hello.svg" alt="addresses" class="img-fluid">
        <button @click="addNew=true" class="btn btn-primary btn-lg m-0 mt-4">Add new</button>
      </b-card-body>
    </b-card>

    <!-- Update/Creation form -->
    <b-card v-else-if="addNew">
      <b-card-body>
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

        <button @click="sendChanges" v-if="createMode" class="btn btn-primary btn-md m-0 mt-4">
          <i class="fa fa-check mr-3"></i>
          Validate
        </button>
        <button @click="updateAddress" v-else class="btn btn-primary btn-md m-0 mt-4">
          <i class="fa fa-check mr-3"></i>
          Update
        </button>
      </b-card-body>
    </b-card>
    
    <!-- Cards -->
    <div v-else class="row">
      <div class="col-12">
        <b-card v-for="(address, index) in addresses" :key="address.id" :class="{ 'mt-2': index >= 1 }">
          <b-card-body>
            {{ address.street_address }}, {{ address.zip_code }}

            <b-checkbox @change="mainAddress(address.id)" :id="`address_${address.id}`" :checked="address.is_main">
              <span class="ml-2">Use as main address</span>
            </b-checkbox>
            
            <div class="row">
              <div class="col">
                <button @click="deleteAddress(address.id)" class="btn btn btn-light">
                  <i class="fa fa-trash mr-2"></i>
                </button>

                <button @click="startUpdateAddress(address.id)" class="btn btn btn-light">
                  <i class="fa fa-create mr-2"></i>
                </button>
              </div>
            </div>
          </b-card-body>
        </b-card>

        <!-- Creation -->
        <b-card class="text-center mt-2">
          <button @click="addNew=true" class="btn btn-lg btn-primary">Create new</button>
        </b-card>
      </div>
    </div>
  </section>
</template>

<script>
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
    addresses() {
      return this.$store.state.profileModule.userDetails.addresses
    }
  },
  
  methods: {
    sendChanges () {
      this.addNew = false
      this.$store.dispatch('profileModule/newAddress', this.newAddress)
      this.newAddress = {}
    },

    deleteAddress (id) {
      this.$store.commit('profileModule/deleteAddress', id)
    },

    startUpdateAddress(id) {
      // Initiates the updating of the address by
      // showing the update fields with the the
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
      this.$store.dispatch('profileModule/updateAddress', this.newAddress)
      this.createMode = true
      this.addNew = false
    }
  }
}
</script>
