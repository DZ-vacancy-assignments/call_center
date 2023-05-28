<template>
  <div class="center">
    <h1 class="page-title">&nbsp;WELCOME TO <span class="brand-name">MCK</span> CALL CENTER&nbsp</h1>
    <div class="login-form">
      <article
        v-if="warningMessage"
        class="message is-warning"
      >
        <div class="message-body">{{ warningMessage }}</div>
      </article>
      <div class="field-email">
        <label>Email</label>
        <input
          class="input is-normal"
          type="email"
          v-model="email"
          @keydown.enter="login()"
          placeholder="email"
        />
      </div>
      <div class="field-password">
        <label>Password</label>
        <input
          class="input is-normal"
          type="password"
          v-model="password"
          @keydown.enter="login()"
          placeholder="password"
        />
      </div>
      <div>
        <button
          class="button"
          @click="login();"
        >Login
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      email: 'firstcreateduser@user.co',
      password: 'testOK99%1',
      warningMessage: '',
    };
  },
  methods: {
    login: function() {
      let payload = {'email': this.email, 'password': this.password}
      this.$store.dispatch('auth/postLogin', payload)
      .then(() => {
        if (this.$store.state.auth.authError) {
          this.warningMessage = "Login was not successful."
        } else {
          this.$store.dispatch('auth/getProfile')
          .then(() => {
            if (this.$store.state.auth.loggedIn) {
              this.$router.push('/search_customers/')
            }
          })
        }
      })
      return
    }
  },
  created: function() {
    this.$store.dispatch('auth/getProfile')
    .then(() => {
      if (this.$store.state.auth.loggedIn) {
        this.$router.push('/search_customers/')
      }
    })
    return
  }
};
</script>

<style lang="scss" scoped>
@import '../assets/css/login.css';
</style>
