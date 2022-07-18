import { defineStore } from 'pinia'

const useAuthentication = defineStore('authentication', {
  state: () => ({

  }),

  getters: {
    isAuthenticated () {
      return true
    },
    isAdmin () {
      return true
    }
  }
})

export {
  useAuthentication
}
