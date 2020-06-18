<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        TITLE : <input type="text" v-model="movietitle">
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
    </div>
    <div>
      <h1>오늘의 추천</h1>
        <MainView/>
        <br>
    </div>
  </div>
</template>

<script>
import MainView from '@/views/movies/MainView.vue'


import axios from 'axios'
const SERVER_URL = "http://localhost:8000"

export default {
  name: 'Home',
  components: {
    MainView,
  },
  data(){
    return{
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
  }
}
</script>
