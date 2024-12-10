<template>
  <div class="card mb-4 wow fadeIn">
    <div class="card-body d-sm-flex justify-content-between">
      <h4 class="mb-2 mb-sm-0 pt-1">
        <router-link :to="{ name: homePageLink }">{{ homePageName }}</router-link>
        <span>/</span>
        <span>{{ currentPageName }}</span>
      </h4>

      <form class="d-flex justify-content-center" @submit.prevent>
        <input v-model="searchedItem" type="search" placeholder="Search" aria-label="Search" class="form-control">
        <button type="submit" class="btn btn-primary btn-sm my-0 p waves-effect waves-light" @click="doSearch">
          <i class="fas fa-search"></i>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'PageHeader',
    props: {
      homePageName: {
        type: String,
        required: true
      },
      currentPageName: {
        type: String,
        required: true
      },
      homePageLink: {
        type: String,
        default: 'admin_home'
      }
    },
    emits: {
      'do-search': (value) => value
    },
    data() {
      return {
        searchedItem: null
      }
    },
    methods: {
      doSearch() {
        // this.$router.goTo('search', { q: this.search })
        // this.$router.push({ name: 'search', query: { q: this.search } })
        this.$emit('do-search', this.searchedItem)
      }
    }
  }
</script>
