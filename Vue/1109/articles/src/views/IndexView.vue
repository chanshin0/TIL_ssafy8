<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{name:'create'}">게시글 생성하기</router-link>
    <!-- 3. 사용하기 -->
    <ArticleItem
    v-for="article in articles"
    :key="article.id"
    :article=article
    />
  </div>
</template>

<script>
// 1. 불러오기
import ArticleItem from '@/components/ArticleItem'

export default {
  name:'IndexView',
  // 2. 등록하기
  components:{
    ArticleItem,
  },
  computed:{
    articles(){
      return this.$store.state.articles
    }
  }
}
</script>

<style>

</style>