<template>
<div>
  <div class="box customer-view">
    <div class="columns">

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
        <div class="var-item">
          <span class="var-key">gender</span><span class="var-value">: {{ customer.gender }}</span>
        </div>
        <br><br>
        <div class="var-item">
          <span class="var-key"><u>notes:</u></span></div>
        <div class="var-item">
          <span class="var-value">{{ customer.notes }}</span>
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
        <br>
        <div class="var-item">
          <span class="var-key">date created</span><span class="var-value">: {{ customer.date_create }}</span>
        </div>
        <div class="var-item">
          <span class="var-key">date updated</span><span class="var-value">: {{ customer.date_update }}</span>
        </div>
      </div>

    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ViewCustomer',
  components: {},
  data() {
    return {
      customer: {}
    }
  },
  methods: {},
  created: function() {
    this.customer = this.$store.state.cc.customer
    return
  }
};
</script>

<style lang="scss" scoped>
@import '../assets/css/view_customer.css';
</style>
