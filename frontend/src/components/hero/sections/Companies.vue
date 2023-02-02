<template>
  <section class="p-4 mt-2 mb-4 text-center" id="companies">

    <div class="container">
      <p class="text-muted text-uppercase mb-3">Trusted by product-led innovators around the world</p>
      <div class="icons d-flex justify-content-between d-wrap">
        <img v-for="company in companies" :key="company.alt" :src="company.image" :alt="company.alt" height=50 width=120>
      </div>
    </div>
    
  </section>
</template>

<script>
import companies from '../../../data/companies.json'

export default {
  name: 'Companies',
  
  data () {
    return {
      companies: companies
    }
  }
}
</script>
