<template>
  <div id="app">
    <h1>APP</h1>
    {{ appData }}
    <ChildComp v-bind:childData="childData" :childD2="childData2" :grandChildData="grandChildData" 
    v-on:addDataChange="addDataChange"
    />
  </div>
</template>

<script>  
import ChildComp from "./components/ChildComp.vue";

export default {
  name: "App",
  components: {
    ChildComp,
  },
  data() {
    return {
      appData: "App 데이터",
      childData: "Child 데이터",
      childData2: "Child 데이터2",
      grandChildData: "GrandChild 데이터",
    };
  },
  methods:{
    addDataChange(fromGrandChild){
      this.appData = fromGrandChild
    },
    
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.child {
  border: 3px solid blue;
}
</style>
