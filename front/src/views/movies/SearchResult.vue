<template>
  <div v-if="movielist.length > 0" >
    <h2 class="tit-searched">검색된 영화</h2>
    <ul class="searched-list">
      <li v-for="movie in movielist" :key="movie.id" :movie="movie" class="movie-list">
        <h3 class="tit-list">{{movie.title}}</h3>
        <div class="img-box" @click="detailmovie(movie)">
          <img :src="PosterUrl(movie)">
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL="http://localhost:8000"
export default {
  name: 'SearchResult',
  data(){
      return{
        movielist: this.$route.params.movielist
      }
  },
  methods: {
    PosterUrl(one){
      return "https://image.tmdb.org/t/p/w300/" + one.poster_path
    },
    detailmovie(m){
      axios.get(SERVER_URL + `/movies/${m.id}/`)
        .then(() => {
          this.$router.push({name:'MovieDetail', params: {movieData: m}})
        })
        .catch(err => console.log(err.response))
    }
  }
}
</script>

<style>

</style>