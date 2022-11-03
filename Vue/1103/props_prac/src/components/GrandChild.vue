<template>
  <div class="grand-child">
    <h1>GrandChild</h1>
    {{grandChildData}} <br>
    {{childData}}
    <button v-on:click="addDataChange">실행</button>
  </div>
</template>


<script>
export default {
  props:["grandChildData", "childData"],
  methods:{
    addDataChange(){
      this.$emit("addDataChange", "야호")
    },
  },
}
</script>
  
<style>

</style>