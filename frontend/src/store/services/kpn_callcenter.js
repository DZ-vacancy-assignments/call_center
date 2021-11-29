import axios from 'axios'

const state = {
  customerResults: {},
  customer: {},
  searchOptionsCustomers: [
    {
      label: 'address',
      code: 'zipCodeHouseNumber'
    },
    {
      label: 'email',
      code: 'email'
    },
    {
      label: 'telephone',
      code: 'telephoneNumber'
    }
  ],
  createSuccess: null,
  createError: {}
}

const getters = {}

const mutations = {
  setCustomerResults (state, payload) {
    state.customerResults = payload
  },
  setCustomer (state, customer) {
    state.customer = customer
  },
  setCreateSuccess (state, value) {
    state.createSuccess = value
  },
  setCreateError (state, data) {
    state.createError = data
  }
}

const actions = {
  searchCustomers (context, payload) {
    return axios.post('/api/customers/search/', payload)
      .then(response => {
        context.commit('setCustomerResults', response.data)
      })
      .catch(e => {
        console.log(e)
      })
  },
  getCustomer (context, userId) {
    return axios.get('/api/customers/' + userId)
      .then(response => { context.commit('setCustomer', response.data) })
      .catch(e => { console.log(e) })
  },
  createCustomer (context, newCustomer) {
    return axios.post('/api/customers/', newCustomer)
      .then(response => {
        console.log(response.data)
        context.commit('setCustomer', response.data)
        context.commit('setCreateSuccess', true)
      })
      .catch(e => {
        context.commit('setCreateSuccess', false)
        context.commit('setCreateError', e.response.data)
      })
  },
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
