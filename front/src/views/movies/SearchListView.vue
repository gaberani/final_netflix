<template>
  <div class="row">
    <h1>영화 목록</h1>
    <h2>장르 선택</h2>
    <select class="form-control" v-model="selectedGenreId">
      <option :value="genre.id" v-for="genre in genres" :key="genre.id">{{genre.name}}</option>
    </select>
    <button class="btn btn-warning" @click.prevent="filteredMovies()">장르 검색</button>

    <!-- 검색 버튼 누르면 보이는 곳 -->
    <div>
      <span v-for="movie in genre_movies" :key="movie.id">
        <SearchListItem :movie="movie"></SearchListItem>
      </span>
    </div>
    <!-- <p>{{ movies }}</p> -->
  </div>
  
</template>

<script>
import axios from 'axios'
import SearchListItem from './SearchListItem.vue'
const SERVER_URL = "http://localhost:8000"
export default {
    name:'SearchList',
    components:{
        SearchListItem
    },
    data(){
        return{
            genre_movies:[],
            genres:[],
            selectedGenreId:0,
            movie:{},
        }
    },
    mounted(){
        
        // axios.get(`${SERVER_URL}/movies/`)
        //   .then(res=>this.movies=res.data)
        //   .catch(err=>console.log(err))
    },
    methods:{
      filteredMovies() {
        axios.get(`${SERVER_URL}/movies/getGenre/${this.selectedGenreId}/`)
          .then(res=>this.genre_movies=res.data)
          .catch(err=>console.log(err))
        // if (this.selectedGenreId !== 0) {
        //   return this.movies.filter(movie => {
        //     return this.selectedGenreId in movie.genres
        // })} else {
        //   return this.movies
        // }
      },
      getGenres() {
        axios.get(`${SERVER_URL}/movies/genre/`)
          .then(res=>this.genres=res.data)
          .catch(err=>console.log(err))
      }
    },
  created() {
    this.getGenres()
  }
}
</script>

<style>
select {
  display: block;
  width: 50% !important;
  margin: 2rem auto !important;
}
</style>