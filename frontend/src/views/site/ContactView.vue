<template>
  <base-site-vue>
    <template #default>
      <section id="contact">
        <base-intro-vue id="contact" class="border-bottom">
          <template #default>
            <div class="py-5 my-5 text-center">
              <h1 class="display-5 fw-bold">Centered hero</h1>
              <div class="col-lg-6 mx-auto">
                <p class="lead mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
              </div>
            </div>
          </template>
        </base-intro-vue>

        <div class="container">
          <!-- Contact-1 -->
          <div class="row mt-4">
            <div class="col-4">
              <div class="card">
                <div class="card-body">
                  <h4 class="fw-bold card-title mb-4">Email customer support</h4>
                  <p class="mb-1">Have a question? Encountered an issue?</p>
                  <p><i class="fa fa-envelope mr-2"></i>help@gettimely.com</p>
                  <p class="mb-1">For questions about payments and billing</p>
                  <p><i class="fa fa-envelope mr-2"></i>billing@gettimely.com</p>
                </div>
              </div>
            </div>

            <div class="col-4">
              <div class="card">
                <div class="card-body">
                  <h4 class="fw-bold card-title mb-4">Premium phone support</h4>
                  <p>For customers with premium phone support</p>
                </div>
              </div>
            </div>

            <div class="col-4">
              <div class="card">
                <div class="card-body">
                  <h4 class="fw-bold card-title mb-4">For sales enquiries</h4>
                  <p>
                    <font-awesome-icon icon="fa-solid fa-envelope" class="me-2"></font-awesome-icon>sales@gettimely.com
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Contact-2 -->
          <div class="row mt-4 d-none">
            <div class="col-3">
              <contact-card title="Contact a specialist" content="Wondering if Unbounce is the right 
              tool for your business? Chat with our team to see if there’s a fit." button-title="Let's chat" />
            </div>
            <div class="col-3">
              <contact-card title="Get support" content="Wondering if Unbounce is the right 
              tool for your business? Chat with our team to see if there’s a fit." button-title="Get support" />
            </div>
            <div class="col-3">
              <contact-card title="Media inquiries" content="Wondering if Unbounce is the right 
              tool for your business? Chat with our team to see if there’s a fit." button-title="Get in touch" />
            </div>
            <div class="col-3">
              <contact-card title="Partnership inquiries" content="Wondering if Unbounce is the right 
              tool for your business? Chat with our team to see if there’s a fit." button-title="Let's chat" />
            </div>
          </div>

          <!-- Form -->
          <div class="row">
            <div class="col-sm-12 col-md-8 offset-md-2 mt-5 mb-5">
              <div class="card">
                <div class="card-body">
                  <p class="display-6 fw-bold">Get in touch</p>

                  <div class="row">
                    <div class="col-6">
                      <div class="form-group">
                        <input id="email" type="email" class="form-control" placeholder="Email" autocomplete="email">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Banner -->
          <div class="col-12">
            <base-secondary-cta />
          </div>
        </div>
      </section>
    </template>
  </base-site-vue>
</template>

<script>
import BaseIntroVue from '@/layouts/BaseIntro.vue'
import BaseSiteVue from '@/layouts/BaseSite.vue'
import ContactCard from '@/components/contact/BaseCard.vue'

export default {
  name: 'ContactView',
  components: {
    ContactCard,
    BaseIntroVue,
    BaseSiteVue
  },
  title() {
    return 'Contact our friendly support'
  },
  data() {
    return {
      pageTitle: "We've got you covered",
    }
  },
  computed: {
    pageDescription() {
      return `Need a hand getting started or getting the most out of ${this.companyDetails.name}?`
    }
  }
}
</script>
