<template>
  <div>
    <h1>LogIn</h1>
    <form @submit.prevent="getUser">
      <label for="userId">아이디 : </label>
      <input type="text" id="userId" v-model="userId"><br><br>
      <label for="userPassword">비밀번호 : </label>
      <input type="password" id="userPassword" v-model="userPassword"><br><br>
      <button>로그인</button>
    </form>
  </div>
</template>

<script>
export default {
  data(){
    return {
      userId:null,
      userPassword:null,
    }
  },
  methods:{
    getUser(){
      const userId = this.userId
      const userPassword = this.userPassword
      const payload = {
        userId, userPassword
      }
      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style>

</style>