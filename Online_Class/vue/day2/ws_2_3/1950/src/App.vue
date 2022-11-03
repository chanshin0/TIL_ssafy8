<template>
  <div id="app">
  <h1>Todo List</h1>
  <input type="text" v-model="userInput"  v-on:keyup.enter="addList">
  <button v-on:click="addList">+</button>
  <ul>
    <li v-for="todoList in todoLists" v-bind:key="todoList">
      <input type="checkbox" v-model="todoList.flag">
      <span>{{todoList.value}}</span>
    </li>

  </ul>
  <button v-on:click="deleteList">완료 목록 삭제</button>
  </div>
</template>

<script>
export default {
  name:"app",
  data(){
    return{
      userInput:"",
      todoLists:[
      ],
    }

  },
  methods:{
    addList(){
      if (this.userInput === ""){
        alert("입력해!")
      } else {
        this.todoLists.push({flag:0, value:this.userInput})
        this.userInput = ""
      }
    },
    deleteList(){
      let new_todos = this.todoLists.filter(function(todoList){
        return todoList.flag === 0;
      })
      this.todoLists = new_todos;
    }
  }
}
</script>

<style>

</style>