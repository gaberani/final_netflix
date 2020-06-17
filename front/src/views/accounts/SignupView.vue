<template>
  <div class="row">
    <div class="col-2"></div>
    <form class="col-8" @submit.prevent="signup">
      <h1>회원가입 페이지</h1>
      <div class="form-group">
        <label class="d-flex justify-content-start" for="username">아이디: </label>
        <input class="form-control" id="username" v-model="signupData.username" type="text">
        <small id="emailHelp" class="form-text text-muted d-flex justify-content-start">아이디를 작성해주세요.</small>
      </div>
      <div class="form-group">
        <label class="d-flex justify-content-start" for="password1">비밀번호: </label>
        <input class="form-control" v-model="signupData.password1" id="password1" type="password">
        <small id="emailHelp" class="form-text text-muted d-flex justify-content-start">비밀번호를 작성해주세요.</small>
      </div>
      <div>
        <label class="d-flex justify-content-start" for="password2">비밀번호 확인: </label>
        <input class="form-control" v-model="signupData.password2" id="password2" type="password">
        <small id="emailHelp" class="form-text text-muted d-flex justify-content-start">비밀번호를 다시 한번 입력해주세요.</small>
      </div>
      <br>
      <div>
        <button class="btn btn-primary d-flex justify-content-start">확인</button>
      </div>
    </form>
    <div class="col-2"></div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data(){
    return{
      signupData:{
        username:null,
        password1:null,
        password2:null
      }
    }
  },
  methods: {
    signup() {
      this.$emit('submit-signup-data', this.signupData)
    }
  }
}
</script>

<style>


</style>