<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="randomLunch">Pick Lunch</button>
    <p>{{lunchPicked}}</p>
    <h3>로또를 뽑아보자</h3>
    <button @click="goToLotto">Pick Lotto</button>
  </div>

</template>

<script>
import _ from 'lodash'

export default {
  name:'TheLunch',
  data(){
    return{
      lunchPicked:null,
    }
  },
  methods:{
    randomLunch(){
      const lunches = _.sample(['국밥','라면','김치찌개','된장찌개']) 
      console.log(lunches)
      this.lunchPicked = lunches
    },
    goToLotto(){
      this.$router.push({name:'lotto'})
    },

}
}

</script>

<style>

</style>