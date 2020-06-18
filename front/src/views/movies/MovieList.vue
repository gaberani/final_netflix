<template>
  <div class="row">
      <!-- <h1 class="text-align-center">Popular Movie</h1> -->
     <div class="col-sm-6 col-lg-4" v-for="many in many3" :key="many.id" :movie="many">
      <p class="tit-movie">{{many.title}}</p>``
      <p style="display : none;">설명 : {{many.overview}}</p>
      <div class="img-box" @click="detailmovie(many)">
        <img :src="PosterUrl(many)">
        
        <div class="summary">
        <!-- <div class="effect-bar"></div> -->
				<p>{{ many.overview }}</p>
          <!-- <div class="btn-box">
            <button type="button" class="btn-preview" @click="getVideo(many)">예고편</button>
          </div> -->
        </div>
      </div>
      <!-- <img @click="detailmovie(many)" :src="PosterUrl(many)" > -->
      <!-- <div>
        <button class="d-inline-flex justify-content-start m-1 btn btn-primary" @click="getVideo(many)">Play Trailer</button>
        <button button class="d-inline-flex justify-content-end m-1 btn btn-info">좋아요~</button>
      </div> -->
    </div>
    <h1 class="col-12 tit-top">TopRated Movie</h1>
    <div class="col-sm-6 col-lg-4 img-box" v-for="top in top3" :key="top.id" :movie="top">
      <p class="tit-movie">{{top.title}}</p>
      <!-- <img src="@/assets/NoPoster.jpg"> -->
      <img v-if="top.poster_path" :src="PosterUrl(top)" width="300">
      <img v-else src="@/assets/NoPoster.jpg">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'
const API_URL='https://api.themoviedb.org/3/';
const API_KEY='a025f1167b45b03548479a178f387003';
// import MovieListItem from './MovieListItem.vue'
export default {
  name:'MovieList',
  data(){
    return{
      many3:[],
      top3:[],
      movieData: {}
    }
  },
  methods:{
    getVideo(many){
      axios.get(`${API_URL}movie/${many.id}/videos?api_key=${API_KEY}`)
      .then(res => console.log(res))
    },
    getmanyMovie() {
      axios.get(SERVER_URL + '/movies/many3/')
        // .then(res => console.log(res))
        .then(res => this.many3 = res.data)
        .catch(err => console.log(err.response))
    },
    getTopMovie(){
      axios.get(SERVER_URL + '/movies/top3/')
        .then(res=> this.top3=res.data)
        .catch(err => console.log(err.response))
    },
    PosterUrl(one){
      return "https://image.tmdb.org/t/p/w300/" + one.poster_path
    },
    detailmovie(many){
      axios.get(SERVER_URL + `/movies/${many.id}/`)
        .then(() => {
          this.$router.push({name:'MovieDetail', params: {movieData: many}})
        })
        .catch(err => console.log(err.response))
    }
  },
  created() {
    this.getmanyMovie()
    this.getTopMovie()
  }
  //     TopRatedPosterUrl(){
  //         return this.top.poster_path
  //     }
}
</script>

<style scoped>
.img-box {
   position:relative; border-radius:2%; 
  overflow:hidden;
}
.img-box > img { width:100% }
.img-box > .summary { 
  position:absolute; left:0; top:0;
  width:100%; height:100%; 
  transform:scale(1.03);
  background-color:rgba(0, 0, 0, 0.7);
  color:#fff;
  opacity:0;
  transition: all .4s;
  padding: 2.8vw 2.4vw 70px;  box-sizing:border-box;
  overflow:hidden;
  }
  .img-box > .summary > p {
    height:100%;
    overflow:hidden;
  }

.img-box:hover > .summary { 
  opacity:1;
  transform:scale(1);
}

    .tit-movie {
        color:#aaa; font-size:20px
    }
.tit-top {
    color:#fff; font-size:40px;
    font-weight:bold; margin:65px 0 40px
}


</style>

