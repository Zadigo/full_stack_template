<template>
  <header>
    <Navbar />
    
    <keep-alive>
      <Sidebar :links="sideBarLinks" />
    </keep-alive>
  </header>
</template>

<script>
  import Navbar from '@/components/admin/nav/Navbar.vue'
  import Sidebar from '@/components/admin/nav/Sidebar.vue'

  export default {
    components: {
      Navbar,
      Sidebar
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
