<template>
  <section class="page-section p-1 mt-2 mb-4" id="benefits">

    <h2 class="my-5 h3 text-center">...and even more</h2>

    <div class="row features-small mt-5">
      <div v-for="(benefit, index) in additionalbenefits" :key="index" class="col-xl-3 col-lg-6">
        <div class="row">
          <div class="col-2">
            <!-- <i class="fab fa-firefox fa-2x mb-1 indigo-text" aria-hidden="true"></i> -->
            <font-awesome-icon icon="star" class="fa-2x mb-1 indigo-text"></font-awesome-icon>
          </div>

          <div class="col-10 mb-2">
            <h5 class="feature-title font-bold mb-1">{{ benefit.title }}</h5>
            <p class="grey-text mt-2">{{ benefit.content }}</p>

            <!-- <h5 class="feature-title font-bold mb-1">Cross-browser compatibility</h5> -->
            <!-- <p class="grey-text mt-2">Chrome, Firefox, IE, Safari, Opera, Microsoft Edge - MDB loves all browsers; all browsers love MDB. -->
          </div>
        </div>
      </div>

      <!-- <div class="col-xl-3 col-lg-6">
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
        <div class="row">
          <div class="col-2">
            <i class="far fa-file-code fa-2x mb-1 indigo-text" aria-hidden="true"></i>
          </div>
          <div class="col-10 mb-2">
            <h5 class="feature-title font-bold mb-1">SASS files</h5>
            <p class="grey-text mt-2">Arranged and well documented .scss files can't wait until you compile them.</p>
          </div>
        </div>
      </div> -->
    </div>

  </section>
</template>

<script>
import additionalbenefits from '../../../data/additionalbenefits.json'

export default {
  name: 'AdditionalBenefits',

  data () {
    return {
      additionalbenefits: additionalbenefits
    }
  }
}
</script>
