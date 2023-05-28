import Vue from 'vue'
import Vuex from 'vuex'

import auth from '@/store/modules/auth'
import call_center from '@/store/services/call_center'
import users from '@/store/services/users'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    auth,
    cc: call_center,
    users
  }
})

export default store
