import { defineStore } from 'pinia'

const useSubscriptions = defineStore('subscriptions', {
  state: () => ({
    currentSubscription: {},
    selectedSubscription: {}
  }),
  actions: {
    chooseSubscription (subscription) {
      this.selectedSubscription = subscription
    }
  },
  getters: {
    hasSubscription () {
      // return lengthOfDict(state.currentSubscription) > 0
      return false
    },
    hasSelectedSubscription () {
      // return lengthOfDict(state.selectedSubscription) > 0
      return false
    }
  }
})

export {
  useSubscriptions
}
