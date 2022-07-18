import { createRouter, createWebHistory } from 'vue-router'
import { loadView } from '@/utils'

const routes = [
    {
        path: '/506',
        name: 'not_authorized',
        component: loadView('NotAuthorized')
    },
    {
        path: '/404',
        name: 'not_found',
        alias: '*',
        component: loadView('NotFound')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
    scrollBehavior () {
        window.scrollTop(0, 0)
    }
})

router.beforeEach((to, from, next) => {
    next()
})

export default router
