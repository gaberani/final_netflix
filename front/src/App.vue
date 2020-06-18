<template>
 <div id="app" class="container">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light">
        <router-link to="/" class="logo">MoVueHome</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="movie-search">
              <input type="text" v-model="movietitle" @keyup.enter="send" placeholder="영화를 검색하세요">
              <button class="btn-search-icon" @click="send" ><i class="fas fa-search"></i></button>
          </div>
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link to="/articles">글 목록</router-link>
            </li>
            <li v-if="islogin" class="nav-item ">
              <router-link to="/articles/create">글 쓰기</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/movies/SearchList">장르 검색</router-link>
            </li>
            <li v-if="!islogin" class="nav-item ">
              <router-link to="/accounts/login">로그인</router-link>
            </li>
            <li v-if="!islogin" class="nav-item ">
              <router-link to="/accounts/signup">회원가입</router-link>
            </li>
            <li v-if="islogin" class="nav-item ">
              <router-link to="/movies/MovieRecommend">영화 추천</router-link>
            </li>
            <li v-if="islogin" class="nav-item mx-2">
              <router-link to="/accounts/WatchList">보고싶어요</router-link>
            </li>
            <li v-if="islogin" class="nav-item ">
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
      movietitle:null,
      movielist:[],
    }
  },
  methods:{
    send(){
      axios.get(`${SERVER_URL}/movies/search/${this.movietitle}/`)
        .then((res)=>{
          // console.log(res.data)
          if (res.data['message']){
            alert(`Message:${res.data['message']}`)
          }
          else{
            // this.movielist=res.data
            this.$router.push({name: 'SearchResult', params:{movielist: res.data}})
          }
        })
        .catch(err=>console.log(err))
    },
    PosterUrl(one){
      return "https://image.tmdb.org/t/p/w300/" + one.poster_path
    },
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
    body {
        background-color:#000;
    }
    a:hover {
        text-decoration: none !important;
    }
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  position:fixed; left:0; top:0;
  width:100%; padding: 0;
  z-index:1;
}
nav.navbar {
  background-color:#222;
    padding: 0 0 35px;

}
.logo {
  position:absolute; top:36px; left:25px;
    font-size:26px; color:#fff; font-weight:bold;
}
.movie-search {
  text-align:center;
    margin: 0 auto;
}
.movie-search input{
 background-color:transparent;
  border:0; font-size:20px;
  border-bottom:2px solid #aaa;
  padding:10px;
  width:500px; margin-top:25px;
  color:#aaa

}
.navbar-nav {
    position:absolute;
    top:39px; right:25px;
}

.nav-item a {
    color:#aaa;
    font-size:19px;
    padding:20px 10px;
}
#nav a:hover {
  font-weight: bold;
  color:#fff;
}
#nav a.router-link-exact-active {
  color: #fff;
}

.container {
  margin: 0
}

    .btn-search-icon {
        background-color:transparent;
        border:0;
        font-size:25px;
        vertical-align:middle;
        color:#fff;
    }
    .searched-list {
        margin-bottom:145px;
    }
    .tit-searched {
        font-size:40px; color:#fff; font-weight: bold;
        margin-top:55px
    }
.movie-list {
    display:inline-block;
    width:30%;
    margin: 0 1.66666666666%;
}
    .movie-list img {
        width:100%;
    }
    .tit-list {
        color:#aaa; font-size:20px;
        font-weight:bold; margin:65px 0 40px
    }
</style>