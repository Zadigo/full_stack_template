<template>
  <div class="col-sm-12 col-md-3">
    <p class="fw-bold text-light text-uppercase">
      {{ section.title }}
    </p>

    <ul class="p-0">
<<<<<<< HEAD
      <li v-for="(link, index) in section.links" :key="index">
        <router-link :to="{ name: link.path }" :aria-labelledby="link.name" role="link">
=======
      <li v-for="link in section.links" :key="link.id">
        <router-link :to="{ name: link.path }" :aria-labelledby="link.name" class="text-light" role="link">
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
          {{ link.name }}  
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'PageFooterColumn',
  props: {
    section: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
  .page-footer ul {
    list-style: none;
  }

  .page-footer ul li {
    margin-bottom: .5rem;
  }

  .page-footer ul li a {
    /* color: #b2b2b2 !important; */
    text-decoration: none;
  }

  .page-footer-light {
    color: white;
  }
  .page-footer-light a,
  .page-footer-light i {
    color: white;
  }
</style>
