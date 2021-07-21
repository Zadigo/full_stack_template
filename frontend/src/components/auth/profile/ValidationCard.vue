<template>
  <b-card>
    <b-card-body>
      <div class="row">
        <div class="col-12">
          <slot></slot>
        </div>
      </div>
    </b-card-body>

    <template class="bg-white text-right" #footer>
      <button @click="$emit('validateAction', position)" class="btn btn-primary mr-2">
        <font-awesome-icon icon="check"></font-awesome-icon>
        Validate
      </button>
    </template>
  </b-card>
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
