<template>
  <ion-page>
    <base-tab-header />

    <ion-content :fullscreen="true" class="ion-padding">

      <ion-list>
        <ion-item @click="goTo(tech)" v-for="tech in techs" :key="tech.title">
          <ion-icon :name="tech.icon" slot="sart"></ion-icon>
          <ion-label>{{ tech.title }}</ion-label>
        </ion-item>
      </ion-list>

    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonContent, IonList, IonItem, IonIcon, IonLabel } from '@ionic/vue';
import BaseTabHeader from '../components/BaseTabHeader.vue'

export default  {
  name: 'Tab3',
  components: { BaseTabHeader, IonContent, IonPage, IonList, IonItem, IonIcon, IonLabel },

  data () {
    return {
      techs: [
        {
          'title': 'Angular',
          'icon': 'angular',
          'description': 'A powerful Javascript framework for building single page apps. Angular is open source, and maintained by Google.',
          'color': '#E63135'
        },
        {
          'title': 'CSS3',
          'icon': 'css3',
          'description': 'The latest version of cascading stylesheets - the styling language of the web!',
          'color': '#0CA9EA'
        },
      ]
    }
  },

  methods: {
    goTo () {
      this.$router.push({ name: 'profile' })
    }
  }
}
</script>
