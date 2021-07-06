import { createRouter, createWebHistory } from '@ionic/vue-router';
// import Tabs from '../views/Tabs.vue'
// import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    component: () => import('@/views/Home.vue')
    // redirect: '/tabs/tab1'
    // redirect: '/home'
  },
  // {
  //   path: '/home/',
  //   // component: Tabs,
  //   component: Home,
  //   children: [
  //     {
  //       path: '',
  //       redirect: 'produts'
  //     },
  //     {
  //       path: 'products',
  //       component: () => import('@/views/Products.vue')
  //     }
  //     // {
  //     //   path: '',
  //     //   redirect: '/tabs/tab1'
  //     // },
  //     // {
  //     //   path: 'tab1',
  //     //   component: () => import('@/views/Tab1.vue')
  //     // },
  //     // {
  //     //   path: 'tab2',
  //     //   component: () => import('@/views/Tab2.vue')
  //     // },
  //     // {
  //     //   path: 'tab3',
  //     //   component: () => import('@/views/Tab3.vue')
  //     // }
  //   ]
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
