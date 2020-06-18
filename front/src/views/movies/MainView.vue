<template>
  <div>
    <MovieList/>
    <MovieDetail/>
  </div>
</template>

<script>
// import axios from 'axios'
import MovieList from './MovieList.vue'
import MovieDetail from './MovieDetail.vue'

export default {
  name:'MainView',
  components:{
    MovieList,
    MovieDetail,
  },
}
</script>

<style>

</style>