<template>
  <section id="payment">

    <!-- Intro -->
    <base-card v-if="payments.length===0 && !addNew" class="text-center">
      <h2 class="mb-4">You have no payments</h2>
      <img src="../../../assets/hello.svg" alt="payments" class="img-fluid">
      <button type="button" class="btn btn-primary btn-lg m-0 mt-4" @click="addNew=true">Add new</button>
    </base-card>

    <!-- Create -->
    <base-validation-card v-else-if="addNew" @validateAction="createNewCard">
      <fields-iterator :form-fields="fields" @start-action="registerChange" />
    </base-validation-card>

    <!-- Payments -->
    <div v-else class="row">
      <div class="col-12">
        <base-card v-for="(payment, index) in payments" :key="payment.id" :class="{ 'mt-2': index >= 1 }">
          {{ payment.id }}

          <div class="row">
            <div class="col">
              <button type="button" class="btn btn btn-light" @click="deleteCreditCard(payment.id)">
                <i class="fa fa-trash mr-2"></i>
              </button>
            </div>
          </div>
        </base-card>

        <base-card class="text-center mt-2">
          <button type="button" class="btn btn-lg btn-primary" @click="addNew=true">New card</button>
        </base-card>
      </div>
    </div>

  </section>
</template>

<script>
import { mapState } from 'pinia'
import { useAuthentication } from '@/store/authentication'

import BaseValidationCard from './BaseValidationCard.vue'
import FieldsIterator from '../../FieldsIterator.vue'

export default {
  name: 'PaymentsSection',
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
    ...mapState(useAuthentication, {
      payments: (state) => {
        return state.userDetails.payments
      }
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
