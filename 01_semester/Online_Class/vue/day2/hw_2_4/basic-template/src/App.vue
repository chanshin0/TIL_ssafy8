<template>
  <div id="app">
    <h1>Cat image</h1>
    <img v-bind:src="catUrl" alt="cat" height=500>
    <button v-on:click="getCat">Get Cat</button>
    <!-- v-on:click => @click: -->
  </div>
</template>

<script>
import axios from 'axios'
// import { AxiosRequestHeaders, SerializerVisior} from 'axios'
// 밑에거는 axios에서딱 저거만 가져온다.
export default {
  data() {
    return {
      catUrl: "",
    }
  },
  created(){
    this.getCat();
  },
  methods: {
    async getCat() {
      //비동기가 어딘가 있다 async
      try{
        const url ="https://api.thecatapi.com/v1/images/search"
        const response = await axios.get(url);//.then((a)=>{this.catUrl=a.data[0].url})
        if(response.data){
          console.log(response.data);
          this.catUrl=response.data[0].url
        }
      } catch(error){
        console.log(error);
      }
     
      //await 있으면 await 끝난 다음에만 다음 구문 실행 가능.

    }
  }
}
</script>

<style>
</style>