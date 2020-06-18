<template>
  <div class="detail-page row">
    <div class="col-sm-1 col-lg-2"></div>
    <div class="col-sm-10 col-lg-8">
      <p class="text-left text-white">게시글 제목: {{ article.title }}</p>
      <p class="text-left text-white" v-if="LoggedIn">게시글 내용: {{ article.content }}</p>
      <button v-if="isUser" 
              @click.prevent="goupdateArticle()"
              class="btn btn-primary m-1">게시글 수정</button>
      <button v-if="isUser" 
              @click.prevent="deleteArticle()"
              class="btn btn-danger m-1">게시글 삭제</button>
      <!-- 댓글창 -->
      <!-- <input v-model="commentData.rating" type="text"> -->
      <form v-if="LoggedIn" action="">
        <h4 class="text-left text-white">댓글 작성하기</h4>
          <div class="d-flex justify-content-start">
            <input v-model="commentData.content" type="text" class="mr-2">
            <button class="btn btn-primary" @click.prevent="createComment">댓글 작성</button>
          </div>
        <div>
        </div>
        <h3>댓글 목록</h3>
        <ul v-for="comment in comments" :key="comment.id">
          <li class="text-left">{{comment.user.username}}: {{comment.content}}</li>
          <!-- <li>{{comment.id}}</li>      -->
          <button data-toggle="modal" :data-target="'#myModal'+comment.id" @click.prevent="getComment(comment.id)">
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
                    <button @click.prevent="updateComment()" type="submit" class="btn btn-primary" data-dismiss="modal">수정하기</button>
                  </div>
                  </form>
                </div>
              </div>
            </div>
          <button @click.prevent="deleteComment(comment)">
            댓글 삭제
          </button>
        </ul>
      </form>
      <h3 v-else class="text-white">로그인한 사용자만 볼 수 있습니다.</h3>
    </div>
    <div class="col-sm-1 col-lg-2"></div>
  </div>

</template>

<script>

const SERVER_URL = 'http://localhost:8000'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'

export default {
  name:'ArticleDetail',
  data(){
    return{
      islogin:false,
      isUser:false,
      commentData: {
        content:null,
      },
      NewcommentData: {
        content:null,
      },
      article: this.$route.params.articleData,
    }
  },
  computed:{
    LoggedIn(){
      return this.$cookies.isKey('auth-token')
    },
    comments(){
      return this.article.article_comments
    },
  },
  methods:{
    // 로그인한 유저가 게시글 작성자인지 확인
    userConfirm(){
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.get(SERVER_URL+'/articles/'+this.article.id+'/user_confirm/', config)
        .then(res => {
          console.log('ㅎㅎㅎ')
          this.isUser = res.data.isUser
        })
        .catch(err => console.log(err.response))
    },
    // 아티클 정보 가져오기
    getArticle(){
      axios.get(SERVER_URL+'/articles/'+this.article.id+'/')
        .then(res2=>{
        this.article=res2.data
      })
    },
    // article UD
    goupdateArticle(){
      this.userConfirm()
      if (this.isUser) {
        // console.log('성공')
        // console.log(this.article)
        this.$router.push({name:'Create', params:{articleData: this.article}})
      }
    },
    deleteArticle(){
      this.userConfirm()
      if (this.isUser) {
        const config={
          headers:{
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
        axios.delete(SERVER_URL+'/articles/' + this.article.id + '/article_update_and_delete/', config)
          .then()
        this.$router.push({name:'List'})
      }
    },

    // commentList RESET
    resetComments(){
      axios.get(SERVER_URL+'/articles/'+this.article.id)
        .then(res=>{
        this.article=res.data
      })
    },
    // comment CRUD
    createComment() {
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.post(SERVER_URL + '/articles/'+this.article.id + '/comments_create/',this.commentData,config)
        .then(()=>{
          // console.log(res)
          axios.get(SERVER_URL+'/articles/'+this.article.id)
            .then(res2=>{
            this.article=res2.data
          })
        // this.$router.go(this.$router.history.current)
        })
        .catch(err=>console.log(err.response))
    },
    getComment(two){
        axios.get(SERVER_URL+'/articles/'+this.article.id+'/comments/'+two+'/')
        .then((res)=>{
            this.commentData=res.data     
          }
        )
        .catch(err=>console.log(err.response))
    },
    updateComment(){
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.put(SERVER_URL + '/articles/'+this.article.id+'/comments/'+this.commentData.id+'/update_and_delete/',this.NewcommentData,config)
        .then(()=>{
          this.resetComments()
          this.NewcommentData.content = null
        })
        .catch(err=>console.log(err.response))
    },
    deleteComment(one){
      const config = {
        headers: {Authorization: `Token ${this.$cookies.get('auth-token')}`}
      }
      axios.delete(SERVER_URL + '/articles/'+this.article.id+'/comments/'+one.id+'/update_and_delete/', config)
      .then(()=>{
        this.resetComments()
      })
      .catch(err=> console.log(err))
    },
  },
  mounted() {
    this.islogin = this.$cookies.isKey('auth-token')
    this.getArticle()
    // this.$forceUpdate();
    this.userConfirm()
    this.comments()
  },
  created() {
    // this.$forceUpdate();
  }
}
</script>

<style scoped>
/* .movie-wrapper {
    position: relative;
    padding-top: 50vh;
    color:white;
    opacity: 1;
    font-weight:bold;
}
.detail-page{
    opacity:0.7;
} */
</style>