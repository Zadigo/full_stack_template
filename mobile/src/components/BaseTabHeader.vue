<template>
  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-menu-button menu="sidebar"></ion-menu-button>
      </ion-buttons>

      <ion-buttons slot="end">
        <ion-button>
          <ion-icon slot="icon-only" :icon="personCircle"></ion-icon>
        </ion-button>
      </ion-buttons>

      <ion-title>Zara</ion-title>
    </ion-toolbar>
  </ion-header>
</template>

<script>
import { IonHeader, IonToolbar, IonButtons, IonButton, IonMenuButton, IonIcon, IonTitle } from '@ionic/vue'
import { personCircle } from 'ionicons/icons'

export default {
  name: 'BaseTabHeader',
  components: { IonHeader, IonToolbar, IonButtons, IonButton, IonMenuButton, IonIcon, IonTitle },
  setup () {
    return { personCircle }
  }
}
</script>
