<template>
  <div class="container">
    <section class="section mt-4">
      <div class="row">
        <!-- Sidebar -->
        <div class="col-sm-12 col-md-3 offset-md-2">
          <aside role="navigation">
            <base-card>
              <b-list-group>
                <b-list-group-item v-for="link in sideBarLinks" :key="link.id" :to="{ name: link.link }">
                  {{ link.name }}
                </b-list-group-item>
              </b-list-group>
            </base-card>
          </aside>
        </div>

        <!-- Content -->
        <div class="col-5">
          <router-view />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
var _ = require('lodash')

import { mapState } from 'vuex'

export default {
  name: 'Profile',

  data() {
    return {
      sideBarLinks: []
    }
  },
  
  beforeMount() {
    // Gather all the links related to the user profile dynamically
    var routesForProfile = _.find(this.$router.options.routes, ['path', '/profile'])
    _.forEach(routesForProfile.children, (route, index) => {
      this.sideBarLinks.push({ id: index, link: route.name, name: route.meta.verboseName })
    })
  },
  
  mounted() {
    if (!this.hasUserDetails) {
      this.$api.profile.getUserDetails()
      .then((response) => {
        console.log(response.data)
        this.$store.commit('profileModule/updateUserDetails', response.data)
      })
      .catch((error) => {
        console.error(error)
      })
    }
  },

  computed: {
    ...mapState('profileModule', [
      'hasUserDetails'
    ])
  }

  // _checkCredentials () {
  //   var { email, password } = this.credentials
  //   if (!this._validateEmail(email)) {
  //     console.log('Email is not valid')
  //   }
  //   password
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
