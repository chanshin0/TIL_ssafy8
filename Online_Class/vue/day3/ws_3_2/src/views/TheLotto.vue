<template>
  <div>
    <h1>로또번호</h1>
    <button @click="getLotto">Get Lucky Numbers</button>
    <p>{{myPrecious}}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name:'TheLotto',
  data(){
    return{
      myPrecious:null,
    }
  },
  methods:{
    getLotto(){
      const lottos = _.sampleSize(_.range(1, 49), 6) 
      console.log(lottos)
      this.myPrecious = lottos
    }
  },
}
</script>

<style>

</style>