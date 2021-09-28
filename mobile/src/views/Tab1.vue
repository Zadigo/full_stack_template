<template>
  <ion-page>
    <!-- Toolbar -->
    <base-tab-header />
    
    <ion-content :fullscreen="true">
      
    </ion-content>

  </ion-page>
</template>

<script>
import { IonPage, IonContent } from '@ionic/vue'
import { personCircle, ellipsisHorizontal, ellipsisVertical } from 'ionicons/icons'
import BaseTabHeader from '../components/BaseTabHeader.vue'

export default  {
  name: 'Tab1',
  components: { BaseTabHeader, IonContent, IonPage },
  
  setup () {
    return { personCircle, ellipsisHorizontal, ellipsisVertical }
  }
}
</script>
