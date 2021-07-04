var _ = require('lodash')

function authenticationFields () {
    var fields = []
    const fieldNames = ['email', 'password']
    _.forEach(fieldNames, (name, index) => {
        fields.push(
            { id: index, type: name, name: name, id: name, placeholder: '' }
        )
    })
    return fields
}


function signupFields () {
    const baseFields = authenticationFields()
    var passwordField = baseFields.pop()
    var passwordField1 = {...passwordField}
    var passwordField2 = {...passwordField}

    passwordField1['name'] = 'password1'
    passwordField1['id'] = 'password1'
    passwordField2['name'] = 'password2'
    passwordField2['id'] = 'password2'
    baseFields.push([passwordField1, passwordField2])

    const fieldNames = ['firstname', 'lastname']
    _.forEach(fieldNames, (name) => {
        if (name === 'firstname' | name == 'lastname') {
            baseFields.unshift(
                { id: index, type: 'text', name: name, id: name, placeholder: '' }
            )
        } else {
            baseFields.push(
                { id: index, type: 'text', name: name, id: name, placeholder: '' }
            )
        }
    })
}


export default {
    authenticationFields,
    signupFields
}
