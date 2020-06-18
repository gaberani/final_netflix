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
              영화검색 : <input type="text" v-model="movietitle">
              <button @click="send" @keyup.enter="send">검색</button>
              <br>
              <br>
              <ul v-for="movie in movielist" :key="movie.id" :movie="movie">
                <li>
                  {{movie.title}}
                </li>
                <div class="img-box" @click="detailmovie(movie)">
                  <img :src="PosterUrl(movie)">
                </div>
              </ul>
          </div>
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link to="/articles">글 목록</router-link>
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
              <router-link to="/articles/create">글 쓰기</router-link>
            </li>
            <li v-if="islogin" class="nav-item ">
              <router-link to="/movies/MovieRecommend">영화 추천</router-link>
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
      movies:null,
      movietitle:null,
      movielist:[],
      movieData:{}
    }
  },
  methods:{
    send(){
      axios.get(`${SERVER_URL}/movies/search/${this.movietitle}/`)
        .then((res)=>{
          console.log(res.data)
          if (res.data['message']){
            alert(`Message:${res.data['message']}`)
          }
          else{
            this.movielist=res.data
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
        text-decoration: none;
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
  width:100%;
  padding: 0;
  z-index:1
}
.navbar {
  background-color:#000;
}
.logo {
  position:absolute; top:22px; left:25px;
    font-size:26px; color:#fff
}
.movie-search {
  text-align:center;
    margin: 0 auto;
}
.movie-search input{
 background-color:transparent;
  border:0;
  border-bottom:2px solid rgb(144,144,144);
  padding:10px 5px;
    width:500px;

}
.navbar-nav {
    position:absolute;
    top:27px; right:0;
}

.nav-item a {
    color:rgb(144,144,144);
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


</style>