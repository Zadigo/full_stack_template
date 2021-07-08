<template>
  <section class="section" id="payment">
    <!-- Add new -->
    <b-card v-if="payments.length===0 && !addNew">
      <b-card-body class="text-center">
        <h2 class="mb-4">You have no payments</h2>
        <img src="../../../assets/hello.svg" alt="payments" class="img-fluid">
        <button @click="addNew=true" class="btn btn-primary btn-lg m-0 mt-4">Add new</button>
      </b-card-body>
    </b-card>

    <!-- Form -->
    <b-card v-else-if="addNew">
      <b-card-body>
        <div class="form-group">
          <input v-model="newCreditCard['number']" type="text" class="form-control" placeholder="Card number" autocomplete="cc-number" required>
        </div>

        <div class="row mt-2">
          <div class="col-6">
            <div class="form-group">
              <input v-model="newCreditCard['month']" type="text" class="form-control" id="expiry-month" placeholder="MM" autocomplete="cc-exp-month" required>
            </div>
          </div>
          
          <div class="col-6">
            <div class="form-group">
              <input v-model="newCreditCard['year']" type="text" class="form-control" id="expiry-year" placeholder="YY" autocomplete="cc-exp-year" required>
            </div>
          </div>
        </div>

        <div class="row mt-2">
          <div class="form-group">
            <input v-model="newCreditCard['cvv']" type="password" class="form-control" id="cvv" placeholder="CV" autocomplete="cc-csc" required>
          </div>
        </div>

        <button @click="sendChanges" class="btn btn-primary btn-md m-0 mt-4">
          Validate
        </button>

        <!-- <div class="form-group">
          <input v-model="bankAccounts['iban']" type="text" class="form-control" id="iban-input" placeholder="BANK 0123456789" required>
        </div> -->
      </b-card-body>
    </b-card>
    
    <!-- Cards -->
    <div v-else class="row">
      <div class="col-12">
        <b-card v-for="(payment, index) in payments" :key="payment.id" :class="{ 'mt-2': index >= 1 }">
          <b-card-body>
            {{ payment.id }}
            
            <div class="row">
              <div class="col">
                <button @click="deleteCreditCard(payment.id)" class="btn btn btn-light">
                  <i class="fa fa-trash mr-2"></i>
                </button>
              </div>
            </div>
          </b-card-body>
        </b-card>

        <b-card class="text-center mt-2">
          <button @click="addNew=true" class="btn btn-lg btn-primary">New card</button>
        </b-card>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Payment',
  
  title () {
    return 'Payment methods'
  },

  data () {
    return {
      addNew: false,
      newCreditCard: {},
      bankAccounts: {}
    }
  },
  
  computed: {
    payments () {
      // return this.$store.state.authenticationModule.userDetails.payments
      return this.$store.getters['authenticationModule/getPaymentMethods']
    }
  },
  
  methods: {
    sendChanges () {
      this.$store.commit('authenticationModule/addNewCreditCard', this.newCreditCard)
      this.addNew = false
    },
    
    deleteCreditCard (id) {
      this.$store.commit('authenticationModule/deleteCreditCard', id)
    }
  }
}
</script>
