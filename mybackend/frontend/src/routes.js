import Vue from 'vue'
import Router from 'vue-router'
import store from './stores'

// Global components
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

// Admin
import Admin from './pages/Admin.vue'
import Index from './components/admin/Index.vue'
import Products from './components/admin/Products.vue'
import Product from './components/admin/Product.vue'
import Create from './components/admin/Create.vue'
import Settings from './components/admin/Settings.vue'
import AdminNav from './components/admin/nav/Header.vue'
import AdminFooter from './components/admin/nav/Footer.vue'

// Hero
import Home from './pages/Home.vue'

// Registration
import RegistrationHero from './pages/RegistrationHero.vue'

// Profile
import Profile from './pages/Profile.vue'
import Subscriptions from './components/auth/profile/Subscriptions.vue'

// Legal
import Legal from './pages/Legal.vue'
import TermsOfConditions from './components/legal/TermsOfConditions.vue'
import TermsOfUse from './components/legal/TermsOfUse.vue'

// About
import AboutUs from './pages/AboutUs.vue'
import Payment from './pages/Payment.vue'
import Contact from './pages/Contact.vue'
// import Press from './pages/Press.vue'


Vue.use(Router)


const routes = [
    {
        path: '/',
        components: {
            default: Home,
        },
        children: [
            {
                name: 'home',
                path: '/',
                components: {
                    nav: Navbar,
                    default: () => import('./components/hero/Intro.vue'),
                    footer: Footer
                }
            }
        ]
    },

    {
        path: '/',
        components: {
            default: RegistrationHero
        },
        children: [
            {
                name: 'signin',
                path: '/signin',
                components: {
                    default: () => import('./components/auth/registration/Signin.vue')
                }
            },
            {
                name: 'signup',
                path: '/signup',
                components: {
                    default: () => import('./components/auth/registration/Signup.vue')
                }
            },
            {
                name: 'forgot',
                path: '/forgot-password',
                components: {
                    default: () => import('./components/auth/registration/Forgot.vue')
                }
            }
        ]
    },

    {
        path: '/pricing',
        name: 'pricing',
        components: {
            nav: Navbar,
            default: () => import('./pages/Pricing.vue'),
            footer: Footer
        }
    },
    {
        path: '/payment',
        name: 'payment',
        component: Payment,
        meta: {
            requiresAuthentication: true
        }
        // beforeEnter: (to, from, next) {

        // }
    },
    {
        name: 'about',
        path: '/about-us',
        components: {
            nav: Navbar,
            default: AboutUs,
            footer: Footer
        }
    },
    {
        name: 'jobs',
        path: '/jobs',
        components: {
            nav: Navbar,
            default: () => import('./pages/Jobs.vue'),
            footer: Footer
        }
    },
    {
        name: 'contact',
        path: '/contact-us',
        components: {
            nav: Navbar,
            default: Contact,
            footer: Footer
        }
    },

    {
        path: '/legal',
        components: {
            default: Legal
        },
        children: [
            {
                name: 'terms_of_condition',
                path: 'terms-of-condition',
                components: {
                    default: TermsOfConditions
                },
                meta: {
                    verboseName: 'Terms of condition'
                }
            },
            {
                name: 'terms_of_use',
                path: 'terms-of-use',
                components: {
                    default: TermsOfUse
                },
                meta: {
                    verboseName: 'Terms of use'
                }
            }
        ]
    },

    // Routes for /profile

    {
        path: '/profile',
        components: {
            nav: Navbar,
            default: Profile,
            footer: Footer
        },
        children: [
            {
                name: 'profile_overview',
                path: '/',
                components: {
                    default: () => import('./components/auth/profile/Index.vue')
                },
                meta: {
                    verboseName: 'Home',
                    requiresAuthentication: true
                }
            },
            {
                name: 'profile_details',
                path: 'details',
                components: {
                    default: () => import('./components/auth/profile/Details.vue')
                },
                meta: {
                    verboseName: 'Details',
                    requiresAuthentication: true
                }
            },
            {
                name: 'profile_preferences',
                path: 'preferences',
                components: {
                    default: () => import('./components/auth/profile/Preferences.vue')
                },
                meta: {
                    verboseName: 'Preferences',
                    requiresAuthentication: true
                }
            },
            {
                name: 'profile_passwords',
                path: 'password',
                components: {
                    default: () => import('./components/auth/profile/Password.vue')
                },
                meta: {
                    verboseName: 'Passwords',
                    requiresAuthentication: true
                }
            },
            {
                name: 'profile_addresses',
                path: 'addresses',
                components: {
                    default: () => import('./components/auth/profile/Address.vue'),
                },
                meta: {
                    verboseName: 'Addresses',
                    requiresAuthentication: true
                }
            },
            {
                name: 'profile_payments',
                path: 'payments',
                components: {
                    default: () => import('./components/auth/profile/Payments.vue')
                },
                meta: {
                    verboseName: 'Payments',
                    requiresAuthentication: true
                }
            },
            {
                name: 'profile_subscriptions',
                path: 'subscriptions',
                components: {
                    default: Subscriptions,
                },
                meta: {
                    verboseName: 'Subscription',
                    requiresAuthentication: true
                },
                children: [
                    {
                        name: 'profile_subscription_payment',
                        path: 'payment',
                        components: {
                            content: () => import('./components/auth/profile/SubscriptionPayment.vue')
                        },
                        meta: {
                            verboseName: 'Payment',
                            requiresAuthentication: true
                        }
                    }
                ]
            },
            {
                name: 'profile_account',
                path: 'account',
                components: {
                    default: () => import('./components/auth/profile/Account.vue')
                },
                meta: {
                    verboseName: 'Account',
                    requiresAuthentication: true
                }
            }
        ]
    },

    {
        path: '/admin',
        component: Admin,
        meta: {
            requiresAuthentication: true,
            requiresAdmin: true,
            requiresStaff: true
        },
        children: [
            {
                name: 'admin_home',
                path: '/',
                components: {
                    default: Index,
                    nav: AdminNav,
                    footer: AdminFooter
                }
            },
            {
                name: 'admin_products',
                path: 'products',
                components: {
                    default: Products,
                    nav: AdminNav,
                    footer: AdminFooter
                },
            },
            {
                name: 'admin_product',
                path: 'products/:id(\\d)',
                components: {
                    default: Product,
                    nav: AdminNav,
                    footer: AdminFooter
                }
            },
            {
                name: 'admin_product_create',
                path: 'create',
                components: {
                    default: Create,
                    nav: AdminNav,
                    footer: AdminFooter
                }
            },
            {
                name: 'admin_settings',
                path: 'settings',
                components: {
                    default: Settings,
                    nav: AdminNav,
                    footer: AdminFooter
                }
            }
        ]
    },

    {
        path: '/506',
        name: 'not_authorized',
        component: () => import('./pages/NotAuthorized.vue')
    },

    {
        path: '/404',
        name: 'not_found',
        alias: '*',
        component: () => import('./pages/NotFound.vue')
    }
]

var router = new Router({
    mode: 'history',
    routes: routes
})

export default router

router.beforeEach((to, from, next) => {
    // Checks for user authentication
    if (to.meta['requiresAuthentication']) {
        if (store.getters['authenticationModule/isAuthenticated']) {
            // Checks that those who want to access the admin
            // have the required admin flag set to true
            if (to.name.includes('admin')) {
                var isAdmin = store.getters['authenticationModule/isAdmin']
                if (!isAdmin) {
                    next('not_authorized')
                }
            }
            next()
        } else {
            next('signin')
        }
    } else {
        next()
    }
})
