<template>
  <nav class="navbar navbar-expand-lg d-lg-block" style="z-index: 2000;">
    <div class="container-fluid">
      <!-- Navbar brand -->
      <router-link :to="{ name: 'home' }" class="navbar-brand nav-link">
        <strong>{{ companyDetails.name }}</strong>
      </router-link>

      <button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#navbarExample01" aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
        <i class="fas fa-bars"></i>
      </button>

      <div class="collapse navbar-collapse" id="navbarExample01">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li v-for="link in links" :key="link.id" class="nav-item">
            <router-link :to="{ name: link.name }" :id="link.name" class="nav-link" role="link">
              {{ link.title }}
            </router-link>
          </li>

          <li v-show="isAuthenticated" class="nav-item">
            <router-link :to="{ name: 'profile_overview' }" id="profile" class="nav-link" role="link">
              Profile
            </router-link>
          </li>
          <li v-show="!isAuthenticated" class="nav-item">
            <router-link :to="{ name: 'signin' }" id="signin" class="nav-link" role="link">
              Signin
            </router-link>
          </li>
          <li v-show="!isAuthenticated" class="nav-item">
            <router-link :to="{ name: 'signup' }" id="signup" class="nav-link" role="link">
              Signup
            </router-link>
          </li>
          <li v-show="isAuthenticated" class="nav-item">
            <a @click.prevent="logoutUser" id="logout" class="nav-link" role="link">
              Logout
            </a>
          </li>
          <li v-show="isAuthenticated && isAdmin" class="nav-item">
            <router-link :to="{ name: 'admin_home' }" id='admin' class="nav-link" role="link">
              Admin
            </router-link>
          </li>
        </ul>

        <!-- Share -->
        <ul class="navbar-nav d-flex flex-row">
          <li v-for="social in companyDetails.socials" :key="social.id" class="nav-item me-3 me-lg-0">
            <a :href="social.link" class="nav-link" rel="nofollow" target="_blank">
              <i :class="social.icon"></i>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      links: [
        { id: 1, name: 'pricing', title: 'Pricing', authentication: false, admin: false },
        // { id: 2, name: 'products', title: 'Products', authentication: false, admin: false },
      ]
    }
  },
  computed: {
    isAuthenticated () {
      return this.$store.getters['authenticationModule/isAuthenticated']
    },
    isAdmin () {
      return this.$store.getters['authenticationModule/isAdmin']
    }
  },
  methods: {
    logoutUser () {
      this.$store.dispatch('authenticationModule/logout')
    }
  }
}
</script>

<style scoped>
  /* .navbar .nav-link {
    color: #fff !important;
  } */

  .navbar .nav-flex-icons {
    flex-direction: row;
  }
  /* .navbar.bg-white .nav-link {
    color: black !important;
  } */

  .navbar-light .navbar-brand, .navbar-light .navbar-brand:focus, .navbar-light .navbar-brand:hover {
    color: rgba(0,0,0,.9);
  }

  /* navbar-light bg-light */

  .navbar.navbar-dark .breadcrumb .nav-item.active>.nav-link, .navbar.navbar-dark .navbar-nav .nav-item.active>.nav-link {
    background-color: rgba(255,255,255,0.1);
  }

  .navbar.navbar-dark .breadcrumb .nav-item .nav-link, .navbar.navbar-dark .navbar-nav .nav-item .nav-link {
    color: #fff;
    transition: .35s;
  }
  .navbar-dark .navbar-nav .active>.nav-link, .navbar-dark .navbar-nav .nav-link.active, .navbar-dark .navbar-nav .nav-link.show, .navbar-dark .navbar-nav .show>.nav-link {
      color: #fff;
  }
  .navbar .nav-item .nav-link {
      display: block;
  }
  .navbar-dark .navbar-nav .nav-link {
      color: rgba(255,255,255,.5);
  }

  @media (min-width: 600px) {
    .navbar.scrolling-navbar {
      padding-top: 12px;
      padding-bottom: 12px;
      transition: background 0.5s ease-in-out,padding 0.5s ease-in-out;
    }
  } 
</style>
