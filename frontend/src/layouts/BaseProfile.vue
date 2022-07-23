<template>
  <section id="profile" class="my-5">
    <base-navbar-vue />

    <div class="container">
      <section class="section mt-4">
        <div class="row">
          <!-- Sidebar -->
          <div class="col-sm-12 col-md-3 offset-md-2">
            <aside role="navigation">
              <keep-alive>
                <div class="card">
                  <div class="card-body">
                    <div class="list-group">
                      <router-link v-for="item in sidebarLinks" :key="item.id" :to="{ name: item.link }" class="list-group-item">
                        {{ item.name }}
                      </router-link>
                    </div>
                  </div>
                </div>  
              </keep-alive>
            </aside>
          </div>
  
          <!-- Content -->
          <div class="col-sm-12 col-md-5">
            <router-view />
          </div>
        </div>
      </section>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'

import { useAuthentication } from '@/store/authentication'
import { storeToRefs } from 'pinia'
import BaseNavbarVue from './BaseNavbar.vue'

export default {
  name: 'ProfileView',
  components: {
    BaseNavbarVue
  },
  setup () {
    const store = useAuthentication()
    const { user } = storeToRefs(store)
    return {
      store,
      user
    }
  },
  data() {
    return {
      sidebarLinks: []
    }
  },
  beforeMount() {
    // Gather all the links related to the user profile dynamically
    const routesForProfile = _.find(this.$router.options.routes, ['path', '/profile'])
    _.forEach(routesForProfile.children, (route, index) => {
      this.sidebarLinks.push({ id: index, link: route.name, name: route.meta.verboseName })
    })
  },
  // mounted () {
  //   this.getUserProfile()
  // },
  // methods: {
  //   async getUserProfile () {
  //     if (!this.hasUserDetails) {
  //       this.$api.profile.getUserDetails()
  //       .then((response) => {
  //         this.$store.commit('profileModule/updateUserDetails', response.data)
  //       })
  //       .catch((error) => {
  //         console.error(error)
  //       })
  //     }
  //   }
  // }
}
</script>

<style scoped>
  .list-group-item+.list-group-item.router-link-exact-active {
    margin-top: -1px;
    border-top-width: 1px;
  }
  
  .list-group-item.router-link-exact-active {
    z-index: 2;
    color: #fff;
    background-color: #007bff;
    border-color: #007bff;
  }
</style>
