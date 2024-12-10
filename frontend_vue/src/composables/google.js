
// function asyncTimeout (seconds) {
//   return new Promise(resolve => setTimeout(() => {
//       resolve()
//     }, seconds)
//   )
// }

// export default function useGoogleAuhentication (vueInstance, options = {}) {
//   let googleApi = null
//   // const isReady = ref(false)
  
//   const prompt = 'select_account'
  
//   const isAuthorized = ref(false)
//   // let authentifiedUser = {}
  
//   // computed('isLoaded', () => {
//   //   return googleApi.value !== null
//   // })
    
//   console.info(vueInstance)

//   function install () {
//     // Creates the Google authentication script
//     return new Promise((resolve) => {
//       const script = document.createElement('script')
//       script.src = 'https://apis.google.com/js/api.js'
//       document.querySelector('head').appendChild(script)
//       resolve()
//     })
//   }

//   function initialize (options) {
//     // Initializes the script above
//     return new Promise((resolve, reject) => {
//       try {
//         window.gapi.load('auth2', () => {
//           window.gapi.auth2.init(options)
//           resolve(window.gapi)
//         })
//       } catch {
//         reject(false)
//       }
//     })
//   }

//   async function load () {
//     // Entrypoint for loading authentication with Google
//     let defaultOptions = {
//       scope: 'profile email',
//       discoveryDocs: [
//         'https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'
//       ]
//     }
//     defaultOptions = Object.assign(defaultOptions, options)
//     defaultOptions.prompt = prompt

//     if (!defaultOptions.clientId) {
//       throw new Error('No client ID for Google authentication')
//     }

//     await install()

//     await asyncTimeout(1000)
//     const api = await initialize(defaultOptions)

//     console.log('Google api', api)
//     googleApi = api.auth2.getAuthInstance()
//     // isReady.value = true
//     isAuthorized.value = googleApi.isSignedIn.get()
//     console.log('Googlee instance', googleApi, isAuthorized.value)
//   }

//   // async function authenticate (accessToken) {
//   //   // Authenticates the user on the Google backend
//   //   // and then returns their infos
//   //   const client = new OAuth2Client('xxxxxxxxxxxxx.apps.googleusercontent.com')
//   //   const ticket = await client.verifyIdToken({
//   //     // idToken: inputs.accessToken,
//   //     idToken: accessToken,
//   //     audience: 'xxxxx.apps.googleusercontent.com'
//   //   })
//   //   const payload= ticket.getPayload()
//   //   authentifiedUser = payload
//   //   // console.log('Google payload is '+JSON.stringify(payload));
//   //   // const userid = payload.sub;
//   //   // let email = payload.email;
//   //   // let emailVerified = payload.email_verified;
//   //   // let name = payload.name;
//   //   // let pictureUrl = payload.picture;
//   // }

//   function signin (successCallback, errorCallback) {
//     // Used to signin a user, returns acces token
//     // used to authenticate the user and gets his info
//     return new Promise((resolve, reject) => {
//       if (!googleApi) {
//         errorCallback(false)
//         reject(false)
//       }

//       try {
//         const user = googleApi.signIn()
//         isAuthorized.value = googleApi.isSignedIn.get()
//         console.log('signin', googleApi, 'user', user)
//         successCallback(user)
//         resolve(user)
//       } catch (error) {
//         console.log('signin error', error)
//         errorCallback(false)
//         reject(false)
//       }
//     })
//   }

//   // async function logout (successCallback, errorCallback) {
//   //   return new Promise((resolve, reject) => {
//   //     try {
//   //       googleApi.value.signOut()
//   //       successCallback(true)
//   //       isAuthorized.value = false
//   //       resolve(true)
//   //     } catch (error) {
//   //       errorCallback(false)
//   //       reject(false)
//   //     }
//   //   })
//   // }

//   // async function authenticationCode (successCallback, errorCallback) {
//   //   return new Promise((resolve, reject) => {
//   //     if (!this.isLoaded) {
//   //       reject(false)
//   //     }

//   //     try {
//   //       const result = googleApi.value.grantOfflineAccess({ prompt: prompt })
//   //       successCallback(result.code)
//   //       resolve(result.code)
//   //     } catch (error) {
//   //       errorCallback(false)
//   //       reject(false)
//   //     }
//   //   })
//   // }

//   return {
//     // authentifiedUser,
//     isAuthorized,
//     load,
//     signin
//     // authenticate
//     // logout,
//     // signin,
//     // authenticationCode
//   }
// }






var googleAuth = (function () {
  function installClient () {
    var apiUrl = 'https://apis.google.com/js/api.js'
    return new Promise((resolve) => {
      var script = document.createElement('script')
      script.src = apiUrl
      script.onreadystatechange = script.onload = function () {
        if (!script.readyState || /loaded|complete/.test(script.readyState)) {
          setTimeout(function () {
            resolve()
          }, 500)
        }
      }
      document.getElementsByTagName('head')[0].appendChild(script)
    })
  }

  function initClient (config) {
    return new Promise((resolve) => {
      window.gapi.load('auth2', () => {
        window.gapi.auth2.init(config)
          .then(() => {
            resolve(window.gapi)
          })
      })
    })
  }

  function Auth () {
    if (!(this instanceof Auth))
    return new Auth()
    this.GoogleAuth = null /* window.gapi.auth2.getAuthInstance() */
    this.isAuthorized = false
    this.isInit = false
    this.prompt = null
    
    this.isLoaded = function () {
      /* eslint-disable */
      console.warn('isLoaded() will be deprecated. You can use "this.$gAuth.isInit"')
      return !!this.GoogleAuth
    }

    this.load = (config, prompt) => {
      installClient()
      .then(() => {
        return initClient(config)
      })
      .then((gapi) => {
        this.GoogleAuth = gapi.auth2.getAuthInstance()
        this.isInit = true
        this.prompt = prompt
        this.isAuthorized = this.GoogleAuth.isSignedIn.get()
      })
    }

    this.signIn = (successCallback, errorCallback) => {
      return new Promise((resolve, reject) => {
      if (!this.GoogleAuth) {
        if (typeof errorCallback === 'function') errorCallback(false)
        reject(false)
        return
      }
      this.GoogleAuth.signIn()
        .then(googleUser => {
        if (typeof successCallback === 'function') successCallback(googleUser)
          this.isAuthorized = this.GoogleAuth.isSignedIn.get()
          resolve(googleUser)
        })
        .catch(error => {
          if (typeof errorCallback === 'function') errorCallback(error)
          reject(error)
        })
      })
    }

    this.getAuthCode = (successCallback, errorCallback) => {
      return new Promise((resolve, reject) => {
      if (!this.GoogleAuth) {
        if (typeof errorCallback === 'function') errorCallback(false)
          reject(false)
        return
      }
      this.GoogleAuth.grantOfflineAccess({ prompt: this.prompt })
        .then(function (resp) {
        if (typeof successCallback === 'function') successCallback(resp.code)
          resolve(resp.code)
        })
        .catch(function (error) {
        if (typeof errorCallback === 'function') errorCallback(error)
          reject(error)
        })
      })
    }

    this.signOut = (successCallback, errorCallback) => {
      return new Promise((resolve, reject) => {
      if (!this.GoogleAuth) {
        if (typeof errorCallback === 'function') errorCallback(false)
          reject(false)
        return
      }
      this.GoogleAuth.signOut()
        .then(() => {
        if (typeof successCallback === 'function') successCallback()
          this.isAuthorized = false
          resolve(true)
        })
        .catch(error => {
        if (typeof errorCallback === 'function') errorCallback(error)
          reject(error)
        })
      })
    }
  }

  return new Auth()
})()

function installGoogleAuthPlugin(Vue, options) {
  //set config
  let GoogleAuthConfig = null
  let GoogleAuthDefaultConfig = { scope: 'profile email', discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'] }
  let prompt = 'select_account'
  if (typeof options === 'object') {
    GoogleAuthConfig = Object.assign(GoogleAuthDefaultConfig, options)
    if (options.scope) GoogleAuthConfig.scope = options.scope
    if (options.prompt) prompt = options.prompt
    if (!options.clientId) {
      console.warn('clientId is required')
    }
  } else {
    console.warn('invalid option type. Object type accepted only')
  }

  //Install Vue plugin
  Vue.gAuth = googleAuth
  Object.defineProperties(Vue.prototype, {
    $gAuth: {
      get: function () {
        return Vue.gAuth
      }
    }
  })
  Vue.gAuth.load(GoogleAuthConfig, prompt)
}

export default installGoogleAuthPlugin
