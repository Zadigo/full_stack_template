<template>
  <base-card>

    <b-list-group>
      <b-list-group-item>
        <b-form-checkbox id="newsletter" v-model="userOptions['newsletter']" @change="updatePreferences">
          <span class="m-2">I would like to get updates related to newsletters</span>
        </b-form-checkbox>
      </b-list-group-item>

      <b-list-group-item>
        <b-form-checkbox id="another" v-model="userOptions['another']">
          <span class="m-2">I would like to get updates related to newsletters</span>
        </b-form-checkbox>
      </b-list-group-item>

      <b-list-group-item>
        <b-form-checkbox id="other" v-model="userOptions['other']">
          <span class="m-2">I would like to get updates related to newsletters</span>
        </b-form-checkbox>
      </b-list-group-item>
    </b-list-group>

  </base-card>
</template>

<script>
export default {
  name: 'PreferencesSection',
  title() {
    return 'Preferences'
  },
  data() {
    return {
      userOptions: {}
    }
  },
  methods: {
    async updatePreferences() {
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
