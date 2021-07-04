function productClick() {

}

function collectionView() {

}

function addToCart() {

}

function removeFromCart() {

}

function cartView(cart, step) {
    if (typeof step !== 'number') {
        console.error('Step should be a number')
        return false
    } else {

    }
}


export default {
    install: function (Vue, options) {
        Vue.productClick = productClick
        Vue.collectionView = collectionView
        Vue.addToCart = addToCart
        Vue.removeFromCart = removeFromCart
        Vue.cartView = cartView
    }
}
