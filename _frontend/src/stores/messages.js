import { isUndefined } from 'lodash'

var _ = require('lodash')

var notificationsModule = {
    state: () => ({
        messages: []
    }),

    mutations: {
        hideMessage(state) {
            return (id) => {
                var messageId = _.findIndex(state.messages, ['id', id])
                state.messages.splice(0, messageId)
            }
        },

        clearMessages(state) {
            // Clears the current stack
            // of messages in order to
            // prevent stale messages to be
            // constantly displayed
            state.messages = []
        },

        addMessage(state, message) {
            // Adds a message to the stack. A message
            // should be like the following:
            // { type: 'alert-danger', app: 'auth', content: null, title: null }
            var lastMessage = _.last(state.messages)
            if (isUndefined(lastMessage)) {
                message['id'] = 0
            } else {
                message['id'] = lastMessage.id + 1
            }
            state.messages.push(message)
        }
    },

    getters: {
        getMessagesFor(state) {
            return (name) => {
                return _.filter(state.messages, ['app', name])
            }
        }
    },
    
    actions: {
        newDangerMessage({ commit }, message) {
            message['type'] = 'alert-danger'
            commit('clearMessages')
            commit('addMessage', message)
        },

        newSuccessMessage({ commit }, message) {
            message['type'] = 'alert-success'
            commit('clearMessages')
            commit('addMessage', message)
        }
    }
}

export default notificationsModule
