import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginComponent from '@/components/Login.vue'
import SearchCustomersComponent from '@/components/SearchCustomers.vue'
import CreateCustomerComponent from '@/components/CreateCustomer.vue'
import ViewCustomerComponent from '@/components/ViewCustomer.vue'
import ViewSomeVideoComponent from '@/components/ViewSomeVideo.vue'

const routes = [
  { path: '/', component: LoginComponent },
  { path: '/search_customers', component: SearchCustomersComponent },
  { path: '/create_customer', component: CreateCustomerComponent },
  { path: '/view_customer', component: ViewCustomerComponent },
  { path: '/view_some_video', component: ViewSomeVideoComponent }
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes,
  linkActiveClass: "is-active"
})

export default router
