<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        Blank
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 1</ion-title>
        </ion-toolbar>
      </ion-header>

      Something to write here
    </ion-content>
  </ion-page>
</template>

<script>
// import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue'
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue'

export default  {
  name: 'Home',
  components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage }
}
</script>
