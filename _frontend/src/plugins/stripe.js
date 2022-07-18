function createScript (url, callback) {
    // Creates the Stripe script dynamically

    let documentTag = document
    var tag = 'script'
    var object = documentTag.createElement(tag)
    var scriptTag = documentTag.getElementsByTagName(tag)[0]

    object.src = '//' + url
    if (callback) { 
        object.addEventListener('load', function (e) { 
                callback(null, e)
            }, false
        )
    }
    scriptTag.parentNode.insertBefore(object, scriptTag)
}

// function configureStripe () {
//     this.stripe = Stripe(this.stripeAPIToken)

//     this.elements = this.stripe.elements()
//     this.card = this.elements.create('card')

//     this.card.mount('#card-element')
// }

export default {
    install: function (Vue, options) {
        console.log(options)
        Vue.runStripe = createScript
    }
}
