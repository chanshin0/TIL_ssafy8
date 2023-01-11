<template>
  <div class="Parent">
    <h1>AppParent</h1>
    <AppChild/>
    <hr>
    <input type="text">
    <h3>appData</h3>
    <h3>childData</h3>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  components:{
    AppChild,
  }
}
</script>

<style>

</style>