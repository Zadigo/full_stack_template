// A mixin that implements some functionalities
// for getting the fields for a form present
// in the fields.json file

var _ = require('lodash')
import fields from '../data/fields.json'

export default {
    // computed: {
    //     fields() {
    //         var formFieldsFor = this.formFieldsFor
    //         if (!_.isUndefined(formFieldsFor)) {
    //             var nonIndexedFields = fields[formFieldsFor]
    //             _.forEach(nonIndexedFields, (field, index) => {
    //                 field['id'] = index
    //             })
    //             return nonIndexedFields
    //         }
    //         return []
    //     }
    // },
    methods: {
        getFieldsFor(name) {
            var nonIndexedFields =  fields[name]
            _.forEach(nonIndexedFields, (field, index) => {
                field['id'] = index
            })
            return nonIndexedFields
        }
    }
}
