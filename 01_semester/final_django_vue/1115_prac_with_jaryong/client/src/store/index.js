import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios"

const API_URL = "http://localhost:8000/"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    Token :null,
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    getArticles(context){
      axios({
        method:"get",
        url:`${API_URL}api/v1/articles/`,
        headers:{
          Authorization:`Token ${context.state.Token}`
        }
      })
        .then((res)=>{
          console.log(res)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    login(context, payload){
      console.log(payload)
      axios({
        method:'post',
        url:`${API_URL}/accounts/login/`,
        data:{
          username:payload.userId,
          password:payload.userPassword,
        }
      })
        .then((res)=>{
          console.log(res)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
  },
  modules: {
  }
})
