<template>
  <section id="testimonials">
    <div id="banner bg-blue bg-lighten-md p-4">

      <div class="container">
        <div class="row">
          <div class="col-12 text-center mb-4">
            <h3 class="font-weight-bold">{{ companyDetails.name }} makes you happier</h3>
            <p class="mb-4">More than 3 million people rely on {{ companyDetails.name }} to take care of their tedious tasks.</p>
          </div>

          <template v-for="(testimonial, index) in testimonials">
            <div :class="{ 'mt-2': index >= 2 }" :key="index" class="col-6">
              <b-card>
                <b-card-text>
                  {{ testimonial.content }}
                  <p class="font-weight-bold text-muted text-uppercase mt-3">
                    {{ testimonial.author }}
                  </p>
                </b-card-text>
              </b-card>
            </div>
          </template>

          <div class="col-12 text-center mt-5">
            <h3 class="font-weight-bold">Wave goodbye to your busywork</h3>
            <p>Don't waste another minute. Create an account now and start saving more time.</p>
            <router-link :to="{ name: 'signup' }" class="btn btn-lg btn-secondary">Signup for free</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import testimonials from '../../../data/testimonials.json'

export default {
  name: 'Testimonials',
  data () {
    return {
      testimonials: testimonials
    }
  }
}
</script>
