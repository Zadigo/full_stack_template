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
      <button @click="$emit('validateAction', position)" class="btn btn-primary">
        <i class="fa fa-check mr-3"></i>
        Validate
      </button>
    </template>
  </b-card>
</template>

<script>
export default {
  props: {
    position: {
      type: Number,
      default: 0
    }
  }
}
</script>
