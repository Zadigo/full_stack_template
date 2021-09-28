<template>
  <ion-page>
    <!-- Toolbar -->
    <base-tab-header />
    
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 2</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <ExploreContainer name="Tab 2 page" />
    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue'
import ExploreContainer from '@/components/ExploreContainer.vue'
import BaseTabHeader from '../components/BaseTabHeader.vue'

export default  {
  name: 'Tab2',
  components: { BaseTabHeader, ExploreContainer, IonHeader, IonToolbar, IonTitle, IonContent, IonPage }
}
</script>
