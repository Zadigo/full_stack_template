<template>
  <div class="card">
    <!-- Header -->
    <slot name="cardHeader"></slot>

    <!-- Content -->
    <div class="card-content">
      <slot></slot>
    </div>

    <!-- Footer -->
    <slot name="cardFooter"></slot>
  </div>
</template>

<script>
export default {
  // A base card in order to unify all the
  // cards on the application at once
  name: 'BaseCard'
}
</script>
