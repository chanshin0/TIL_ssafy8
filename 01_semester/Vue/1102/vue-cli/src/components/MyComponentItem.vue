<template>
  <div>
    <h3>나는 MyComponent의 하위 컴포넌트이다</h3>
    <p>{{staticProps}}</p>
    <p>{{dynamicProps}}</p>
    <button @click="childToParent">클릭</button>
  </div>
  <input type="text"
  v-model="childInputData"
  @keyup.enter="childInput"
  >
</template>

<script>
export default {
  name:"MyComponentItem",
  props:{
    staticProps:String,
    dynamicProps:String,
  },
  methods:{
    childToParent:function () {
      this.$emit("child-to-parent", '여기는 데이터보내는 자리다!')
    }
  },
}
</script>

<style>

</style>