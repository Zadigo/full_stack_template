<template>
  <p>
    By providing your information you agree to our
    <router-link :to="{ name: 'home_view' }" class="fw-bold">
      Privacy policy
    </router-link>
  </p>
</template>

<script>
export default {
  name: 'BasePrivacyText'
}
</script>
