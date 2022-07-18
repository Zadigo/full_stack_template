import { createRouter, createWebHistory } from 'vue-router'
import { useAuthentication } from '@/store/autthentication'
import { loadView } from '@/utils'

const routes = [
    {
        path: '/',
        name: 'home_view',
        component: loadView('site/HomeView')
    },
    {
        path: '/pricing',
        name: 'pricing_view',
        component: loadView('site/PricingView')
    },
    {
        path: '/login',
        name: 'login_view',
        component: loadView('site/LoginView')
    },
    {
        path: '/506',
        name: 'not_authorized_view',
        component: loadView('site/NotAuthorized')
    },
    {
        path: '/404',
        name: 'not_found_view',
        component: loadView('site/NotFound')
    },
    {
        path: '/:catchAll(.*)',
        redirect: '/404'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
    scrollBehavior () {
        window.scrollTo(0, 0)
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
