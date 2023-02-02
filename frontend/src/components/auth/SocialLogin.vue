<template>
  <div class="socials">
    <div class="col-12">
      <div id="google-button"></div>
    </div>
  </div>
</template>

<script>
import useGoogleAuthentication from '../../composables/socials'
import { getCurrentInstance } from 'vue'

export default {
  name: 'SocialLogin',
  setup () {
    console.info(process.env)
    const instance = getCurrentInstance()
    const { load } = useGoogleAuthentication(instance, { clientId: '' })
    return {
      load
    }
  }
}
</script>
