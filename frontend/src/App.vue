<template lang="html">
<div>
  <nav v-if="$store.state.auth.loggedIn" class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <span class="navbar-item">
        <h1 class="nav-title"><span class="brand-name">KPN</span> CALL CENTER</h1>
      </span>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/search_customers">Search Customers</router-link>
        <router-link class="navbar-item" to="/create_customer">Create Customer</router-link>
        <router-link class="navbar-item" to="/list_products">List Products</router-link>
        <router-link class="navbar-item" to="/create_product">Create Product</router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a @click="logout();" class="button is-light">
              Logout
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
  <div>
    <h1 v-if="$store.state.auth.loggedIn" class="title">Welcome {{ $store.state.auth.profile.full_name }}</h1>
  </div>
  <router-view/>
</div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    logout: function() {
      this.$store.dispatch('auth/logout')
      .then(() => {
        if (!this.$store.state.auth.loggedIn) {
          this.$router.push('/')
        }
      })
      return
    }
  },
  created: function() {
    this.$store.dispatch('auth/getProfile')
    .then(() => {
      if (!this.$store.state.auth.loggedIn) {
        this.$router.push('/')
      }
    })
  }
}
</script>

<style lang="scss" scoped>
@import './assets/css/main.css';
</style>
