<template>
<div>
  <div class="box create-customer">
    <article
      v-if="$store.state.kcc.createSuccess === false"
      class="message is-warning"
    >
      <div class="message-body">{{ $store.state.kcc.createError }}</div>
    </article>
    <div class="field">
      <label>first name</label>
      <input
        class="input is-normal"
        type="text"
        v-model="newCustomer.first_name"
        placeholder="first name"
      />
    </div>
    <div class="field">
      <label>last name</label>
      <input
        class="input is-normal"
        type="text"
        v-model="newCustomer.last_name"
        placeholder="last name"
      />
    </div>
    <div class="field">
      <label>date birth</label>
      <input
        class="input is-normal"
        type="date"
        v-model="newCustomer.date_birth"
        placeholder="date_birth"
      />
    </div>

    <div
      class="select is-primary"
    >
      <select
        v-model="newCustomer.gender"
      >
        <option>female</option>
        <option>male</option>
        <option>other</option>
        <option>unknown</option>
      </select>
    </div>
    <div class="field">
      <label>zip code</label>
      <input
        class="input is-normal"
        type="text"
        v-model="newCustomer.zip_code"
        placeholder="zip code"
      />
    </div>
    <div class="field">
      <label>house number</label>
      <input
        class="input is-normal"
        type="text"
        v-model="newCustomer.house_number"
        placeholder="house number"
      />
    </div>
    <div class="field">
      <label>telephone</label>
      <input
        class="input is-normal"
        type="text"
        v-model="newCustomer.telephone"
        placeholder="telephone"
      />
    </div>
    <div class="field-email">
      <label>Email</label>
      <input
        class="input is-normal"
        type="email"
        v-model="newCustomer.email"
        placeholder="email"
      />
    </div>
    <div class="field">
      <label>notes</label>
      <input
        class="input is-normal"
        type="text"
        v-model="newCustomer.notes"
        placeholder="notes"
      />
    </div>
    <button class="button" @click="createCustomer();">Create Customer</button>
  </div>
</div>
</template>

<script>
export default {
  name: 'CreateCustomerComponent',
  components: {},
  data() {
    return {
      newCustomer: {
        'first_name': "",
        'last_name': "",
        'date_birth': "",
        'gender': "unknown",
        'zip_code': "",
        'house_number': "",
        'telephone': "",
        'email': "",
        'notes': "",
      }
    }
  },
  methods: {
    createCustomer: function() {
      this.$store.dispatch('kcc/createCustomer', this.newCustomer)
      .then(() => {
        if (this.$store.state.kcc.createSuccess) {
          this.$router.push('/view_customer/')
        }
      })
    }
  },
  created: function() {
    this.$store.commit('kcc/setCustomer', {})
    this.$store.commit('kcc/setCreateSuccess', null)
    this.$store.commit('kcc/setCreateError', {})
  }
};
</script>

<style lang="scss" scoped>
@import '../assets/css/create_customer.css';
</style>
