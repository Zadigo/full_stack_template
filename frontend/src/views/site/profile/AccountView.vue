<template>
  <section id="account">
    <base-validation-card-vue>
      <p class="fw-light">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla sed, aliquid debitis nemo aspernatur
        veniam itaque iusto! Excepturi laudantium commodi cupiditate, delectus repudiandae
        suscipit, quis quidem odio nostrum rem nam?
      </p>

      <template #cardFooter>
        <footer class="card-footer">
          <button type="button" class="btn btn-sm btn-danger" @click="deleteAccount">
            Delete account
          </button>
        </footer>
      </template>
    </base-validation-card-vue>
  </section>
</template>

<script>
import useAuthenticationComposable from '@/composables/authentication'
import BaseValidationCardVue from '@/layouts/BaseValidationCard.vue'

export default {
  name: 'AccountView',
  components: {
    BaseValidationCardVue
  },
  setup () {
    const store = useAuthenticationComposable()
    return {
      store
    }
  },
  title() {
    return 'Account'
  },
  methods: {
    async deleteAccount () {
      
    }
  }
}
</script>
