<template>
  <section class="page-section text-white text-center">
    <div class="container px-4 px-lg-5">

      <h2 class="p-3">We've got what you need!</h2>
      
      <hr class="divider divider-light">

      <div class="row gx-4 gx-lg-5 justify-content-center">
        <div class="col-lg-8">
          <p class="text-white-75 mb-4">
            {{ companyDetails.name }} has everything you need to get your new website 
            up and running in no time! Choose one of our open source, free to download, 
            and easy to use themes! No strings attached!
          </p>

          <router-link :to="{ name: 'home' }" class="btn btn-light btn-lg">Get started!</router-link>
        </div>
      </div>
    
    </div>
  </section>
</template>

<script>
export default {
  name: 'CTA'
}
</script>
