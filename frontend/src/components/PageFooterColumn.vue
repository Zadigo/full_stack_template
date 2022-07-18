<template>
  <div class="col-sm-12 col-md-3">
    <p class="fw-bold text-light text-uppercase">
      {{ section.title }}
    </p>

    <ul class="p-0">
      <li v-for="link in section.links" :key="link.id">
        <router-link :to="{ name: link.path }" :aria-labelledby="link.name" class="text-light" role="link">
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
