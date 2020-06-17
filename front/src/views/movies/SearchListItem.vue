<template>
<div class="col-3 my-3">
    <li v-if="movie.poster_path"><img class="movie--poster my-3" :src="posterUrl(movie)"></li>
            
           <li v-else><img class="movie--poster my-3" src="@/assets/NoPoster.jpg"></li> 
   
    
    
    <h3>{{movie.name}}</h3>
   
  </div>
  
</template>

<script>
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
        return{}
    },
    methods:{
         PosterUrl(one){
      return "https://image.tmdb.org/t/p/w300/" + one.poster_path
    },
    }
}
</script>

<style>
.movie--poster {
  width: 200px;
}
</style>