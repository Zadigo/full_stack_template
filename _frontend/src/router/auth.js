// Global components
import PageNavigation from '@/components/BaseNavigation.vue'
import PageFooter from '@/components/BaseFooter.vue'

// Profile
import Profile from '@/pages/Profile.vue'
import Subscriptions from '@/components/auth/profile/Subscriptions.vue'

// Registration
import RegistrationHero from '@/pages/RegistrationHero.vue'


var authRoutes = [
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
                    default: () => import(/* webpackChunkName: "registration" */ '@/components/auth/registration/Signin.vue')
                }
            },
            {
                name: 'signup',
                path: '/signup',
                components: {
                    default: () => import(/* webpackChunkName: "registration" */ '@/components/auth/registration/Signup.vue')
                }
            },
            {
                name: 'forgot',
                path: '/forgot-password',
                components: {
                    default: () => import(/* webpackChunkName: "registration" */ '@/components/auth/registration/Forgot.vue')
                }
            }
        ]
    },

    {
        path: '/profile',
        components: {
            nav: PageNavigation,
            default: Profile,
            footer: PageFooter
        },
        children: [
            {
                name: 'profile_overview',
                path: '/',
                components: {
                    default: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/Index.vue')
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
                    default: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/Details.vue')
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
                    default: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/Preferences.vue')
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
                    default: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/Password.vue')
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
                    default: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/Address.vue'),
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
                    default: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/Payments.vue')
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
                            content: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/SubscriptionPayment.vue')
                        },
                        meta: {
                            verboseName: 'Payment',
                            requiresAuthentication: true
                        },
                        props: true
                    }
                ]
            },
            {
                name: 'profile_account',
                path: 'account',
                components: {
                    default: () => import(/* webpackChunkName: "profile" */ '@/components/auth/profile/Account.vue')
                },
                meta: {
                    verboseName: 'Account',
                    requiresAuthentication: true
                }
            }
        ]
    },
]

export default authRoutes
