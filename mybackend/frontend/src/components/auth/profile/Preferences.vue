<template>
  <div class="card">
    <div class="card-body">
      <b-list-group>
        <b-list-group-item>
          <b-form-checkbox id="newsletter" v-model="userOptions['newsletter']">
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
  }
}
</script>
