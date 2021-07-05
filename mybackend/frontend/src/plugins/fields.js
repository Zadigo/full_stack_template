import { isUndefined } from 'lodash'

var _ = require('lodash')

function createField(type, name, autocomplete) {
    // A simple function to create a form field
    if (isUndefined(type)) { type = 'text' }
    // Auto create the placeholder for the field
    placeholder = name.charAt(0).toUpperCase() + name.slice(1)
    return { type: type, name: name, autocomplete: autocomplete, placeholder: placeholder }
}

function reIndex(fields) {
    // Reindex the fields so that fields that were
    // added afterwards do not create an issue
    _.forEach(fields, (field, index) => {
        field[id] = index
    })
    return fields
}


function loginFields() {
    // A function for returning login fields
    return [
        { id: 1, type: 'text', name: 'email', autocomplete: 'current-email', placeholder: null },
        { id: 2, type: 'password', name: 'password', autocomplete: 'current-password', placeholder: null },
    ]
}


function signUpFields() {
    // A function for returning signup fields
    var fields = loginFields()
    var additionnalFields = [
        { id: 1, type: 'text', name: 'firstname', autocomplete: '', placeholder: null },
        { id: 2, type: 'text', name: 'lastname', autocomplete: '', placeholder: null },
        { id: 3, type: 'password', name: 'password1', autocomplete: 'new-password', placeholder: null },
        { id: 4, type: 'password', name: 'password2', autocomplete: 'new-password', placeholder: null },
    ]
    return reIndex(fields.concat(additionnalFields))
}


function buildFieldsFromDatabase(data, names, types) {
    // A set of data retrieved from the database,
    // quickly create a set of fields to be used
    // in a given form
    var newFields = []
    _.forEach(Object.keys(data), (key, index) => {
        var field = createField(types[index], names[index], null)
        newFields.push(field)
    })
    return reIndex(newFields)
}


export default {
    install: function (Vue) {
        Vue.prototype.$forms = function () {
            loginFields = loginFields
            signUpFields = signUpFields
        }
        Vue.createField = createField
        Vue.fieldsFromDatabase = buildFieldsFromDatabase
    }
}
buildFieldsFromDatabase()
