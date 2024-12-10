<doc>
  Use his page in order to help the customer read more about
  the products proposed by your enterprise
</doc>

<template>
  <base-site-vue>
    <template #default>
      <base-intro-vue intro-classes="text-left text-white bg-dark" wrapper-classes="d-flex justify-content-left align-items-center p-5" height="100vh" class="shadow-sm">
        <template #default>
          <div class="w-50 text-left">
            <h1 class="fw-bold">Build your landing page in minutes</h1>
            <p class="fw-light">
              Landing pages are the best way to get more leads, sales, and
              signups out of your marketing campaigns. When you create pages
              with Smart Builder, you get data-backed recommendations on
              what works—so you can create high-performing campaigns in a
              fraction of the time.
            </p>
            <button type="button" class="btn btn-lg btn-light">Start building for free</button>
          </div>

          <div class="right">
            <img :src="require('@/assets/payment.svg')" class="img-fluid" width="700">
          </div>
        </template>
      </base-intro-vue>

      <div class="container">
        <div class="row">
          <div class="col-12">
            <!-- Presentation 1 -->
            <section class="p-5 text-center">
              <h1 class="display-3 mb-4">How does Smart Builder work?</h1>
              <p class="fw-light">
                Smart Builder helps you create your best-performing landing pages in a few simple steps.
                Just provide some information about your campaign and Smart Builder will suggest an eye-catching layout
                designed to resonate with your audience. Complete a few prompts and watch as Smart Builder instantly
                generates on-brand copy for your page. Make whatever changes you want, add no-code functionality through
                apps, and go live with a landing page that’s built to convert.
              </p>
            </section>

          </div>
        </div>
      </div>

      <!-- Testimony -->
      <section class="p-4 bg-dark text-white text-left">
        <p class="fs-4 m-0">
          That’s really what attracted me to [Smart Builder] in the first place—the
          fact that it’s smart. It makes decisions that are based scientifically, rather
          than on someone’s gut feeling.
        </p>
        <p class="fs-5 mt-4 fw-light"><span class="fw-bold">Peter Letts,</span> Founder, Abyss Scuba Diving</p>
      </section>

      <section class="p-5">
        <div class="container">
          <div class="row">
            <div class="col-6">
              <h2 class="display-4 mb-3">Add more functionality with Unbounce apps</h2>
              <p class="fw-light">
                Whether you need your landing page to sell products, accept payments, or collect leads,
                Unbounce Apps help you do it all—without even having to code. Connect the tools you already
                use (and discover new ones you’ll love) so you can get your visitors to take action
                without ever leaving your page.
              </p>
              <button type="button" class="btn btn-lg btn-outline-primary">Start building for free</button>
            </div>

            <div class="col-6 gs-5">
              <img :src="require('@/assets/payment.svg')" class="img-fluid">
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

export default {
  name: 'ProductView',
  components: {
    BaseIntroVue,
    BaseSiteVue
  }
}
</script>
