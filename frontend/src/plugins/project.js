// function someFunction () {
//     console.log('Hey')
// }


export default {
    install: (Vue, options) => {
        Vue.someClick = function () {
            console.log(options)
        }
    }
}
