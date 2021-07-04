<template>
  <section id="pricing">
    <header>
      <!-- Jumbotron -->
      <div class="p-5 text-center bg-light" id="intro">
        <h1 class="mb-3 font-weight-bold">We've got you covered</h1>
        <p class="font-weight-bold">
          Need a hand getting started or getting the most out of {{ companyDetails.name }}?
        </p>
      </div>
    </header>

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
          tool for your business? Chat with our team to see if there’s a fit." buttonTitle="Let's chat" />
        </div>
        <div class="col-3">
          <contact-card title="Get support" content="Wondering if Unbounce is the right 
          tool for your business? Chat with our team to see if there’s a fit." buttonTitle="Get support" />
        </div>
        <div class="col-3">
          <contact-card title="Media inquiries" content="Wondering if Unbounce is the right 
          tool for your business? Chat with our team to see if there’s a fit." buttonTitle="Get in touch" />
        </div>
        <div class="col-3">
          <contact-card title="Partnership inquiries" content="Wondering if Unbounce is the right 
          tool for your business? Chat with our team to see if there’s a fit." buttonTitle="Let's chat" />
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
                  <input type="text" class="form-control" id="firstname" placeholder="Firstname">
                </div>
              </div>
            </div>
          </b-card>
        </div>
      </div>

      <!-- Banner -->
      <div class="col-12">
        <banner-cta />
      </div>
    </div>
  </section>
</template>

<script>
import Card from '@/components/contact/Card.vue'

export default {
  name: 'ContactUs',
  components: {
    'contact-card': Card
  },
  title() {
    return 'Contact our friendly support'
  }
}
</script>
