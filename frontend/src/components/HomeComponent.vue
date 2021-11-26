<template>
  <div class="container">
    <h1>Welcome {{ $store.state.auth.profile.full_name }}</h1>
    <h1>Welcome {{ $store.state.auth.profile.email }}</h1>
    <h2>This is the home screen.</h2>
    <div>I'm in the HomeComponent.vue.</div>
      <button @click="logout();">logout</button>
      <div>Login state: {{ $store.state.auth.loggedIn }}.</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeComponent',
  data() {
    return {};
  },
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
        return
  }
};
</script>

<style lang="scss" scoped>
  h1 {
    text-align: center;
  }
</style>

