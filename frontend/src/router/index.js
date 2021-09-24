import Vue from 'vue'
import Router from 'vue-router'
import store from '../stores'

// Routes
import globalRoutes from './global'
import authRoutes from './auth'
import adminRoutes from './admin'
// import Press from './pages/Press.vue'

Vue.use(Router)

const routes = [
    ...globalRoutes,
    ...authRoutes,
    ...adminRoutes,

    {
        path: '/506',
        name: 'not_authorized',
        component: () => import('@/pages/NotAuthorized.vue')
    },

    {
        path: '/404',
        name: 'not_found',
        alias: '*',
        component: () => import('@/pages/NotFound.vue')
    }
]

var router = new Router({
    mode: 'history',
    routes: routes,
    scrollBehavior() {
        return { x: 0, y: 0 }
    }
})

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
            next({ name: 'signin', query: { next: to.fullPath } })
        }
    } else {
        next()
    }
})

export default router
