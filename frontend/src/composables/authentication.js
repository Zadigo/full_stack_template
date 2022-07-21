import { client } from '@/plugins/axios'
import { ref } from 'vue'

export default function useAuthenticationComposable () {
  const authenticationErrors = ref([])
  const responseData = ref({})
  const loginCredentials = ref({
    email: null,
    password: null
  })
  
  const signupCredentials = ref({
    username: null,
    firstname: null,
    lastname: null,
    email: null,
    password1: null,
    password2: null
  })

  const forgotPasswordCredentials = ref({
    email: null
  })

  function passwordsValid () {
    return signupCredentials.value.password1 === signupCredentials.value.password2
  }

  async function login () {
    try {
      const response = client.post('/login', loginCredentials.value)
      responseData.value = response.daa
    } catch (error) {
      authenticationErrors.value.push({ type: 'danger', content: error.message})
    }
  }
  
  async function signup () {
    try {
      const response = client.post('/signup', signupCredentials.value)
      responseData.value = response.daa
    } catch (error) {
      authenticationErrors.value.push({ type: 'danger', content: error.message})
    }
  }

  return {
    responseData,
    authenticationErrors,
    loginCredentials,
    signupCredentials,
    forgotPasswordCredentials,
    login,
    signup,
    passwordsValid
  }
}
