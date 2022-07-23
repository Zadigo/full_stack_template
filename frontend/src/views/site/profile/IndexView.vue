<template>
  <section>
    <div class="row">
      <div class="col-12">
        <base-card>
          <h2>Welcome <strong>{{ firstName }},</strong></h2>
        </base-card>
      </div>

      <div class="col-12">
        <div class="card">
          <div class="card-content">
            <img :src="require('@/assets/hello.svg')" class="img-fluid" alt="overview" role="img" aria-label="Account overview">
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// import { useAuthentication } from '@/store/authentication'
// import { mapState } from 'pinia'

export default {
  name: 'IndexSection',
  computed: {
    // ...mapState(useAuthentication, {
    //   firstName: (state) => {
    //     return state.userDetails.myuser.firstname
    //   }
    // })
  }
}
</script>
