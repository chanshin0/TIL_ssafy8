<template>
  <div id="app">
    <h1>캐릭터 진화 가이드</h1>
    <nav>
      <button @click="moveToHome">Home</button>
      <button @click="moveToStart">Start</button>
    </nav>
    <h3>Start 버튼으로 시작해 보세요!</h3>
    <router-view/>
    <img src="/ssafy-banner.png" alt="">
  </div>
</template>

<script>
export default {
  methods:{
    moveToHome(){
      if(this.$$route.path !== "/"){
        this.$router.push("/")
      }
    },
    moveToStart(){
      this.$router.push({name:'noColor'})
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
