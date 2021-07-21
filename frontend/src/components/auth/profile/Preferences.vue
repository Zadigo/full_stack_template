<template>
  <div class="card">
    <div class="card-body">
      <b-list-group>
        <b-list-group-item>
          <b-form-checkbox @change="updatePreferences" v-model="userOptions['newsletter']" id="newsletter">
            <span class="m-2">I would like to get updates related to newsletters</span>
          </b-form-checkbox>
        </b-list-group-item>

        <b-list-group-item>
          <b-form-checkbox v-model="userOptions['another']"  id="another">
            <span class="m-2">I would like to get updates related to newsletters</span>
          </b-form-checkbox>
        </b-list-group-item>

        <b-list-group-item>
          <b-form-checkbox v-model="userOptions['other']" id="other">
            <span class="m-2">I would like to get updates related to newsletters</span>
          </b-form-checkbox>
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Preferences',
  
  title() {
    return 'Preferences'
  },

  data() {
    return {
      userOptions: {}
    }
  },

  methods: {
    updatePreferences() {
      this.$api.profile.updatePreferences(this.userOptions)
      .then((response => {
        console.log(response)
        this.$buefy.snackbar.open({
          message: 'Yellow button and positioned on top, click to close',
          type: 'is-warning',
          position: 'is-top',
          duration: 3500,
          
          // onAction: () => {
          //   this.$buefy.toast.open({
          //       message: 'Action pressed',
          //       queue: false
          //   })
          // }
        })
      }))
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
