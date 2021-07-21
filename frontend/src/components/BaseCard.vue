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
  // cards on the application as once
  name: 'BaseCard'
}
</script>
