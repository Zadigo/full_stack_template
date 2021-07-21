<template>
  <footer class="page-footer text-center font-small wow fadeIn">
    <div class="container pt-3">
      <div class="row text-left">
        <page-footer-column v-for="section in sections" :key="section.id" :section="section" />

        <div class="col-3">
          <div class="row">
            <div class="col-12">
              <p class="font-weight-bold text-white text-uppercase">Get in touch</p>
              <p>
                Any questions? Let us know in store at 
                {{ companyDetails.address }} 
                or call us on {{ companyDetails.telephone }}
              </p>
            </div>

            <!-- Newsletter -->
            <div class="col-12 pt-2 pb-2">
              <transition name="general-transition" mode="out-in">
                <div v-if="!sent" class="form-group">
                  <label class="mb-2" for="newsletter">Sign up for {{ companyDetails.name }} latest news</label>
                  <input v-model="newsletterEmail" type="email" class="form-control" id="newsletter" placeholder="Email">
                  <button @click="subscribeUser" class="btn btn-md btn-primary m-0 mt-2" role="button">
                    <i class="fa fa-envelope mr-3"></i>
                    Subscribe
                  </button>
                </div>  

                <div v-else :class="alertDetails.type" class="alert">
                  {{ alertDetails.message }}  
                </div>
              </transition>
            </div>

            <div class="col-12">
              <p class="font-weight-bold text-white text-uppercase">We accept</p>
              <div class="d-flex justify-content-between">
                <i class="fa fa-cc-mastercard" aria-hidden="true"></i>
                <i class="fa fa-cc-visa" aria-hidden="true"></i>
                <i class="fa fa-cc-google-pay" aria-hidden="true"></i> 
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

    <hr class="my-4">

    <div class="pb-4">
      <a v-for="social in companyDetails.socials" :key="social.id" :href="social.link" target="_blank" role="link">
        <i :class="social.icon" class="mr-3"></i>
      </a>
    </div>

    <div class="footer-copyright py-3">
      <div class="d-flex flex-direction-row justify-content-center">
        <span>© {{ currentYear }} Copyright: {{ companyDetails.name }}</span>
        <router-link :to="{ name: 'terms_of_condition' }" class="ml-3">CGV</router-link>
        <router-link :to="{ name: 'terms_of_use' }" class="ml-3">CGU</router-link>
      </div>
    </div>
  </footer>
</template>

<script>
import PageFooterData from '../data/PageFooter.json'
import PageFooterColumn from './PageFooterColumn.vue'

export default {
  name: 'PageFooter',
  components: {
    PageFooterColumn
  },

  data () {
    return {
      newsletterEmail: null,
      sent: false,
      alertDetails: {
        type: 'alert-success',
        message: null 
      },
      sections: PageFooterData
    }
  },

  methods: {
    subscribeUser () {
      this.$api.subscribe(this.newsletterEmail)
      .then((response) => {
        console.log(response)
        this.newsletterEmail = null
        this._newMessage('alert-success', 'Subscription validated')
      })
      .catch((error) => {
        console.error(error)
        this._newMessage('alert-danger', 'Email is not valid')
      })
    },

    _newMessage (type, message) {
      this.alertDetails['type'] = type
      this.alertDetails['message'] = message
      return this.alertDetails
    }
  }
}
</script>

<style scoped>
  /* .page-footer {
    background-color: #1C2331;
	}
 */

  .page-footer {
      background-color: #1C2331;
  }
</style>

