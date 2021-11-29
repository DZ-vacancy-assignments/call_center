<template>
<div>
  <div>I'm in the view customer component.</div>
  <div class="box customer-view">
    <div>id: {{ customer.id }}</div>
    <br/>
    <div>first_name: {{ customer.first_name }}</div>
    <div>last_name: {{ customer.last_name }}</div>
    <div>gender: {{ customer.gender }}</div>
    <div>date_birth: {{ customer.date_birth }}</div>
    <br/>
    <div>zip_code: {{ customer.zip_code }}</div>
    <div>house_number: {{ customer.house_number }}</div>
    <br/>
    <div>email: {{ customer.email }}</div>
    <div>telephone: {{ customer.telephone }}</div>
    <br/>
  </div>
</div>
</template>

<script>
export default {
  name: 'ViewCustomerComponent',
  components: {},
  data() {
    return {
      customer: {}
    }
  },
  methods: {},
  created: function() {
    this.customer = this.$store.state.kcc.customer
    return
  }
};
</script>

<style lang="scss" scoped>
@import '../assets/css/view_customer.css';
</style>
