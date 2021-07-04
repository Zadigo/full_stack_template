function pageTitle (vm) {
    const { title } = vm.$options
    if (title) {
        return typeof title === 'function' ? title.call(vm) : title
    }
}

export default {
    created () {
        const title = pageTitle(this)
        if (title) {
            document.title = `${ title } - ${ this.companyDetails.name }`
        }
    }
}
