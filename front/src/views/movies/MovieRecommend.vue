<template>
<div>
    <h1 class="text-white">추천</h1>
    <ul v-for="comment in comments" :key="comment.id">
        <li v-if="comment.poster_path"><img :src="posterUrl(comment)"></li>
        <li v-else><img src="@/assets/NoPoster.jpg"></li> 
        <li>{{comment.rating}}</li>
    </ul>
</div>
  
</template>

<script>
const SERVER_URL='http://localhost:8000'
import axios from 'axios'
export default {
    name:'MovieRecommend',
    data(){
        return{
            comments:[],
            movie:{},
            genres:[],
        }
    },
    methods:{
        posterUrl(one){ return 'https://image.tmdb.org/t/p/w300/' + one.poster_path },
        getComment(){
        const config = {
            headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
        }
        axios.get(`${SERVER_URL}/movies/comments/`,config)
            .then(res=>this.comments=res.data)
            .catch(err=>console.log(err))
        }
        
    },
    computed:{
         
    },
    mounted(){
        this.getComment()
    }
}
</script>

<style>
</style>