<template>
  <div>
    <!-- Header -->
    <PageHeader homePageName="Dashboard" currentPageName="Index" />
    
    <div class="card">
      <div class="card-body">
        <!-- <line-chart :chartData="{ labels: ['Jan', 'Feb'], datasets: [{ label: 'Kendall', data: [40, 20] }] }" :options="{ responsive: true, maintainAspectRatio: false }" /> -->
      </div>
    </div>
  </div>
</template>

<script>
import PageHeader from './nav/PageHeader.vue'

export default {
  name: 'Index',
  title () {
    return 'Index - Dashboard'
  },
  components: {
    // 'base-admin': Base,
    PageHeader,
    // 'line-chart': Line
  }
}
</script>
