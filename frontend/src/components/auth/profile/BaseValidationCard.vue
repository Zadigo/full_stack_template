<template>
  <div class="card">
    <slot name="cardHeader"></slot>

    <div class="card-content">
      <div class="row">
        <div class="col-12">
          <slot></slot>
        </div>
      </div>
    </div>

    <footer class="card-footer bg-white text-right">
      <button @click="$emit('validateAction', position)" class="btn btn-primary mr-2">
        <font-awesome-icon icon="check"></font-awesome-icon>
        Validate
      </button>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'ValidationCard',
  props: {
    position: {
      type: Number,
      default: 0
    }
  }
}
</script>
