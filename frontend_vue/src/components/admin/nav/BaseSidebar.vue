<template>
  <div class="sidebar-fixed position-fixed">
    <a class="logo-wrapper waves-effect">
      <img :src="sideBarLogo" class="img-fluid" :alt="sideBarImageAlt">
    </a>

    <div class="list-group list-group-flush">
      <router-link v-for="link in links" :key="link.id" :to="{ name: link.name }" class="list-group-item list-group-item-action waves-effect" role="link">
        <i :class="link.icon" class="mr-3"></i>
        {{ link.title }}
      </router-link>
    </div>
  </div>
</template>

<script>
  // import _ from 'lodash'
  
  export default {
    props: {
      links: {
        type: Array,
        required: true
      },
      sideBarLogo: {
        type: String,
        default: 'https://mdbootstrap.com/img/logo/mdb-email.png'
      },
      sideBarImageAlt: {
        type: String,
        default: 'Dashboard'
      }
    },
    // methods: {
    //   makeActive (link) {
    //     _.forEach(this.$props.links, (item) => {
    //       item.active = false
    //     })
    //     link.active = true
    //   }
    // }
  }
</script>

<style scoped>
  .sidebar-fixed {
    height: 100vh;
    width: 270px;
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
    z-index: 1050;
    background-color: #fff;
    padding: 0 1.5rem 1.5rem;
  }
  .position-fixed {
    position: fixed!important;
  }
  .sidebar-fixed .list-group .router-link-exact-active {
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
    border-radius: 5px;
  }
  .sidebar-fixed .logo-wrapper {
    padding: 2.5rem;
  }
  .list-group-item.router-link-exact-active {
    z-index: 2;
    color: #fff;
    background-color: #007bff;
    border-color: #007bff;
  }
  .list-group-item {
    padding: .75rem 1.25rem;
    margin-bottom: -1px;
    background-color: #fff;
    border: 1px solid rgba(0,0,0,.125);
  }
</style>
