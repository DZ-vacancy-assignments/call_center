import axios from 'axios'

const state = {
  customerResults: {},
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
  ]
}

const getters = {}

const mutations = {
  setCustomerResults (state, payload) {
    state.customerResults = payload
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
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
