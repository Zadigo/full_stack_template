// Hero
import Home from '@/pages/Home.vue'

// Global components
import PageNavigation from '@/components/BaseNavigation.vue'
import PageFooter from '@/components/BaseFooter.vue'

// Legal
import Legal from '@/pages/Legal.vue'

// About
import AboutUs from '@/pages/AboutUs.vue'
import Payment from '@/pages/Payment.vue'
import Contact from '@/pages/Contact.vue'

var globalRoutes = [
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
                    nav: PageNavigation,
                    default: () => import(/* webpackChunkName: "home" */ '@/components/hero/Intro.vue'),
                    footer: PageFooter
                }
            }
        ]
    },

    {
        path: '/pricing',
        name: 'pricing',
        components: {
            nav: PageNavigation,
            default: () => import(/* webpackChunkName: "pricing" */ '@/pages/Pricing.vue'),
            footer: PageFooter
        }
    },
    {
        path: '/payment',
        name: 'payment',
        component: Payment,
        meta: {
            requiresAuthentication: true
        }
    },
    {
        name: 'about',
        path: '/about-us',
        components: {
            nav: PageNavigation,
            default: AboutUs,
            footer: PageFooter
        }
    },
    {
        name: 'jobs',
        path: '/jobs',
        components: {
            nav: PageNavigation,
            default: () => import(/* webpackChunkName: "jobs" */ '@/pages/Jobs.vue'),
            footer: PageFooter
        }
    },
    {
        name: 'contact',
        path: '/contact-us',
        components: {
            nav: PageNavigation,
            default: Contact,
            footer: PageFooter
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
                    default: () => import(/* webpackChunkName: "legal" */ '@/components/legal/TermsOfConditions.vue')
                },
                meta: {
                    verboseName: 'Terms of condition'
                }
            },
            {
                name: 'terms_of_use',
                path: 'terms-of-use',
                components: {
                    default: () => import(/* webpackChunkName: "legal" */ '@/components/legal/TermsOfUse.vue')
                },
                meta: {
                    verboseName: 'Terms of use'
                }
            }
        ]
    }
]

export default globalRoutes
