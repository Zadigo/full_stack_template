<template>
<section :id="sectionId">
  <header>
    <!-- Jumbotron -->
    <div id="intro" class="p-5 text-center bg-light">
      <h1 class="mb-3 font-weight-bold">{{ pageTitle }}</h1>
      <p class="font-weight-bold">
        {{ pageDescription }}
      </p>
    </div>
  </header>

  <slot></slot>
</section>
</template>

<script>
export default {
  name: 'BaseJumbotron',
  props: {
    sectionId: {
      type: String,
      required: true
    },
    pageTitle: {
      type: String,
      required: true
    },
    pageDescription: {
      type: String,
      required: true
    }
  }
}
</script>
