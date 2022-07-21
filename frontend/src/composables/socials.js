import { computed, ref } from 'vue'

function asyncTimeout (seconds) {
  return new Promise(resolve => setTimeout(() => {
      resolve()
    }, seconds)
  )
}

export default function useGoogleAuhentication (vueInstance, options = {}) {
  console.log(vueInstance)
  const googleApi = ref(null)
  // const isReady = ref(false)

  const apiUrl = 'https://apis.google.com/js/api.js'
  const isAuthorized = ref(false)
  const prompt = 'select_account'
  // const config = null

  computed('isLoaded', () => {
    return googleApi.value !== null
  })
  
  function install () {
    return new Promise((resolve) => {
      const script = document.createElement('script')
      script.src = apiUrl
      document.querySelector('head').appendChild(script)
      resolve()
    })
  }

  function initialize (options) {
    return new Promise((resolve, reject) => {
      try {
        window.gapi.load('auth2', () => {
          window.gapi.auth2.init(options)
          resolve(window.gapi)
        })
      } catch {
        reject(false)
      }
    })
  }

  async function load () {
    let defaultOptions = {
      scope: 'profile email',
      discoveryDocs: [
        'https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'
      ]
    }
    defaultOptions = Object.assign(defaultOptions, options)
    defaultOptions.prompt = prompt

    if (!defaultOptions.clientId) {
      throw new Error('No client ID for Google authentication')
    }

    await install()

    await asyncTimeout(1000)
    const api = await initialize(defaultOptions)

    console.log('Google api', api)
    googleApi.value = api.auth2.getAuthInstance()
    // isReady.value = true
    isAuthorized.value = googleApi.value.isSignedIn.get()
    console.log('Googlee instance', googleApi, isAuthorized.value)
  }

  // function signin (successCallback, errorCallback) {
  //   return new Promise((resolve, reject) => {
  //     if (!googleApi.value) {
  //       errorCallback(false)
  //       reject(false)
  //     }

  //     try {
  //       const user = googleApi.value.signin()
  //       isAuthorized.value = googleApi.value.isSignedIn.get()
  //       successCallback(user)
  //       resolve(user)
  //     } catch (error) {
  //       errorCallback(false)
  //       reject(false)
  //     }

  //   })
  // }

  // async function logout (successCallback, errorCallback) {
  //   return new Promise((resolve, reject) => {
  //     try {
  //       googleApi.value.signOut()
  //       successCallback(true)
  //       isAuthorized.value = false
  //       resolve(true)
  //     } catch (error) {
  //       errorCallback(false)
  //       reject(false)
  //     }
  //   })
  // }

  // async function authenticationCode (successCallback, errorCallback) {
  //   return new Promise((resolve, reject) => {
  //     if (!this.isLoaded) {
  //       reject(false)
  //     }

  //     try {
  //       const result = googleApi.value.grantOfflineAccess({ prompt: prompt })
  //       successCallback(result.code)
  //       resolve(result.code)
  //     } catch (error) {
  //       errorCallback(false)
  //       reject(false)
  //     }
  //   })
  // }

  return {
    googleApi,
    load
    // logout,
    // signin,
    // authenticationCode
  }
}
