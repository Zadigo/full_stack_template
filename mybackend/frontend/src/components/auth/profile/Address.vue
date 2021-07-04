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

    <!-- Form -->
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

        <button @click="sendChanges" class="btn btn-primary btn-md m-0 mt-4">
          Validate
        </button>
      </b-card-body>
    </b-card>
    
    <!-- Cards -->
    <div v-else class="row">
      <div class="col-12">
        <b-card v-for="(address, index) in addresses" :key="address.id" :class="{ 'mt-2': index >= 1 }">
          <b-card-body>
            {{ address.street }}, {{ address.city }}

            <b-checkbox @change="mainAddress(address.id)" id="main-address" :checked="address.is_main">
              <span class="ml-2">Use as main address</span>
            </b-checkbox>
            
            <div class="row">
              <div class="col">
                <button @click="deleteAddress(address.id)" class="btn btn btn-light">
                  <i class="fa fa-trash mr-2"></i>
                </button>
              </div>
            </div>
          </b-card-body>
        </b-card>

        <b-card class="text-center mt-2">
          <button @click="addNew=true" class="btn btn-lg btn-primary">New address</button>
        </b-card>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Addresses',
  title () {
    return 'Addresses'
  },
  data () {
    return {
      addNew: false,
      newAddress: { is_main: false }
    }
  },
  computed: {
    addresses () {
      return this.$store.getters['authenticationModule/getUserAddresses']
    }
  },
  methods: {
    sendChanges () {
      this.$store.dispatch('authenticationModule/newAddress', this.newAddress)
      this.addNew = false
      this.newAddress = {}
    },
    deleteAddress (id) {
      this.$store.commit('authenticationModule/deleteAddress', id)
    },
    mainAddress (id) {
      this.$store.commit('authenticationModule/mainAddress', id)
    }
  }
}
</script>
