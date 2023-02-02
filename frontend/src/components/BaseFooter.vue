<template>
<<<<<<< HEAD
  <footer class="page-footer text-center font-small">
    <div class="container pt-5">
      <div class="row text-left">
        
=======
  <footer class="page-footer">
    <div class="container p-4">
      <div class="row">
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
        <page-footer-column v-for="section in sections" :key="section.id" :section="section" />

        <div class="col-sm-12 col-md-3">
          <div class="row">
            <div class="col-12">
<<<<<<< HEAD
              <p class="font-weight-bold text-white text-uppercase">
                Get in touch
              </p>

=======
              <p class="fw-bold mb-1 text-white text-uppercase">Get in touch</p>
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
              <p>
                Any questions? Let us know in store at
                {{ 'companyDetails.address' }}
                or call us on {{ 'companyDetails.telephone' }}
              </p>
            </div>

            <!-- Newsletter -->
            <div class="col-12 pt-2 pb-2">
              <transition name="general-transition" mode="out-in">
                <div v-if="!sent" class="form-group">

                  <label class="mb-2" for="newsletter">Sign up for {{ 'companyDetails.name' }} latest news</label>
                  <input id="newsletter" v-model="newsletterEmail" type="email" class="form-control" placeholder="Email">
                  <button type="button" class="btn btn-md btn-primary m-0 mt-2" @click="subscribeUser">
                    <i class="fa fa-envelope mr-3"></i>
                    Subscribe
                  </button>

                </div>

                <div v-else :class="alertDetails.type" class="alert">
                  {{ alertDetails.message }}
                </div>
              </transition>
            </div>

            <!-- <div class="col-12">
              <p class="font-weight-bold text-white text-uppercase">We accept</p>
              <div class="d-flex justify-content-between">
                <i class="fa fa-cc-mastercard" aria-hidden="true"></i>
                <i class="fa fa-cc-visa" aria-hidden="true"></i>
                <i class="fa fa-cc-google-pay" aria-hidden="true"></i>
              </div>
            </div> -->
          </div>
        </div>
      </div>
    </div>

    <hr class="my-4">

<<<<<<< HEAD
    <!-- Socials -->
    <div class="pb-4">
      <a v-for="social in companyDetails.socials" :key="social.id" :href="social.link" target="_blank" role="link">
=======
    <!-- <div class="pb-4">
      <a v-for="social in companyDetails.socials" :key="social.id" :href="social.link" target="_blank" rel="noopener noreferrer nofollow" role="link">
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
        <i :class="social.icon" class="mr-3"></i>
      </a>
    </div> -->

    <!-- Copyright -->
    <div class="footer-copyright py-3">
      <div class="d-flex flex-direction-row justify-content-center">
        <router-link :to="{ name: 'home_view' }" class="mx-1">
          Terms of sale
        </router-link>

        <router-link :to="{ name: 'home_view' }" class="mx-1">
          Terms of use
        </router-link>

        <span>© {{ 'currentYear' }} Copyright: {{ 'companyDetails.name' }}</span>
      </div>
    </div>
  </footer>
</template>

<script>
import footer from '../data/footer.json'
import PageFooterColumn from './PageFooterColumn.vue'

export default {
  name: 'BaseFooter',
  components: { PageFooterColumn },
  setup () {
    return {
      sections: footer
    }
  },
  data () {
    return {
      newsletterEmail: null,
      sent: false
    }
  },

  methods: {
    async subscribeUser () {
      this.$api.subscribe(this.newsletterEmail)
      .then((response) => {
        console.log(response)
        this.newsletterEmail = null
        this._newMessage('alert-success', 'Subscription validated')
      })
      .catch((error) => {
        console.error(error)
      })
    }
  }
}
</script>

<style scoped>
  .page-footer {
      background-color: #1C2331;
  }
</style>

