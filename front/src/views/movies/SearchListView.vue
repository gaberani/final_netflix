<template>
<div>
    <h1>영화 목록</h1>
    <h2>장르 선택</h2>
    <select class="form-control" v-model="selectedGenreId">
      <option :value="genre.id" v-for="genre in genres" :key="genre.id">{{genre.name}}</option>
    </select>
    
      <div class="row">
          <SearchListItem :movie="movie" v-for="movie in filteredMovies" :key="movie.id"></SearchListItem>
      </div>
    
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
            movies:[],
            genres:[],
            selectedGenreId:0,
            movie:{},
        }
    },
    mounted(){
        axios.get(`${SERVER_URL}/movies/genre/`)
        // axios.get(`${SERVER_URL}/movies/getGenre/`)
        
        .then(res=>
        this.genres=res.data
        // console.log(res.data)
        )
        .catch(err=>console.log(err))
        axios.get(`${SERVER_URL}/movies/`)
        .then(res=>this.movies=res.data)
        .catch(err=>console.log(err))
    },
      computed: {
    
  },
  methods:{
    filteredMovies() {
      if (this.selectedGenreId !== 0) {
        
        return this.movies.filter(movie => {
          
          
          return this.selectedGenreId in movie.genres
      })} else {
        return this.movies
      }
    }
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