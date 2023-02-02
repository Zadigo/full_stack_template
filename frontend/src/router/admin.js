// Admin
import Admin from '@/pages/Admin.vue'
import Index from '@/components/admin/Index.vue'
// import Products from '@/components/admin/Products.vue'
import Product from '@/components/admin/Product.vue'
import Create from '@/components/admin/Create.vue'
import Settings from '@/components/admin/Settings.vue'
import AdminNav from '@/components/admin/nav/Header.vue'
import AdminFooter from '@/components/admin/nav/Footer.vue'

var adminRoutes = [
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
                path: '/products',
                components: {
                    nav: AdminNav,
                    default: () => import(/* webchunkPackName "products" */ '@/components/admin/Products.vue'),
                    footer: AdminFooter
                },
            },
            {
                name: 'admin_product',
                path: '/products/:id(\\d+)',
                components: {
                    nav: AdminNav,
                    default: Product,
                    footer: AdminFooter
                }
            },
            {
                name: 'admin_product_create',
                path: '/create',
                components: {
                    default: Create,
                    nav: AdminNav,
                    footer: AdminFooter
                }
            },
            {
                name: 'admin_settings',
                path: '/settings',
                components: {
                    default: Settings,
                    nav: AdminNav,
                    footer: AdminFooter
                }
            }
        ]
    }
]

export default adminRoutes
