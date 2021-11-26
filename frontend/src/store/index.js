import Vue from 'vue'
import Vuex from 'vuex'

import auth from '@/store/modules/auth'
import kpn_callcenter from '@/store/services/kpn_callcenter'
import users from '@/store/services/users'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    auth,
    kcc: kpn_callcenter,
    users
  }
})

export default store
