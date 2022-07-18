<template>
  <base-jumbotron :page-title="pageTitle" :page-description="pageDescription" section-id="contact">
    <div class="container">
      <!-- Contact-1 -->
      <div class="row mt-4">
        <div class="col-4">
          <b-card>
            <h4 class="font-weight-bold mb-4">Email customer support</h4>
            <p class="mb-1">Have a question? Encountered an issue?</p>
            <p><i class="fa fa-envelope mr-2"></i>help@gettimely.com</p>
            <p class="mb-1">For questions about payments and billing</p>
            <p><i class="fa fa-envelope mr-2"></i>billing@gettimely.com</p>
          </b-card>
        </div>

        <div class="col-4">
          <b-card>
            <h4 class="font-weight-bold mb-4">Premium phone support</h4>
            <p>For customers with premium phone support</p>
          </b-card>
        </div>

        <div class="col-4">
          <b-card>
            <h4 class="font-weight-bold mb-4">For sales enquiries</h4>
            <p>
              <i class="fa fa-envelope mr-2"></i>sales@gettimely.com
            </p>
          </b-card>
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
          <b-card>
            <p class="font-weight-bold">Get in touch</p>

            <div class="row">
              <div class="col-6">
                <div class="form-group">
                  <input id="firstname" type="text" class="form-control" placeholder="Firstname">
                </div>
              </div>
            </div>
          </b-card>
        </div>
      </div>

      <!-- Banner -->
      <div class="col-12">
        <base-secondary-cta />
      </div>
    </div>
  </base-jumbotron>
</template>

<script>
import ContactCard from '@/components/contact/BaseCard.vue'

export default {
  name: 'ContactView',
  components: {
    ContactCard
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
