<template>
  <div>
    <h1>Article</h1><hr>
    <ArticleItem/>
  </div>  
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue'




export default {
  components:{
    ArticleItem,
  },
  data(){
    return{
      Token:null,
    }
  },
  methods:{
    getArticles(){
      if (this.isLogIn===true){
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스입니다!')
        this.$router.push({name:'login'})
      }
    }
  },
  created(){
    this.getArticles()
  },
}
</script>

<style>

</style>