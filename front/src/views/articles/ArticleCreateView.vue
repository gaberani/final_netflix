<template>
  <div>
    <h1>게시글 쓰기 페이지</h1>
    <div>
      <label for="title">제목: </label>
      <input v-model="articleData.title" id="title" type="text">
    </div>
      <label for="content">내용: </label>
      <textarea v-model="articleData.content" id="content" cols="50" rows="10"></textarea>
    <div>
      <button v-if="!isUpdate" @click="createArticle">작성하기</button>
      <button v-if="isUpdate" @click="updateArticle">수정하기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL= 'http://localhost:8000'
export default {
  name: 'ArticleCreateView',
  data(){
    return{
      articleData:{
        title:null,
        content:null,
        created_at:null,
      },
      preArticleData: this.$route.params.articleData
    }
  },
  methods:{
    createArticle(){
      const config={
        headers:{
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/articles/create/', this.articleData, config)
        .then(() =>{
        this.$router.push({name:'List'})
      })
        .catch(err => console.log(err.response))
    },
    updateArticle(){
      const config={
        headers:{
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.put(SERVER_URL + '/articles/' + this.preArticleData.id  + '/article_update_and_delete/', this.articleData, config)
        .then(res => console.log(res))
        .catch(err => console.log(err.response))
      this.$router.push({name:'ArticleDetail', params: {articleData: this.articleData}})
    }
  },
  computed: {
    isUpdate() {
      if (this.$route.params.articleData) {
        return true
      } else {
        return false
      }
    },
  },
  created() {
    // 수정하러 왔으면 이전 데이터로 덮어 씌움
    if (this.isUpdate) {
      this.articleData.id = this.preArticleData.id
      this.articleData.title = this.preArticleData.title
      this.articleData.content = this.preArticleData.content
      this.articleData.created_at = this.preArticleData.created_at
      this.articleData.article_comments = this.preArticleData.article_comments
      // this.articleData = this.preArticleData
    }
  }
}
</script>

<style>

</style>