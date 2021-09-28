<template>
  <ion-page>

    <ion-header>
      <h2>Login</h2>
    </ion-header>

    <ion-content>
      <div id="login">
        <ion-input v-model="email" placeholder="Email"></ion-input>
        <ion-input v-model="password" placeholder="Password"></ion-input>
        <ion-button @click="loginUser">Login</ion-button>
      </div>
    </ion-content>
  
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonContent, IonInput, IonButton } from '@ionic/vue'

export default {
  components: { IonPage, IonHeader, IonContent, IonInput, IonButton },
  data () {
    return {
      email: null,
      password: null
    }
  },

  methods: {
    loginUser () {
      
    }
  }
}
</script>
