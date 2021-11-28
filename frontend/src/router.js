import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginComponent from '@/components/LoginComponent.vue'
import SearchCustomersComponent from '@/components/SearchCustomersComponent.vue'
import CreateCustomerComponent from '@/components/CreateCustomerComponent.vue'

const routes = [
  { path: '/', component: LoginComponent },
  { path: '/search_customers', component: SearchCustomersComponent },
  { path: '/create_customer', component: CreateCustomerComponent }
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
