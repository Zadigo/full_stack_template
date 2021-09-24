<template>
  <div class="text-white">

    <h1 class="display-4 font-weight-bold mb-3">{{ lead }}</h1>
    <h5 class="mb-4">{{ description }}</h5>
    
    <!-- Call to action -->
    <router-link :to="{ name: 'signin' }" class="btn btn-outline-light btn-lg m-2" role="button" rel="nofollow">
      Start tutorial
    </router-link>
  
  </div>
</template>

<script>
export default {
  name: 'Intro',
  props: {
    lead: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    }
  },
  title () {
    return 'Home'
  },

  methods: {
    testFunction() {
      console.log('for testing')
    }
  }
}
</script>
