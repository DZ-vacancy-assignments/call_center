<template>
  <div>
    <div class="container">
      <h1>Welcome {{ $store.state.auth.profile.full_name }}</h1>
      <h1>Welcome {{ $store.state.auth.profile.email }}</h1>
      <h2>This is the home screen.</h2>
      <div>I'm in the HomeComponent.vue.</div>
        <button @click="logout();">logout</button>
        <div>Login state: {{ $store.state.auth.loggedIn }}.</div>
      </div>
      <div class="work-area">
        <div class="search-v1">
          <span>
            <input
              v-model="ZipCode"
              @keydown.enter="search-v1"
              placeholder="zip code"
            />
          </span>
          <span>
            <input
              v-model="HouseNumber"
              @keydown.enter="search-v1"
              placeholder="house number"
            />
          </span>
          <div>
            <button @click="searchV1();">search</button>
          </div>
        </div>
        <div
          class="customer-results"
          v-if="$store.state.kcc.customerResults"
          v-for="customer in $store.state.kcc.customerResults"
          :key="customer.id"
        >
          <div>--------------------------------</div>
          <div>id: {{ customer.id }}</div>
          <div>date_birth: {{ customer.date_birth }}</div>
          <div>email: {{ customer.email }}</div>
          <div>first_name: {{ customer.first_name }}</div>
          <div>last_name: {{ customer.last_name }}</div>
          <div>gender: {{ customer.gender }}</div>
          <div>notes: {{ customer.notes }}</div>
          <div>telephone: {{ customer.telephone }}</div>
          <div>zip_code: {{ customer.zip_code }}</div>
          <div>--------------------------------</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeComponent',
  data() {
    return {
      // Customers: {},
      ZipCode: "",
      HouseNumber: "",
    };
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
    },
    searchV1: function() {
      this.$store.dispatch('kcc/searchCustomers')
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

