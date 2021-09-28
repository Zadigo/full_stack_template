var _ = require('lodash')

var incrementIdFromLast = (items) => {
    var lastItem = _.last(items)
    return lastItem == undefined ? 0 : lastItem.id + 1
}


var lengthOfDict = (item) => {
    // Returns the current length
    // of a given dictionnary
    if (_.isUndefined(item)) {
        return 0
    }
    return Object.keys(item).length
}


export {
    incrementIdFromLast,
    lengthOfDict
}
