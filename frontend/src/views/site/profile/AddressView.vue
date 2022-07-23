<template>
  <section id="addresses">
    <!-- Add new -->
    <base-card v-if="addresses.length===0 && !addNew">
      <b-card-body class="text-center">
        <h2 class="mb-4">You have no addresses</h2>
        <img src="../../../assets/hello.svg" alt="addresses" class="img-fluid">
        <button type="button" class="btn btn-primary btn-lg m-0 mt-4" @click="addNew=true">Add new</button>
      </b-card-body>
    </base-card>

    <!-- Update/Creation form -->
    <base-card v-else-if="addNew">
      <div class="form-group">
        <input id="street-address" v-model="newAddress['street_address']" type="text" class="form-control" placeholder="1 rue de Rivoli" autocomplete="address-line1">
      </div>

      <div class="form-group mt-2">
        <input id="address2" v-model="newAddress['city']" type="text" class="form-control" placeholder="City" autocomplete="address-level2">
      </div>

      <div class="form-group mt-2">
        <input id="postal-code" v-model="newAddress['zip_code']" type="text" class="form-control" placeholder="75001" autocomplete="postal-code">
      </div>

      <div class="form-group mt-2">
        <input id="country" v-model="newAddress['country']" type="text" class="form-control" placeholder="France" autocomplete="country-name">
      </div>

      <template v-slot:cardFooter>
        <button v-if="createMode" type="button" class="btn btn-primary btn-md" @click="sendChanges">
          <font-awesome-icon icon="check"></font-awesome-icon>
          Validate
        </button>

        <button v-else type="button" class="btn btn-primary btn-md" @click="updateAddress">
          <font-awesome-icon icon="check"></font-awesome-icon>
          Update
        </button>

        <button type="button" class="btn btn-outline-primary btn-md" @click="$router.go(-1)">
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

// import { useAuthentication } from '@/store/authentication'
// import { mapState } from 'pinia'

export default {
  name: 'AddressesSection',
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
    // ...mapState(useAuthentication, {
    //   addresses: (state) => {
    //     return state.userDetails.addresses
    //   }
    // })
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
