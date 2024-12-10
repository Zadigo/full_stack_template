<template>
  <div class="card">
    <div class="card-body">
      <div class="list-group">
        <div class="list-group-item">
          <base-checkbox-vue id="newsletter" label="I would like to get updates related to newsletters" />
        </div>

        <div class="list-group-item">
          <base-checkbox-vue id="another" label="I would like to get updates related to newsletters" />
        </div>

        <div class="list-group-item">
          <base-checkbox-vue id="another2" label="I would like to get updates related to newsletters" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BaseCheckboxVue from '@/layouts/BaseCheckbox.vue'

export default {
  name: 'PreferencesView',
  components: {
    BaseCheckboxVue
  },
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
      
    }
  }
}
</script>
