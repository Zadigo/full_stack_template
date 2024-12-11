import { createRouter, createWebHistory } from 'vue-router'
 
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: async () => import('../layouts/BaseSite.vue'),
            children: [
                {
                    path: '',
                    name: 'home',
                    component: async () => import('../pages/HomePage.vue')
                }
            ]
        }
    ]
})

export default router
