<template>
  <footer class="page-footer text-center font-small wow fadeIn">
    <div class="container pt-3">
      <div class="row text-left">
        <!-- Company -->
        <div class="col-3">
          <p class="font-weight-bold text-white text-uppercase">Company info</p>
          <ul class="p-0">
            <li><router-link :to="{ name: 'home' }" role="link" aria-labelledby="Home">Home</router-link></li>
            <!-- <li><router-link :to="{ name: 'products' }" role="link" aria-labelledby="Shop">Shop</router-link></li> -->
            <li><router-link :to="{ name: 'about' }" role="link" aria-labelledby="About us">About us</router-link></li>
            <li><router-link :to="{ name: 'jobs' }" role="link" aria-labelledby="Home">Career</router-link></li>
          </ul>
        </div>

        <!-- Support -->
        <div class="col-3">
          <p class="font-weight-bold text-white text-uppercase">Help and support</p>
          <ul class="p-0">
            <!-- <li><router-link :to="{ name: 'products' }" role="link" aria-label="Home">Shipping info</router-link></li> -->
            <!-- <li><router-link :to="{ name: 'faq' }" role="link" aria-label="Home">FAQ</router-link></li> -->
            <li><router-link :to="{ name: 'pricing' }" role="link" aria-label="Home">Pricing</router-link></li>
            <!-- <li><router-link :to="{ name: 'jobs' }" role="link" aria-label="Jobs">Jobs</router-link></li> -->
          </ul>
        </div>
        
        <!-- Customer care -->
        <div class="col-3">
          <p class="font-weight-bold text-white text-uppercase">Customer care</p>
          <ul class="p-0">
            <li><router-link :to="{ name: 'contact' }" role="link" aria-label="Home">Contact</router-link></li>
            <!-- <li><router-link :to="{ name: 'products' }" role="link" aria-label="Home">Another link</router-link></li> -->
            <!-- <li><router-link :to="{ name: 'products' }" role="link" aria-label="Home">Something to click</router-link></li> -->
            <!-- <li><router-link :to="{ name: 'products' }" role="link" aria-label="Home">What</router-link></li> -->
          </ul>
        </div>

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
        <span>© 2018 Copyright: {{ companyDetails.name }}</span>
        <router-link :to="{ name: 'terms_of_condition' }" class="ml-3">CGV</router-link>
        <router-link :to="{ name: 'terms_of_use' }" class="ml-3">CGU</router-link>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {
      newsletterEmail: null,
      sent: false,
      alertDetails: {
        type: 'alert-success',
        message: null 
      },
      socials: []
    }
  },
  methods: {
    subscribeUser () {
      if (this._validateEmail(this.newsletterEmail)) {
        this._newMessage('alert-success', 'Subscription validated')
        this.sent = true
      } else {
        this._newMessage('alert-danger', 'Email is not valid')
        this.sent = true
      }
      // var formData = new FormData()
      // formData.append('email', this.newsletterEmail)

      // Axios({
      //   url: 'http://example.com',
      //   method: 'post',
      //   responseType: 'json',
      //   data: formData
      // })
      // .then((response) => {
      //   response.json().then((data) => {
      //     this._newMessage('alert-success', 'An error occured')
      //     console.log(data)
      //     this.sent = true
      //   })
      // })
      // .error((error) => {
      //   this._newMessage('alert-danger', 'An error occured')
      //   this.sent = true
      //   console.error(error)
      // })
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
  
  .page-footer ul {
    list-style: none;
  }

  .page-footer ul li {
    margin-bottom: .5rem;
  }

  .page-footer ul li a {
    /* color: #b2b2b2 !important; */
    text-decoration: none;
  }

  .page-footer-light {
    color: white;
  }
  .page-footer-light a,
  .page-footer-light i {
    color: white;
  }
</style>

