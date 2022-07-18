// import { setupDevtools } from "../devtools"
import functions from './functions'

/**
 * Standard function for creating a product
 * standardized for Google Analytics
 * 
 * @param {String|Number} id - Product ID
 * @param {String} name - Product name
 * @param {String|Number} price - Product price
 * @param {String} brand - Brand related to the product
 * @param {String} category - Product category
 * @param {String|Number} index - Product's position in the list
 */
function createProduct (id, name, price, brand, category, index) {
    return {
        item_id: id,
        item_name: name,
        price: price,
        item_brand: brand,
        item_category: category,
        index: index
    }
}

/**
 * Map the fields from incoming products
 * to a different name example: 
 * {price: 15} > unit_price > {unit_price: 15}
 * 
 * @param {Array} products - List of products
 * @param {Object} mapping - Fields to map to a new name
 * @return Products with a new field name
 */
function mapToFields (products, mapping) {
    return products.map((product) => {
        var entries = Object.entries(mapping)
        var newItems = {}

        entries.forEach((entry) => {
            newItems[entry[1]] = product[entry[0]]
        })

        return newItems
    })
}

function createGoogleAnalytics (tag, options) {
    const { currency, brand } = options
    
    functions.DEFAULT_CURRENCY = currency || functions.DEFAULT_CURRENCY
    functions.DEFAULT_BRAND = brand

    const head = document.querySelector('head')

    // Create the no script tag
    const noScript = document.createElement('script')
    const srcAttribute = document.createAttribute('src')
    const url = new URL('https://www.googletagmanager.com/gtag/js')

    url.searchParams.append('id', tag)
    srcAttribute.value = url.toString()

    const asyncAttribute = document.createAttribute('async')
    noScript.setAttributeNode(srcAttribute)
    noScript.setAttributeNode(asyncAttribute)

    const script = document.createElement('script')
    const content = document.createTextNode(`
    window.dataLayer = window.dataLayer || []
    function gtag() { dataLayer.push(arguments) }
    gtag('js', 1 * new Date())
    gtag('config', '${ tag }', { currency: '${ functions.DEFAULT_CURRENCY }' })`)

    script.appendChild(content)

    // additionalProperties.forEach((property) => {
    //     var textObject = document.createTextNode(`gtag('config', '${property}', { currency: '${functions.DEFAULT_CURRENCY}' })`)
    //     script.appendChild(textObject)
    // })

    head.appendChild(script)
    script.parentNode.insertBefore(noScript, script)

    return {
        install: (app) => {
            app.config.globalProperties.$analytics = {
                google: functions
            }

            window.VueAnalytics = {
                google: functions
            }
        }
    }
}

/**
 * Creates a composable for components
 */
function useAnalytics () {
    // pass
}

export {
    createProduct,
    createGoogleAnalytics,
    mapToFields,
    useAnalytics
}
