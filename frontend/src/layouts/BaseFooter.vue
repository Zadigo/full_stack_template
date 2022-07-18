<template>
  <footer class="bg-light">
    <div class="container p-4">
      <section class="mb-4 text-center">
        <a v-for="(social, i) in footer.socials" :key="i" :href="social.href" :style="`background-color: #${getColor(social.name)}`" class="btn btn-primary btn-floating m-1" role="button">
          <i class="fab fa-facebook-f"></i>
        </a>
      </section>

      <section class="text-center">
        <div class="row">
          <div v-for="(section, i) in footer.sections" :key="i" class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">
              {{ section.title }}
            </h5>

            <ul class="list-unstyled mb-0">
              <li v-for="(link, t) in section.links" :key="t">
                <router-link :to="{ name: link.to }" class="text-dark">
                  {{ link.name }}
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </section>
    </div>

    <!-- Copyright -->
    <div class="copyright text-center p-3">
      © 2020 Copyright:
      <router-link :to="{ name: 'templates_view' }" class="text-dark">
        John Pendenque
      </router-link>
    </div>
  </footer>
</template>

<script>
import footer from '../data/footer.json'

export default {
  name: 'BaseFooter',
  setup () {
    return {
      footer: footer
    }
  },
  methods: {
    getColor (name) {
      var colors = {
        'Facebook': '#3b5998',
        'Google': '#dd4b39',
        'Instagram': '#ac2bac',
        'Twitter': '#55acee',
        'Linkedin': '#0082ca'
      }
      return colors[name]
    }
  }
}
</script>

<style scoped>

.copyright {
  background-color: rgba(0, 0, 0, 0.2)
}
</style>
