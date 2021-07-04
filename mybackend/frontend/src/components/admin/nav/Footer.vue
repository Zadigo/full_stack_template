<template>
  <footer class="page-footer text-center font-small primary-color-dark darken-2 mt-4 wow fadeIn animated">
    <div class="pt-4">
      <a class="btn btn-outline-white waves-effect waves-light" href="" target="_blank" role="button">
        Download MDB
        <i class="fas fa-download ml-2"></i>
      </a>
      <a class="btn btn-outline-white waves-effect waves-light" href="" target="_blank" role="button">
        Start free tutorial
        <i class="fas fa-graduation-cap ml-2"></i>
      </a>
    </div>

    <hr class="my-4">

    <div class="pb-4">
      <a v-for="social in socials" :key="social.id" :href="social.href" :id="social.id|createAnalaticsId" target="_blank" role="link">
        <i :class="social.icon" class="mr-3"></i>
      </a>
    </div>

    <div class="footer-copyright py-3">
      © {{ currentYear }} Copyright: {{ copyright }}
    </div>
  </footer>
</template>

<script>
  // var DateJs = require('datejs')
  export default {
    name: 'AdminFooter',
    // props: {
    //   copyright: {
    //     type: String,
    //     required: true
    //   },
    //   socials: {
    //     type: Array,
    //     required: true
    //   }
    // },
    data() {
      return {
        currentYear: 2021,
        copyright: 'Something',
        socials: []
      }
    },
    filters: {
      createAnalaticsId(value) {
        return `link_${value}`
      }
    }
  }
</script>
