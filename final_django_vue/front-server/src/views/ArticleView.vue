<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{name:'CreateView'}">CreateArticle</router-link>
    <hr>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles(){
      if (this.isLogin===true){
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스입니다')
        this.$router.push({name:'LogInView'})
      }

      // this.$store.dispatch('getArticles',)
    }
  }
}
</script>

<style>

</style>
