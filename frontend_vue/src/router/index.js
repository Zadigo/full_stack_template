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
        path: '/product',
        name: 'product_view',
        component: loadView('site/ProductView')
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
            },
            {
                path: 'verify',
                name: 'verify_view',
                components: {
                    content: loadView('site/auth/VerifyAccountView')
                }
            }
        ]
    },
    {
        path: '/profile',
        component: loadLayout('BaseProfile'),
        children: [
            {
                name: 'profile_index_view',
                path: '',
                meta: {
                    verboseName: 'Index',
                    requiresAuthentication: true
                },
                component: loadView('site/profile/IndexView')
            },
            {
                name: 'details_view',
                path: 'details',
                meta: {
                    verboseName: 'Details',
                    requiresAuthentication: true
                },
                component: loadView('site/profile/DetailsView')
            },
            {
                name: 'password_view',
                path: 'password',
                meta: {
                    verboseName: 'Password',
                    requiresAuthentication: true
                },
                component: loadView('site/profile/PasswordView')
            },
            {
                name: 'preferences_view',
                path: 'preferences',
                meta: {
                    verboseName: 'Preferences',
                    requiresAuthentication: true
                },
                component: loadView('site/profile/PreferencesView')
            },
            {
                name: 'addresses_view',
                path: 'addresses',
                meta: {
                    verboseName: 'Addresses',
                    requiresAuthentication: true
                },
                component: loadView('site/profile/AddressView')
            },
            {
                name: 'account_view',
                path: 'details',
                meta: {
                    verboseName: 'Account',
                    requiresAuthentication: false
                },
                component: loadView('site/profile/AccountView')
            }
        ]
    },
    {
        path: '/506',
        name: 'not_authorized_view',
        component: loadView('site/NotAuthorizedView')
    },
    {
        path: '/404',
        name: 'not_found_view',
        component: loadView('site/NotFoundView')
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
            next({ name: 'login_view' })
        }

        if (to.meta.requiresAdmin) {
            if (!store.isAdmin) {
                next({ name: 'not_authorized_view' })
            }
        }
    }
    next()
})

export default router
