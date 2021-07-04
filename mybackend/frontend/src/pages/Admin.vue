<template>
  <div id="wrapper">
    <!-- Header -->
    <!-- <Header /> -->
    <router-view name="nav" />

    <!-- Content -->
    <main class="pt-5 mx-lg-5">
      <div class="container-fluid mt-5">
        <!-- <div class="alert alert-danger">
          Some message to show here
        </div> -->

        <router-view />
      </div>
    </main>

    <!-- Footer -->
    <!-- <Footer copyright="Dashboard" :socials="socials" /> -->
    <router-view name="footer" />
  </div>
</template>

<script>
// import Header from '@/components/admin/nav/Header.vue'
// import Footer from '@/components/admin/nav/Footer.vue'

export default {
  name: 'Admin',
  components: {
    // Header,
    // Footer
  },
  data() {
    return {
      socials: [
        { id: 1, name: 'Facebook', icon: 'fab fa-facebook-f', url: 'http://example.com' }
      ]
    }
  }
}
</script>

<style scoped>
  body {
    background-color: #eee!important;
  }
</style>
