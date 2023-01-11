<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title"> <br>
      <textarea cols="30" rows="10" v-model.trim="content"></textarea>
      <input type="submit" value="제출">
    </form>
    <router-link :to="{name:'index'}">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name:'CreateView',
  data(){
    return{
      title:null,
      content:null,
    }
  },
  // 메소드 - 액션 - 뮤테이션 - 스테이트
  methods:{
    createArticle(){
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
      // 액션호출 하고 나서 이동
      this.$router.push({name:'index'})
    }
  }
}
</script>

<style>

</style>