<template>
  <section class="page-section p-3" id="testimonials">

    <div class="container">
      <div class="row">
        <div class="col-12 text-center mb-4">
          <h3 class="font-weight-bold">{{ companyDetails.name }} makes you happier</h3>
          <p class="mb-4">
            More than 3 million people rely on {{ companyDetails.name }} to take care of their tedious tasks.
          </p>
        </div>

        <!-- Cards -->
        <template v-for="(testimonial, index) in testimonials">
          <div :class="{ 'mt-2': index >= 2 }" :key="index" class="col-sm-12 col-md-6">
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

<<<<<<< HEAD:frontend/src/components/hero/sections/Testimonials.vue
        <div class="col-12 text-center mt-5">
          <h3 class="font-weight-bold">Wave goodbye to your busywork</h3>
          <p>Don't waste another minute. Create an account now and start saving more time.</p>
=======
          <template v-for="(testimonial, index) in testimonials" :key="index">
            <div :class="{ 'mt-2': index >= 2 }" class="col-sm-12 col-md-6">
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
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09:frontend/src/components/hero/sections/TestimonialsIterator.vue

          <router-link :to="{ name: 'signup' }" class="btn btn-lg btn-secondary">
            Signup for free
          </router-link>
        </div>
      </div>
    </div>

  </section>
</template>

<script>
import testimonials from '../../../data/testimonials.json'

export default {
  name: 'TestimonialsIterator',
  data () {
    return {
      testimonials: testimonials
    }
  }
}
</script>
