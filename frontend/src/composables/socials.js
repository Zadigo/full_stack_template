import { ref } from 'vue'
import { OAuth2Client } from 'google-auth-library'

function asyncTimeout (seconds) {
  return new Promise(resolve => setTimeout(() => {
      resolve()
    }, seconds)
  )
}

export default function useGoogleAuhentication (vueInstance, options = {}) {
  let googleApi = null
  // const isReady = ref(false)
  
  const prompt = 'select_account'
  
  const isAuthorized = ref(false)
  let authentifiedUser = {}
  
  // computed('isLoaded', () => {
  //   return googleApi.value !== null
  // })
    
  console.info(vueInstance)

  function install () {
    // Creates the Google authentication script
    return new Promise((resolve) => {
      const script = document.createElement('script')
      script.src = 'https://apis.google.com/js/api.js'
      document.querySelector('head').appendChild(script)
      resolve()
    })
  }

  function initialize (options) {
    // Initializes the script above
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
    // Entrypoint for loading authentication with Google
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
    googleApi = api.auth2.getAuthInstance()
    // isReady.value = true
    isAuthorized.value = googleApi.isSignedIn.get()
    console.log('Googlee instance', googleApi, isAuthorized.value)
  }

  async function authenticate (accessToken) {
    // Authenticates the user on the Google backend
    // and then returns their infos
    const client = new OAuth2Client('xxxxxxxxxxxxx.apps.googleusercontent.com')
    const ticket = await client.verifyIdToken({
      // idToken: inputs.accessToken,
      idToken: accessToken,
      audience: 'xxxxx.apps.googleusercontent.com'
    })
    const payload= ticket.getPayload()
    authentifiedUser = payload
    // console.log('Google payload is '+JSON.stringify(payload));
    // const userid = payload.sub;
    // let email = payload.email;
    // let emailVerified = payload.email_verified;
    // let name = payload.name;
    // let pictureUrl = payload.picture;
  }

  // function signin (successCallback, errorCallback) {
  //   // Used to signin a user, returns acces token
  //   // used to authenticate the user and gets his info
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
    authentifiedUser,
    isAuthorized,
    load,
    authenticate
    // logout,
    // signin,
    // authenticationCode
  }
}
