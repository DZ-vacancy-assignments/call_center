<template>
  <div class="container">
    <h1>WELCOME TO KPN CALL CENTER</h1>
    <p align="center">
      <img src="https://i.imgur.com/SA8cjs8.png">
    </p>
    <div>I'm in the LoginComponent.vue.</div>
    <div>
      <input
        v-model="email"
        @keydown.enter="login()"
        placeholder="email"
      />
    </div>
    <div>
      <input
        v-model="password"
        @keydown.enter="login()"
        placeholder="password"
      />
    </div>
    <div>
      <button @click="login();">login</button>
      <div>Login state: {{ $store.state.auth.loggedIn }}.</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginComponent',
  data() {
    return {
      email: 'firstcreateduser@user.com',
      password: 'testOK99%1',
    };
  },
  methods: {
    login: function() {
      let payload = {'email': this.email, 'password': this.password}
      this.$store.dispatch('auth/postLogin', payload)
      .then(() => {
        this.$store.dispatch('auth/getProfile')
        .then(() => {
          if (this.$store.state.auth.loggedIn) {
            this.$router.push('/home/')
          }
        })
      })
      return
    }
  },
  created: function() {
    this.$store.dispatch('auth/getProfile')
    .then(() => {
      if (this.$store.state.auth.loggedIn) {
        this.$router.push('/home/')
      }
    })
  }
};
</script>

<style lang="scss" scoped>
  h1 {
    text-align: center;
  }
</style>
