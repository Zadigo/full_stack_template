import { createRouter, createWebHistory } from 'vue-router'
import { useAuthentication } from '@/store/authentication'
import { loadLayout, loadView } from '@/utils'

const routes = [
    {
        path: '/',
        name: 'home_view',
        component: loadView('site/HomeView')
    },
    {
        path: '/contact-us',
        name: 'contact_us_view',
        component: loadView('site/ContactView')
    },
    {
        path: '/jobs',
        name: 'jobs_view',
        component: loadView('site/JobsView')
    },
    {
        path: '/pricing',
        name: 'pricing_view',
        component: loadView('site/PricingView')
    },
    {
        path: '/press',
        name: 'press_view',
        component: loadView('site/PressView')
    },
    {
        path: '/accounts',
        component: loadLayout('BaseRegistration'),
        children: [
            {
                path: 'login',
                name: 'login_view',
                components: {
                    content: loadView('site/auth/LoginView')
                }
            },
            {
                path: 'signup',
                name: 'signup_view',
                components: {
                    content: loadView('site/auth/SignupView')
                }
            },
            {
                path: 'forgot-password',
                name: 'forgot_passoword_view',
                components: {
                    content: loadView('site/auth/ForgotPasswordView')
                }
            }
        ]
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
