<template lang="html">
<div>
  <nav v-if="$store.state.auth.loggedIn" class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <span class="navbar-item">
        <h1 class="nav-title"><span class="brand-name">MCK</span> CALL CENTER</h1>
      </span>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-router-link" to="/search_customers">
          <div class="navbar-item">Search Customers</div>
        </router-link>
        <router-link class="navbar-router-link" to="/create_customer">
          <div class="navbar-item">Create Customer</div>
        </router-link>
        <router-link class="navbar-router-link" event="" to="/list_products">
          <div class="navbar-item disabled">List Products</div>
        </router-link>
        <router-link class="navbar-router-link" event="" to="/create_product">
          <div class="navbar-item disabled">Create Product</div>
        </router-link>
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
