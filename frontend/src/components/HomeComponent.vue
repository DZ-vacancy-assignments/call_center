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
        <br/><br/>
        <span>

            <v-select
              @input="setActiveSearch"
              :options="$store.state.kcc.searchOptionsCustomers"
              :value="activeSearch"
              :clearable="false"
            ></v-select>

        </span>
        <span
          v-if="activeSearch.code=='zipCodeHouseNumber'"
          class="search-address"
        >
          <span>
            <input
              v-model="searchParameters.zipCode"
              @keydown.enter="searchAddress"
              placeholder="zip code (XXXX<space>XX)"
            />
          </span>
          <span>
            <input
              v-model="searchParameters.houseNumber"
              @keydown.enter="searchAddress"
              placeholder="house number"
            />
          </span>
          <div>
            <button @click="searchAddress();">search</button>
          </div>
        </span>
        <span
          v-else-if="activeSearch.code=='email'"
          class="search-email"
        >
          <span>
            <input
              v-model="searchParameters.email"
              @keydown.enter="searchEmail"
              placeholder="email"
            />
          </span>
          <div>
            <button @click="searchEmail();">search</button>
          </div>
        </span>
        <span
          v-else-if="activeSearch.code=='telephoneNumber'"
          class="search-telephone"
        >
          <span>
            <input
              v-model="searchParameters.telephoneNumber"
              @keydown.enter="searchTelephone"
              placeholder="telephone number"
            />
          </span>
          <div>
            <button @click="searchTelephone();">search</button>
          </div>
        </span>

        <div
          class="customer-results"
          v-if="$store.state.kcc.customerResults"
          v-for="customer in $store.state.kcc.customerResults"
          :key="customer.id"
        >
          <div>--------------------------------</div>
          <div>id: {{ customer.id }}</div>
          <div>first_name: {{ customer.first_name }}</div>
          <div>last_name: {{ customer.last_name }}</div>
          <div>zip_code: {{ customer.zip_code }}</div>
          <div>house_number: {{ customer.house_number }}</div>
          <div>email: {{ customer.email }}</div>
          <div>telephone: {{ customer.telephone }}</div>
          <div>notes: {{ customer.notes }}</div>
          <div>date_birth: {{ customer.date_birth }}</div>
          <div>gender: {{ customer.gender }}</div>
          <div>--------------------------------</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import VueSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';

export default {
  name: 'HomeComponent',
  components: {
    'v-select': VueSelect
  },
  data() {
    return {
      activeSearch: '',
      searchParameters: {
        zipCode: '',
        houseNumber: '',
        email: '',
        telephoneNumber: '',
      }
    }
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
    setActiveSearch: function(searchOption) {
      this.activeSearch = searchOption
      return
    },
    searchAddress: function() {
      this.$store.dispatch(
        'kcc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'zip_code': this.searchParameters.zipCode,
          'house_number': this.searchParameters.houseNumber
        }
      )
      return
    },
    searchEmail: function() {
      this.$store.dispatch(
        'kcc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'email': this.searchParameters.email
        }
      )
      return
    },
    searchTelephone: function() {
      this.$store.dispatch(
        'kcc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'telephone': this.searchParameters.telephoneNumber
        }
      )
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
    if (this.activeSearch === '') {
        this.activeSearch = this.$store.state.kcc.searchOptionsCustomers[0]
    }
    return
  }
};
</script>

<style lang="scss" scoped>
  h1 {
    text-align: center;
  }
</style>
