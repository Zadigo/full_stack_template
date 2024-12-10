<template>
  <header>
    <base-navbar />
    
    <keep-alive>
      <base-sidebar :links="sideBarLinks" />
    </keep-alive>
  </header>
</template>

<script>
import BaseNavbar from '@/components/admin/nav/BaseNavbar.vue'
import BaseSidebar from '@/components/admin/nav/BaseSidebar.vue'

export default {
  name: 'BaseHeader',
  components: {
    BaseNavbar,
    BaseSidebar
  },
  data() {
    return {
      sideBarLinks: [
        { id: 1, name: 'admin_home', title: 'Home', icon: 'fas fa-chart-pie', active: true },
        { id: 2, name: 'admin_products', title: 'Products', icon: 'fas fa-table', active: false },
        { id: 3, name: 'admin_settings', title: 'Settings', icon: 'fa fa-cog', active: false },
      ]
    }
  }
}
</script>
