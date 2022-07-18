import { createRouter, createWebHistory } from 'vue-router'
import { useAuthentication } from '@/store/autthentication'
import { loadView } from '@/utils'

const routes = [
    {
        path: '/506',
        name: 'not_authorized_view',
        component: loadView('site/NotAuthorized')
    },
    {
        path: '/404',
        name: 'not_found_view',
        alias: '*',
        component: loadView('site/NotFound')
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
    if (to.meta.requiresAuthentication) {
        const store = useAuthentication()
        
        if (!store.isAuthenticated) {
            next('login_view')
        }

        if (to.meta.requiresAdmin) {
            if (!store.isAdmin) {
                next('not_authorized_view')
            }
        }
    }
    next()
})

export default router
