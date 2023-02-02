import { ref, watch } from 'vue'
import { Buffer } from 'buffer'

function parseJwt (token) {
    const base64Url = token.split('.')[1]
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
    const tokens = Buffer.from(base64, 'base64').toString().split('')
    const result = decodeURIComponent(tokens.map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
    }))
    const jsonPayload = result.join('')
    return JSON.parse(jsonPayload)
}
// https://developers.google.com/identity/gsi/web/reference/js-reference#auto_select
// Content-Security-Policy-Report-Only: script-src https://accounts.google.com/gsi/client; frame-src https://accounts.google.com/gsi/; connect-src https://accounts.google.com/gsi/;
export default function useGoogleAuhentication (options = {}) {
  const authentifiedUser = ref(null)
  
  watch(authentifiedUser, (current) => {
    return current !== null
  })

  function install () {
    return new Promise((resolve, reject) => {
      try {
        const script = document.createElement('script')
        
        script.src = 'https://accounts.google.com/gsi/client'
        script.attributes.setNamedItem(document.createAttribute('async'))
        script.attributes.setNamedItem(document.createAttribute('defer'))

        document.querySelector('head').appendChild(script)
        resolve(true)
      } catch {
        console.warn('Could not create Google signin script')
        reject(false)
      }
    })
  }

  function completeSignin (response) {
    const { credential } = response
    authentifiedUser.value = parseJwt(credential)
    // console.log(parseJwt(credential))
  }

  function initialize () {
    window.google.accounts.id.initialize({
      client_id: options.clientId || process.env.VUE_APP_GOOGLE_CLIENT_ID,
      callback: completeSignin
      // auto_select: false
      // login_uri: 'https://www.example.com/login'
      // native_callback:
      // cancel_on_tap_outside: true
      // prompt_parent_id: 'parent_id'
      // nonce: 'zienfoz'
      // context: 'signin'
      // state_cookie_domain: 'example.com'
      // ux_mode: popup / redirect
      // allowed_parent_origin: ['https://example.com']
      // intermediate_iframe_close_callback:
      // itp_support: true
    })

    window.google.accounts.id.renderButton(
        document.querySelector('#google-button'),
        {
          theme: 'outline',
          size: 'large'
        }
    )
    // window.google.accounts.id.prompt()
  }

  async function load () {
    const result = await install()
    if (result) {
      window.addEventListener('load', initialize)
    }
  }

  return {
    authentifiedUser,
    load,
    completeSignin
  }
}
