<template>
  <div>
    <div class="container">
    <br/><br/>

      <div class="field">
        <label class="label">search options</label>
          <v-select
            class="c-v-select"
            @input="setActiveSearch"
            :options="$store.state.cc.searchOptionsCustomers"
            :value="activeSearch"
            :clearable="false"
          ></v-select>
      </div>

      <hr>

      <div
        v-if="activeSearch.code==='zipCodeHouseNumber'"
        class="search-area search-address"
      >
        <div class="columns">
          <div class="column field">
            <label class="label">zip code</label>
            <div class="control">
              <input
                class="input is-normal"
                v-model="searchParameters.zipCode"
                @keydown.enter="searchAddress"
                placeholder="XXXX<space>XX"
              />
            </div>
          </div>
          <div class="column field">
            <label class="label">house number</label>
            <div class="control">
              <input
                class="input is-normal"
                v-model="searchParameters.houseNumber"
                @keydown.enter="searchAddress"
                placeholder="house number"
              />
            </div>
          </div>
          <div class="column field" style="max-width:0;"></div>
        </div>

        <div class="control submit-search">
          <button
            class="button is-primary"
            v-bind:class="{ 'is-loading': isSearching }"
            @click="searchAddress();"
          >
            search
          </button>
        </div>
      </div>

      <div
        v-else-if="activeSearch.code==='email'"
        class="search-area search-email"
      >
        <div class="columns">
          <div class="column field">
          <label class="label">email</label>
            <div class="control">
              <input
                class="input is-normal"
                v-model="searchParameters.email"
                @keydown.enter="searchEmail"
                placeholder="email"
              />
            </div>
          </div>
          <div class="column field" style="max-width:0;"></div>
        </div>

        <div class="control submit-search">
          <button
            class="button is-primary"
            v-bind:class="{ 'is-loading': isSearching }"
            @click="searchEmail();"
          >
            search
          </button>
        </div>
      </div>

      <div
        v-else-if="activeSearch.code==='telephoneNumber'"
        class="search-area search-telephone"
      >
        <div class="columns">
          <div class="column field">
            <label class="label">telephone number</label>
            <div class="control">
              <input
                class="input is-normal"
                v-model="searchParameters.telephoneNumber"
                @keydown.enter="searchTelephone"
                placeholder="telephone number"
              />
            </div>
          </div>
          <div class="column field" style="max-width:0;"></div>
        </div>

        <div class="control submit-search">
          <button
            class="button is-primary"
            v-bind:class="{ 'is-loading': isSearching }"
            @click="searchTelephone();"
          >
            search
          </button>
        </div>
      </div>

      <hr>

      <div class="results-area">
        <a
          class="card"
          v-if="$store.state.cc.customerResults"
          v-for="customer in $store.state.cc.customerResults"
          :key="customer.id"
          @click="getCustomer(customer.id)"
        >
          <div class="card-header">
            <p class="card-header-title">
              {{ customer.first_name }} {{ customer.last_name }}
            </p>
          </div>
          <div class="card-content">
            <div class="content columns">

              <div class="column">
                <div class="var-item">
                  <span class="var-key">id</span><span class="var-value">: {{ customer.id }}</span>
                </div>
                <div class="var-item">
                  <span class="var-key">first name</span><span class="var-value">: {{ customer.first_name }}</span>
                </div>
                <div class="var-item">
                  <span class="var-key">last name</span><span class="var-value">: {{ customer.last_name }}</span>
                </div>
                <div class="var-item">
                  <span class="var-key">date of birth</span><span class="var-value">: {{ customer.date_birth }}</span>
                </div>
              </div>

              <div class="column">
                <div class="var-item">
                  <span class="var-key">zip code</span><span class="var-value">: {{ customer.zip_code }}</span>
                </div>
                <div class="var-item">
                  <span class="var-key">house_number</span><span class="var-value">: {{ customer.house_number }}</span>
                </div>
                <div class="var-item">
                  <span class="var-key">email</span><span class="var-value">: {{ customer.email }}</span>
                </div>
                <div class="var-item">
                  <span class="var-key">telephone</span><span class="var-value">: {{ customer.telephone }}</span>
                </div>
              </div>

            </div>
          </div>
        </a>
      </div>

    </div>
  </div>
</template>

<script>
import VueSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';
export default {
  name: 'SearchCustomersComponent',
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
      },
      isSearching: false,
    }
  },
  methods: {
    setActiveSearch: function(searchOption) {
      this.activeSearch = searchOption
      return
    },
    searchAddress: async function() {
      this.isSearching = true
      await this.$store.dispatch(
        'cc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'zip_code': this.searchParameters.zipCode,
          'house_number': this.searchParameters.houseNumber
        }
      )
      this.isSearching = false
      return
    },
    searchEmail: async function() {
      this.isSearching = true
      await this.$store.dispatch(
        'cc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'email': this.searchParameters.email
        }
      )
      this.isSearching = false
      return
    },
    searchTelephone: async function() {
      this.isSearching = true
      await this.$store.dispatch(
        'cc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'telephone': this.searchParameters.telephoneNumber
        }
      )
      this.isSearching = false
      return
    },
    getCustomer: function(id) {
      this.$store.dispatch('cc/getCustomer', id)
      .then(() => {
        this.$router.push('/view_customer/')
      })
    }
  },
  created: function() {
    if (this.activeSearch === '') {
        this.activeSearch = this.$store.state.cc.searchOptionsCustomers[0]
    }
    return
  }
};
</script>

<style lang="scss" scoped>
@import '../assets/css/search_customers.css';
</style>
