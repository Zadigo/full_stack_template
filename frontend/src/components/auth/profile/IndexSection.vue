<template>
  <section>
    <div class="row">
      <div class="col-12">
        <base-card>
          <h2>Welcome <strong>{{ firstName }},</strong></h2>
        </base-card>
      </div>
      
      <div class="col-12">
        <base-card class="mt-2">
          <img src="../../../assets/hello.svg" class="img-fluid" alt="overview" role="img" aria-label="Account overview">
        </base-card>
      </div>
    </div>
  </section>
</template>

<script>
import { useAuthentication } from '@/store/autthentication'
import { mapState } from 'pinia'

export default {
  name: 'IndexSection',
  computed: {
    ...mapState(useAuthentication, {
      firstName: (state) => {
        return state.userDetails.myuser.firstname
      }
    })
  }
}
</script>
