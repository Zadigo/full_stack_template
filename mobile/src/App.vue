<template>
  <ion-app>
    <Sidebar />

    <ion-router-outlet name="main" />
  </ion-app>
</template>

<script>
import { IonApp, IonRouterOutlet } from '@ionic/vue'
import Sidebar from './components/Sidebar.vue'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App',
  components: {
    IonApp,
    IonRouterOutlet,
    Sidebar
  }
})
</script>
