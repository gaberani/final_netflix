<template>
  <div class="row">
    <div class="col-2"></div>
    <form class="col-8" @submit.prevent="login">
      <h1 class="text-white">Login</h1>
      <div class="form-group">
        <label class="d-flex justify-content-start text-white" for="username">아이디</label>
        <input class="form-control" id="username" type="text" v-model="loginData.username" placeholder="아이디를 작성해주세요.">
<!--        <small class="form-text text-muted d-flex justify-content-start text-white">아이디를 작성해주세요.</small>-->
      </div>
      <div>
        <label class="d-flex justify-content-start text-white" for="password">비밀번호</label>
        <input class="form-control" id="password" type="password" v-model="loginData.password" placeholder="비밀번호를 작성해주세요.">
<!--        <small class="form-text text-muted d-flex justify-content-start text-white">비밀번호를 작성해주세요.</small>-->
      </div>
      <br>
      <div>
        <button class="btn btn-primary d-flex justify-content-start text-white" @click="login">확인</button>
      </div>
    </form>
    <div class="col-2"></div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data(){
    return{
      loginData:{
        username:null,
        password:null,
        // created_at: null,
      }
    }
  },
  methods:{
    login(){
      this.$emit('submit-login-data', this.loginData)
    }
  }
}
</script>

<style>

</style>