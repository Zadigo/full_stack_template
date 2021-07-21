<template>
  <section id="payment">
    <!-- Intro -->
    <base-card v-if="payments.length===0 && !addNew" class="text-center">
      <h2 class="mb-4">You have no payments</h2>
      <img src="../../../assets/hello.svg" alt="payments" class="img-fluid">
      <button @click="addNew=true" class="btn btn-primary btn-lg m-0 mt-4">Add new</button>
    </base-card>
    
    <!-- Create -->
    <base-validation-card @validateAction="createNewCard" v-else-if="addNew">
      <fields-iterator @startAction="registerChange" :formFields="fields" />
      
      <!-- <div class="form-group">
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
        <div class="col-12">
          <div class="form-group">
            <input v-model="newCreditCard['cvv']" type="password" class="form-control" id="cvv" placeholder="CV" autocomplete="cc-csc" required>
          </div>
        </div>
      </div> -->

      <!-- <div class="form-group">
        <input v-model="bankAccounts['iban']" type="text" class="form-control" id="iban-input" placeholder="BANK 0123456789" required>
      </div> -->
    </base-validation-card>
    
    <!-- Payments -->
    <div v-else class="row">
      <div class="col-12">
        <base-card v-for="(payment, index) in payments" :key="payment.id" :class="{ 'mt-2': index >= 1 }">
          {{ payment.id }}
          
          <div class="row">
            <div class="col">
              <button @click="deleteCreditCard(payment.id)" class="btn btn btn-light">
                <i class="fa fa-trash mr-2"></i>
              </button>
            </div>
          </div>
        </base-card>

        <base-card class="text-center mt-2">
          <button @click="addNew=true" class="btn btn-lg btn-primary">New card</button>
        </base-card>
      </div>
    </div>
  </section>
</template>

<script>
import BaseValidationCard from './BaseValidationCard.vue'

import { mapState } from 'vuex'
import FieldsIterator from '../../FieldsIterator.vue'

export default {
  name: 'Payment',
  components: { BaseValidationCard, FieldsIterator },
  
  title () {
    return 'Payment methods'
  },

  data () {
    return {
      addNew: false,
      newCreditCard: {
        number: '4242424242424242',
        month: null,
        year: null,
        cvv: null
      },
      bankAccounts: {},
      formFieldsFor: 'payment'
    }
  },
  
  computed: {
    ...mapState('profileModule', {
      payments: (state) => { return state.userDetails.payments }
    }),

    // fields() {
    //   return this.getFieldsFor('payment')
    // }
  },
  
  methods: {
    createNewCard() {

    },
    sendChanges () {
      this.$store.commit('authenticationModule/addNewCreditCard', this.newCreditCard)
      this.addNew = false
    },
    
    deleteCreditCard (id) {
      this.$store.commit('authenticationModule/deleteCreditCard', id)
    },

    registerChange(field, value) {
      this.newCreditCard[field] = value
    }
  }
}
</script>
