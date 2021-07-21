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
          <button @click="deleteAccount" class="btn btn-sm btn-danger">
            Delete account
          </button>
        </footer>
      </template>
    </base-card>
  </section>
</template>

<script>
export default {
  name: 'Account',
  title() {
    return 'Account'
  },
  
  methods: {
    deleteAccount() {
      
    }
  }
}
</script>
