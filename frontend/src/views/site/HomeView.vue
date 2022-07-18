<template>
  <base-site-vue>
    <template #default>
      <!-- Intro -->
      <base-intro-vue :image="require('@/assets/hero1.jpg')" height="90vh" class="shadow-sm">
        <template #default>
          <div class="text-white">
            <h1 class="mb-3 display-5 fw-bold">Assouvis tes ardents désir</h1>
            <h5 class="mb-4 lead">Craquez pour nos nouveautés signées Lounge</h5>
  
            <router-link :to="{ name: 'home_view' }" class="btn btn-dark btn-lg btn-rounded" role="button">
              Discover
            </router-link>
          </div>
        </template>
      </base-intro-vue>
  
      <!-- Sections -->
      <!-- Companies anner -->
      <div id="banner" class="p-4 text-center bg-light">
        <div class="container">
          <p class="text-muted text-uppercase mb-3">Trusted by product-led innovators around the world</p>
          <div class="icons d-flex justify-content-between d-wrap">
            <img v-for="company in companies" :key="company.alt" :src="company.image" :alt="company.alt" height="50" width="120">
          </div>
        </div>
      </div>
  
      <!-- Call to action -->
      <section class="page-section text-white text-center bg-dark">
        <div class="container px-4 px-lg-5">
          <h2 class="p-3">We've got what you need!</h2>
  
          <hr class="divider divider-light">
  
          <div class="row gx-4 gx-lg-5 justify-content-center">
            <div class="col-lg-8">
              <p class="text-white-75 mb-4">
                {{ 'Example website' }} has everything you need to get your new website
                up and running in no time! Choose one of our open source, free to download,
                and easy to use themes! No strings attached!
              </p>
  
              <router-link :to="{ name: 'home_view' }" class="btn btn-primary btn-lg">
                Get started!
              </router-link>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Benefits -->
      <section class="p-5">
        <div class="container">
          <div class="row gx-5">
            <div class="col-4">
              <i class="fa fa-user text-blud lighten-2"></i>
              <h4 class="fw-bold">Integrate</h4>
              <p>Link your web apps with a few clicks, so they can share data</p>
            </div>
      
            <div class="col-4">
              <i class="fa fa-user text-blud lighten-2"></i>
              <h4 class="fw-bold">Automate</h4>
              <p>Pass info between your apps with workflows called Zaps</p>
            </div>
      
            <div class="col-4">
              <i class="fa fa-user text-blud lighten-2"></i>
              <h4 class="fw-bold">Innovate</h4>
              <p>Build processes faster and get more done—no code required</p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Testimonials -->
      <section id="testimonials">
        <div id="banner" class="bg-primary bg-lighten-md p-4">
          <div class="container">
            <div class="row">
              <div class="col-12 text-center mb-4">
                <h3 class="font-weight-bold">{{ 'companyDetails.name' }} makes you happier</h3>
                <p class="mb-4">More than 3 million people rely on {{ 'companyDetails.name' }} to take care of their tedious tasks.</p>
              </div>
  
              <template v-for="(testimonial, index) in testimonials" :key="index">
                <div :class="{ 'mt-2': index >= 2 }" class="col-sm-12 col-md-6">
                  <div class="card">
                    <div class="card-body">
                      {{ testimonial.content }}
                      <p class="font-weight-bold text-muted text-uppercase mt-3">
                        {{ testimonial.author }}
                      </p>
                    </div>
                  </div>
                </div>
              </template>
  
              <div class="col-12 text-center mt-5">
                <h3 class="font-weight-bold">Wave goodbye to your busywork</h3>
                <p>Don't waste another minute. Create an account now and start saving more time.</p>
                <router-link :to="{ name: 'home_view' }" class="btn btn-lg btn-light">
                  Signup for free
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Boxes -->
      <section id="other-benefits">
        <h2 class="my-5 h3 text-center">...and even more</h2>
  
        <div class="row features-small mt-5">
          <div class="col-xl-3 col-lg-6">
            <div class="row">
              <div class="col-2">
                <i class="fab fa-firefox fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2 pl-3">
                <h5 class="feature-title font-bold mb-1">Cross-browser compatibility</h5>
                <p class="grey-text mt-2">Chrome, Firefox, IE, Safari, Opera, Microsoft Edge - MDB loves all browsers; all browsers love MDB.
                </p>
              </div>
            </div>
          </div>
  
          <div class="col-xl-3 col-lg-6">
            <div class="row">
              <div class="col-2">
                <i class="fas fa-level-up-alt fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2">
                <h5 class="feature-title font-bold mb-1">Frequent updates</h5>
                <p class="grey-text mt-2">MDB becomes better every month. We love the project and enhance as much as possible.
                </p>
              </div>
            </div>
          </div>
  
          <div class="col-xl-3 col-lg-6">
            <div class="row">
              <div class="col-2">
                <i class="fas fa-comments fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2">
                <h5 class="feature-title font-bold mb-1">Active community</h5>
                <p class="grey-text mt-2">Our society grows day by day. Visit our forum and check how it is to be a part of our family.
                </p>
              </div>
            </div>
          </div>
  
          <div class="col-xl-3 col-lg-6">
            <div class="row">
              <div class="col-2">
                <i class="fas fa-code fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2">
                <h5 class="feature-title font-bold mb-1">jQuery 3.x</h5>
                <p class="grey-text mt-2">MDB is integrated with newest jQuery. Therefore you can use all the latest features which come along with
                  it.
                </p>
              </div>
            </div>
          </div>
        </div>
  
        <div class="row features-small mt-4">
          <div class="col-xl-3 col-lg-6">
            <div class="row">
              <div class="col-2">
                <i class="fas fa-cubes fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2">
                <h5 class="feature-title font-bold mb-1">Modularity</h5>
                <p class="grey-text mt-2">Material Design for Bootstrap comes with both, compiled, ready to use libraries including all features as
                  well as modules for CSS (SASS files) and JS.</p>
              </div>
            </div>
          </div>
  
          <div class="col-xl-3 col-lg-6">
            <div class="row">
              <div class="col-2">
                <i class="fas fa-question fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2">
                <h5 class="feature-title font-bold mb-1">Technical support</h5>
                <p class="grey-text mt-2">We care about reliability. If you have any questions - do not hesitate to contact us.
                </p>
              </div>
            </div>
          </div>
  
          <div class="col-xl-3 col-lg-6">
            <!--Grid row-->
            <div class="row">
              <div class="col-2">
                <i class="fas fa-th fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2">
                <h5 class="feature-title font-bold mb-1">Flexbox</h5>
                <p class="grey-text mt-2">MDB fully supports Flex Box. You can forget about alignment issues.</p>
              </div>
            </div>
          </div>
  
          <div class="col-xl-3 col-lg-6">
            <!--Grid row-->
            <div class="row">
              <div class="col-2">
                <i class="far fa-file-code fa-2x mb-1 indigo-text" aria-hidden="true"></i>
              </div>
              <div class="col-10 mb-2">
                <h5 class="feature-title font-bold mb-1">SASS files</h5>
                <p class="grey-text mt-2">Arranged and well documented .scss files can't wait until you compile them.</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </template>
  </base-site-vue>
</template>

<script>
import BaseIntroVue from '@/layouts/BaseIntro.vue'
import BaseSiteVue from '@/layouts/BaseSite.vue'

import companies from '@/data/companies.json'
import testimonials from '@/data/testimonials.json'

export default {
  name: 'HomeView',
  components: {
    BaseIntroVue,
    BaseSiteVue
},
  setup () {
    return {
      companies,
      testimonials
    }
  }
}
</script>

<style scoped>
#testimonials .card {
  min-height: 200px;
}
</style>