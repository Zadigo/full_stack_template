<template>
  <section class="section" id="account">
    <b-card>
      <b-card-body>
        Something here
      </b-card-body>
    </b-card>

    <b-card class="mt-2">
      <b-card-body>
        <b-card-body>
          <b-card-text>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla sed, aliquid debitis nemo aspernatur 
            veniam itaque iusto! Excepturi laudantium commodi cupiditate, delectus repudiandae 
            suscipit, quis quidem odio nostrum rem nam?
          </b-card-text>
        </b-card-body>

        <b-card-footer>
          <button @click="testMethod" class="btn btn-sm btn-danger">Delete account</button>
        </b-card-footer>
      </b-card-body>
    </b-card>
  </section>
</template>

<script>
var axios = require('axios')

export default {
  name: 'Account',
  title() {
    return 'Account'
  },
  
  methods: {
    testMethod() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/test',
        data: { username: 'Kendall' },
        responseType: 'json',
        headers: {
          'Authorization': `Token ${this.$store.getters['authenticationModule/getToken']}`,
          'Content-Type': 'application/json'
        },
        withCredentials: true
      })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
