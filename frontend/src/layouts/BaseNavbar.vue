<template>
  <nav :class="[scrollY > 20 ? 'bg-light navbar-light' : 'navbar-dark shadow-none']" class="navbar navbar-expand-lg d-lg-block fixed-top">
    <div class="container">
      <!-- Brand -->
      <router-link :to="{ name: 'home_view' }" class="navbar-brand text-uppercase fw-bold">
        Some company
      </router-link>

      <!-- Toggle -->
      <button class="navbar-toggler" type="button" aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
        <i class="fas fa-bars"></i>
      </button>

      <!-- Links -->
      <div id="navbarExample01" class="collapse navbar-collapse">
        <transition name="spread" mode="out-in">
          <div v-if="showSearch">
            <input type="search" class="form-control" placeholder="Search">
          </div>
  
          <div v-else>
            <router-link :to="{ name: 'pricing_view' }" type="button" class="btn btn-transparent shadow-none px-3">
              Pricing
            </router-link>
          </div>
        </transition>

        <div class="ms-auto d-flex align-items-center">
          <button type="button" class="btn btn-transparent shadow-none px-3" @click="showSearch=!showSearch">
            <font-awesome-icon icon="fa-solid fa-search" />
          </button>

          <button type="button" class="btn btn-transparent shadow-none px-3">
            <font-awesome-icon icon="fa-solid fa-user" />
          </button>

          <button type="button" class="btn btn-transparent shadow-none px-3 me-2">
            <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
          </button>

          <button type="button" class="btn btn-primary">
            Signup
          </button>
        </div>
      </div>

      <!-- <ul class="navbar-nav ms-auto my-2 my-lg-0">
          <li v-for="link in links" :key="link.id" class="nav-item">
            <router-link :id="link.name" :to="{ name: link.name }" class="nav-link" role="link">
              {{ link.title }}
            </router-link>
          </li>

          <li v-show="isAuthenticated" class="nav-item">
            <router-link id="profile" :to="{ name: 'home_view' }" class="nav-link" role="link">
              Profile
            </router-link>
          </li>

          <li v-show="!isAuthenticated" class="nav-item">
            <router-link id="signin" :to="{ name: 'home_view' }" class="nav-link" role="link">
              <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
            </router-link>
          </li>

          <li v-show="!isAuthenticated" class="nav-item">
            <router-link id="signup" :to="{ name: 'home_view' }" class="nav-link" role="link">
              Signup
            </router-link>
          </li>

          <li v-show="isAuthenticated" class="nav-item">
            <a id="logout" href class="nav-link" role="link" @click.prevent="logout">
              <font-awesome-icon icon="fa-solid fa-right-fom-bracket" />
            </a>
          </li>

          <li v-show="isAuthenticated && isAdmin" class="nav-item">
            <router-link id="admin" :to="{ name: 'home_view' }" class="nav-link" role="link">
              Admin
            </router-link>
          </li>
        </ul> -->

      <!-- Share -->
      <!-- <ul class="navbar-nav d-flex flex-row">
          <li v-for="social in companyDetails.socials" :key="social.id" class="nav-item me-3 me-lg-0">
            <a :href="social.link" class="nav-link" target="_blank" rel="noopener noreferrer nofollow">
              <i :class="social.icon"></i>
            </a>
          </li>
        </ul> -->
    </div>
  </nav>
</template>

<script>
import { mapActions, storeToRefs } from 'pinia'
import { useAuthentication } from '@/store/authentication'
import { useScroll } from '@vueuse/core'
import { ref } from 'vue'

export default {
  name: 'BaseNavbar',
  setup () {
    const store = useAuthentication()
    const { isAuthenticated, isAdmin } = storeToRefs(store)
    const target = ref(null)
    const { y } = useScroll(target)
    return {
      target,
      store,
      isAuthenticated,
      isAdmin,
      scrollY: y
    }
  },
  data() {
    return {
      showSearch: false,
      links: [
        { id: 1, name: 'home_view', title: 'Pricing', authentication: false, admin: false }
      ]
    }
  },
  mounted () {
    this.target = window.document
  },
  methods: {
    ...mapActions(useAuthentication, ['logoutUser']),
    
    async logout () {

    }
    // logoutUser() {
    //   // Logs out the user from the
    //   // current session
    //   this.$api.auth.logout()
    //   .then(() => {
    //     this.logout()
    //     this.$router.push({ name: 'home_view' })
    //   })
    //   .catch((error) => {
    //     console.error(error)
    //   })
    // }
  }
}
</script>

<!-- <style scoped>
  .navbar .nav-flex-icons {
    flex-direction: row;
  }

  .navbar-light .navbar-brand, .navbar-light .navbar-brand:focus, .navbar-light .navbar-brand:hover {
    color: rgba(0,0,0,.9);
  }

  .navbar.navbar-dark {
    background-color: transparent;
  }

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
</style> -->

<style scoped>
.spread-enter-active,
.spread-leave-active {
  transition: all .3s ease;
}
.spread-enter-from,
.spread-leave-to {
  opacity: 0;
  width: 0%;
}
.spread-enter-to,
.spread-leave-from {
  opacity: 1;
  width: 100%;
}
</style>
