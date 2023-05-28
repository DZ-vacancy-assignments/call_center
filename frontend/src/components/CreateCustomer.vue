<template>
<div>
  <div class="box create-customer">
    <article
      v-if="$store.state.cc.createSuccess === false"
      class="message is-warning"
    >
      <div class="message-body">{{ $store.state.cc.createError }}</div>
    </article>

    <div class="field">
      <label class="label">first name</label>
      <div class="control">
        <input
          class="input is-normal"
          type="text"
          v-model="newCustomer.first_name"
          placeholder="first name"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">last name</label>
      <div class="control">
        <input
          class="input is-normal"
          type="text"
          v-model="newCustomer.last_name"
          placeholder="last name"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">date birth</label>
      <div class="control">
        <input
          class="input is-normal"
          type="date"
          v-model="newCustomer.date_birth"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">gender</label>
      <div class="control">
        <div class="select">
          <select
              v-model="newCustomer.gender"
          >
              <option>female</option>
              <option>male</option>
              <option>other</option>
              <option>unknown</option>
          </select>
        </div>
      </div>
    </div>

    <div class="field">
      <label class="label">zip code</label>
      <div class="control">
        <input
          class="input is-normal"
          type="text"
          v-model="newCustomer.zip_code"
          placeholder="zip code"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">house number</label>
      <div class="control">
        <input
          class="input is-normal"
          type="text"
          v-model="newCustomer.house_number"
          placeholder="house number"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">telephone</label>
      <div class="control">
        <input
          class="input is-normal"
          type="text"
          v-model="newCustomer.telephone"
          placeholder="telephone"
        />
      </div>
    </div>

    <div class="field-email">
      <label class="label">Email</label>
      <div class="control">
        <input
          class="input is-normal"
          type="email"
          v-model="newCustomer.email"
          placeholder="email"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">notes</label>
      <div class="control">
        <input
          class="input is-normal"
          type="text"
          v-model="newCustomer.notes"
          placeholder="notes"
        />
      </div>
    </div>

    <div class="control">
      <button
        class="button is-primary"
        @click="createCustomer();"
      >
        Create Customer
      </button>
    </div>
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
      this.$store.dispatch('cc/createCustomer', this.newCustomer)
      .then(() => {
        if (this.$store.state.cc.createSuccess) {
          this.$router.push('/view_customer/')
        }
      })
    }
  },
  created: function() {
    this.$store.commit('cc/setCustomer', {})
    this.$store.commit('cc/setCreateSuccess', null)
    this.$store.commit('cc/setCreateError', {})
  }
};
</script>

<style lang="scss" scoped>
@import '../assets/css/create_customer.css';
</style>
