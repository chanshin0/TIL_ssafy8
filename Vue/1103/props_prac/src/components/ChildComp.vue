<template>
  <div class="Child">
    <h1>ChildComp</h1>
    {{ childData }} <br />
    {{ childD2 }}
    <button v-on:click="tryChange"></button>
    <GrandChild :grandChildData="grandChildData" :childData="childData"
    v-on:addDataChange="addDataChange"
    />
    <div>
      <input type="text" v-on:input="callParent">
    </div>
  </div>
</template>

<script>
import GrandChild from "./GrandChild.vue";

export default {
  components: {
    GrandChild,
  },
  props: ["childData", "child-d2", "grandChildData"],
  methods: {
    addDataChange(fromGrandChild){
      this.$emit("addDataChange", fromGrandChild)
    },
    callParent(){
      this.$emit("callParent")
    }
  },
};
</script>

<style></style>
