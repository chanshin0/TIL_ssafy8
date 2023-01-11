<template>
  <div>
    <img-card/>
    <h1>Nocolor</h1>
    <button>뒤로</button>
    <img src="/happeed.png" alt="">
    <button>앞으로</button>
    <h2>시작</h2>
  </div>
</template>

<script>
import imgCard from "../components/imgCard.vue"

export default {
  name:'noColor',
  components:{
    imgCard
  }
}
</script>

<style>

</style>