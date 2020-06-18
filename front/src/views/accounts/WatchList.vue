<template>
    <div>
    <h1 class="text-white">보고 싶은 영화 목록</h1>
        <ul style="list-style: none;" v-for="movie in watchlist" :key="movie.id">
            <li class="text-white">{{movie.title}}</li>
        </ul>
    </div>
</template>

<script>
const SERVER_URL="http://localhost:8000"
import axios from 'axios'
export default {
    name:'WatchList',
    data(){
        return{
            watchlist:[],
        }
    },
    methods:{
        getWatchList(){
            const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
            axios.get(`${SERVER_URL}/movies/getwannawatch/`,config)
            .then(res=>this.watchlist=res.data)
            .catch(err=>console.log(err))
        }

    },
    created(){
        this.getWatchList()
    }

}
</script>

<style>

</style>