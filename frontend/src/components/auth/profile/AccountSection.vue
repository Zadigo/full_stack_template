<template>
  <section id="account">
    <base-card>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla sed, aliquid debitis nemo aspernatur
        veniam itaque iusto! Excepturi laudantium commodi cupiditate, delectus repudiandae
        suscipit, quis quidem odio nostrum rem nam?
      </p>

      <template v-slot:cardFooter>
        <footer class="card-footer bg-white">
          <button type="button" class="btn btn-sm btn-danger" @click="deleteAccount">
            Delete account
          </button>
        </footer>
      </template>
    </base-card>
  </section>
</template>

<script>
export default {
  name: 'AccountSection',
  title() {
    return 'Account'
  },
  
  methods: {
    deleteAccount() {
      
    }
  }
}
</script>
