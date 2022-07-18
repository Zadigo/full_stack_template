<template>
  <div class="container">
    <section class="mt-6">
      <div class="row">
        <div class="col-sm-12 col-md-8 offset-md-2">
          <b-card id="not_found" title="404" img-src="https://images.unsplash.com/photo-1500917293891-ef795e70e1f6?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fG1vZGVsfGVufDB8MHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1280&q=60" img-top overlay>
            <div class="d-flex justify-content-left">
              <b-card-text>
                <router-link :to="{ name: 'home' }">Home</router-link>
                <!-- <span class="ml-2 mr-2">|</span> -->
                <!-- <router-link :to="{ name: 'products' }">Shop</router-link> -->
              </b-card-text>
            </div>
          </b-card>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'NotFoundView',
  beforeRouteLeave (to, from, next) {
    console.log(to)
    next()
  }
}
</script>

<style scoped>
  h4.card-title {
    font-size: 8rem;
  }

  #not_found {
    color: white;
  }

  #not_found a {
    color: white;
  }
</style>
