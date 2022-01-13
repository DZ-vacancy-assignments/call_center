<template>
  <div>
    <div class="container">
      <div class="work-area">
        <br/><br/>
        <span>
          <v-select
            @input="setActiveSearch"
            :options="$store.state.cc.searchOptionsCustomers"
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
          class="card"
          v-if="$store.state.cc.customerResults"
          v-for="customer in $store.state.cc.customerResults"
          :key="customer.id"
        >
          <button class="card-content" @click="getCustomer(customer.id)">
            <div>id: {{ customer.id }}
              <span>&nbsp;|&nbsp;last_name: {{ customer.last_name }}</span>
              <span>&nbsp;|&nbsp;zip_code: {{ customer.zip_code }}</span>
              <span>&nbsp;|&nbsp;house_number: {{ customer.house_number }}</span>
            </div>
            <div>email: {{ customer.email }}
              <span>&nbsp;|&nbsp;telephone: {{ customer.telephone }}</span>
              <span>&nbsp;|&nbsp;date_birth: {{ customer.date_birth }}</span>
            </div>
          </button>
        </div>
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
      }
    }
  },
  methods: {
    setActiveSearch: function(searchOption) {
      this.activeSearch = searchOption
      return
    },
    searchAddress: function() {
      this.$store.dispatch(
        'cc/searchCustomers',
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
        'cc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'email': this.searchParameters.email
        }
      )
      return
    },
    searchTelephone: function() {
      this.$store.dispatch(
        'cc/searchCustomers',
        {
          'search_option': this.activeSearch.code,
          'telephone': this.searchParameters.telephoneNumber
        }
      )
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
</style>
