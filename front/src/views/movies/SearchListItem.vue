<template>
  <div>
    <h3 class="tit-list">{{movie.title}}</h3>
    <!-- <p>{{ movie.poster_path }}</p> -->
    <img v-if="movie.poster_path" @click="detailmovie(movie)" class="movie--poster my-3" :src="PosterUrl(movie)">
    <img v-else @click="detailmovie(movie)" class="movie--poster my-3" src="@/assets/NoPoster.jpg">

  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = "http://localhost:8000"
export default {
    name:'SearchListItem',
    components:{
    },
    props:{
        movie:{
            type:Object,
        }
    },
    data(){
        return{
          movieData: {}
        }
    },
    methods:{
      PosterUrl(one){
        console.log(one.poster_path)
        return "https://image.tmdb.org/t/p/w300/" + one.poster_path
      },
      detailmovie(movie){
        axios.get(SERVER_URL + `/movies/${movie.id}/?`)
          .then(() => { this.$router.push({name:'MovieDetail', params: {movieData: movie}}) })
          .catch(err => console.log(err.response))
    },
    computed:{
      LoggedIn(){ return this.$cookies.isKey('auth-token') },
    }
  }
}
</script>

<style>
.movie--poster {
  width: 200px;
}
  .tit-list {
    color:#aaa;
    font-weight: bold;
  }
</style>