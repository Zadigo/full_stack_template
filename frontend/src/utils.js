var _ = require('lodash')

var incrementIdFromLast = (items) => {
    var lastItem = _.last(items)
    return lastItem == undefined ? 0 : lastItem.id + 1
}

export default {
    lastItemIdOf
}
