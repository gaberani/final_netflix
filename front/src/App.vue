<template>
 <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light bg-secondary">
        <router-link to="/" class="mr-3">MoVueHome</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link to="/articles">게시글 목록</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/movies/SearchList">Search</router-link>
            </li>
            <li v-if="!islogin" class="nav-item mx-2">
              <router-link to="/accounts/login">로그인</router-link>
            </li>
            <li v-if="!islogin" class="nav-item mx-2">
              <router-link to="/accounts/signup">회원가입</router-link>
            </li>
            <li v-if="islogin" class="nav-item mx-2">
              <router-link to="/articles/create">게시글 쓰기</router-link>
            </li>
            <li v-if="islogin" class="nav-item mx-2">
              <router-link to="/movies/MovieRecommend">사용자용 추천</router-link>
            </li>
            <li v-if="islogin" class="nav-item mx-2">
              <router-link to="/accounts/logout" @click.native="logout">로그아웃</router-link>
            </li>
          </ul>
        </div>
      </nav>
    </div>
    <router-view 
      @submit-login-data="login"
      @submit-signup-data="signup"
    />
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default{
  name:'App',
  data(){
    return{
      islogin:false,
    }
  },
  methods:{
    setCookie(token){
      this.$cookies.set('auth-token',token)
      this.islogin=true
    },
    login(loginData){
      axios.post(SERVER_URL + '/rest-auth/login/',loginData)
      .then(res=>{
        this.setCookie(res.data.key)
        this.$router.push({name:'Home'})
      })
      .catch(err=>console.log(err.response))
    },
    signup(signupData){
      axios.post(SERVER_URL + '/rest-auth/signup/',signupData)
      .then(res=>{
        this.setCookie(res.data.key)
        this.$router.push({name:'Home'})
      })
      .catch(err=>console.log(err.response))
    },
    logout(){
      const config = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/rest-auth/logout/', null, config)
        .catch(err=>console.log(err.response))
        .finally(() => {
          this.$cookies.remove('auth-token')
          this.islogin = false
          this.$router.push('/')
        })
    }
  },
  mounted() {
    this.islogin = this.$cookies.isKey('auth-token')
  }
} 
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 0px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #2ee492;
}

.container {
  margin: 0
}
</style>