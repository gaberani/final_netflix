<template>
  <div class="detail-page row">
    <!-- <img v-if="backdropUrl" :src="backdropUrl"/>
    <img v-else src="@/assets/NoPoster.jpg"> -->
    <div class="col-1"></div>
    <div class="movie-wrapper col-10" :style="styles">
      <p>{{ movie.title }}</p>
      <p>{{ movie.overview }}</p>
    </div>
    <div class="col-1"></div>
    <div class="col-12 my-3">
      <button v-if="added" class="btn btn-warning " @click="addTo" type="button">보고시퍼용</button>
      <button v-else class="btn btn-success " @click="addTo" type="button">볼거에요</button>
    </div>
    <div class="col-1"></div>
    <div class="col-10">
      <form v-if="LoggedIn" action="">
        <h3>댓글 목록</h3>
        <ul style="list-style: none;" v-for="comment in comments" :key="comment.id">
          <li><h3 class="text-white">평점: {{comment.rating}}</h3></li>
          <li><h4 class="text-white-50">아이디: {{comment.user.username}} | 내용: {{comment.content}}</h4></li>
          <button data-toggle="modal" :data-target="'#myModal'+comment.id" @click.prevent="getComment(comment.id)" class="btn btn-primary mr-1">
            수정
          </button> 
          <div class="modal fade" :id="'myModal'+comment.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">댓글 수정</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <form @submit.prevent>
                    <div class="modal-body">
                      <div class="form-group">
                        <star-rating 
                          v-model="NewcommentData.rating"
                          v-bind:increment="0.5"
                          v-bind:max-rating="5"
                          inactive-color="#000"
                          active-color="#ffc846"
                          v-bind:star-size="50">
                        </star-rating>
                        <textarea
                          class="form-control"
                          id="article_body"
                          placeholder="수정할 댓글 내용"
                          v-model="NewcommentData.content"
                          required="required"
                          rows="3"></textarea>
                          
                      </div>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary m-progress" data-dismiss="modal">닫기</button>
                      <button @click.prevent="updateComment(comment)" type="submit" class="btn btn-primary" data-dismiss="modal">수정하기</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          <button @click.prevent="deleteComment(comment)" class="btn btn-danger">
            댓글 삭제
          </button>
          <br>
        </ul>
        <h2 class="my-3">댓글 작성하기</h2>
        <div class="col-12 d-inline-flex my-3">
          <div class="col-2"></div>
          <div class="col-4">
            <star-rating v-model="commentData.rating"
                        v-bind:increment="0.5"
                        v-bind:max-rating="5"
                        inactive-color="#fff"
                        active-color="#ffc846"
                        v-bind:star-size="50">
            </star-rating>
          </div>
          <div class="col-3"><input v-model="commentData.content" type="text"></div>
          <div class="col-2">
            <button class="btn btn-primary" @click.prevent="createComment">댓글 작성</button>
          </div>
          <div class="col-2"></div>
        </div>
        
      </form>
    </div>
    <div class="col-1"></div>
    <!-- API로 배우 불러오기 -->
    <div class="col-5"></div>
    <button class="col-2 my-2 btn btn-primary" @click="showActor">배우 확인하기</button>
    <div class="col-5"></div>
      <ul style="list-style: none;" v-for="c in actors.cast" :key="c.cast_id">
        <li v-if="c.profile_path"><img :src="c.profile_path"></li>
        <li v-else><img src="@/assets/Anonymous.jpg"></li>
        <li>{{ c.name }} </li>
      </ul>
  </div>
</template>


<script>
const SERVER_URL = 'http://localhost:8000'
const API_URL='https://api.themoviedb.org/3/';
// const IMAGE_URL='http://image.tmdb.org/t/p/'
const API_KEY='a025f1167b45b03548479a178f387003';
const BACKDROP_BASE = 'https://image.tmdb.org/t/p/w1280';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import StarRating from 'vue-star-rating'
import axios from 'axios'

export default {
  name:'MovieDetail',
  components: {
    StarRating,
  },
  data(){
    return{
      islogin:false,
      isUser:false,
      added:false,
    
      commentData: {
        rating:null,
        content:null,
      },
      NewcommentData: {
        rating:null,
        content:null,
      },
      movie: this.$route.params.movieData,
      actors: {},
      actorToggle:false,
    }
  },
  computed:{
    LoggedIn(){ return this.$cookies.isKey('auth-token') },
    comments(){ return this.movie.movie_comments },
    backdropUrl(){ return 'https://image.tmdb.org/t/p/w300/' + this.movie.backdrop_path },
    styles() {
      return {
        'background-image': `url(${BACKDROP_BASE}/${this.movie.backdrop_path})`,
        'background-repeat': 'no-repeat',
        'background-size': 'cover'
        }
      },
    existence(){ return this.movie.like_users}
    },
    mounted() {
    this.islogin = this.$cookies.isKey('auth-token')
    this.added = this.confirmadded()
  },
  methods:{
    // Actor Btn & API Request
    setActorToggle(){
      this.actorToggle=!this.actorToggle
    },
    confirmadded() {
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.get(`${SERVER_URL}/movies/confirmWatch/${this.movie.id}`,config)
        .then(res=>this.added=res.data.result)
        .catch(err=>console.log(err))
    },
    addTo(){
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.get(`${SERVER_URL}/movies/confirmWatch/${this.movie.id}`,config)
        .then(res=>this.added=res.data.result)
        .catch(err=>console.log(err))
      axios.post(`${SERVER_URL}/movies/wannawatch/${this.movie.id}/`,null,config)
        .then(()=>this.added= !this.added)
        .catch(err=>console.log(err))
    },
    showActor(){
        axios.get(`${API_URL}movie/${this.movie.id}/credits?api_key=${API_KEY}`)
        .then(res=>this.actors=res.data)
        this.setActorToggle()
        .catch(err=>console.log(err.response))
    },
    
    // Comment CRUD
    createComment() {
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.post(SERVER_URL + '/movies/'+this.movie.id + '/create/',this.commentData,config)
        .then(this.resetComments)
        .catch(err=>console.log(err.response))
    },
    resetComments(){
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/`)
        .then(res=>{ this.movie=res.data })
        .catch(err=>console.log(err.response))
    },
    updateComment(one){
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.put(SERVER_URL + '/movies/'+this.movie.id+'/comments/'+one.id+'/update_and_delete/', this.NewcommentData, config)
        .then(()=>{
          // console.log(res)
          this.resetComments()
          this.NewcommentData.content = null
          this.NewcommentData.rating = null
        })
        .catch(err=>console.log(err.response))
    },
    deleteComment(one){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.delete(SERVER_URL + '/movies/'+this.movie.id+'/comments/'+one.id+'/update_and_delete/', config)
        .then(()=>{
           this.resetComments()
        })
        .catch(err=> console.log(err))
    },
  },
}
</script>

<style scoped>
.movie-wrapper {
    position: relative;
    padding-top: 50vh;
    color:white;
    opacity: 1;
    font-weight:bold;
}
.detail-page{
  /* opacity:0.7; */
  opacity:1;
}
</style>