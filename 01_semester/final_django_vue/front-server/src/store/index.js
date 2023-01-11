import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
// vuex에서 쓰려면 router 임포트해야함!
import router from '@/router'

Vue.use(Vuex)

const Api_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    articles: [],
    token:null,
  },
  getters: {
    isLogin(state){
      return state.token ? true:false
      // state의 token이 있으면 true, null이면 false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
    },
    //회원가입과 로그인 할 때
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({name:'ArticleView'})
    }
  },
  actions: {
    getArticles(context,){
      axios({
        method:'get',
        url: `${Api_URL}/api/v1/articles/`,
        headers:{
          Authorization:`Token ${context.state.token}`
        }
      })
        .then((res)=>{
          // console.log(context)
          // console.log(res)
          // console.log(res.data)
          context.commit('GET_ARTICLES',res.data)
        })
        .catch((err)=>{
          console.log(err)
        })
    },

    signUp(context, payload){
      axios({
        method:'post',
        url:`${Api_URL}/accounts/signup/`,
        data:{
          username:payload.username,
          password1:payload.password1,
          password2:payload.password2,
          // username,password1,password2
          // JS에서 key이름이랑 value이름이랑 같으면 생략가능하다.
        }
      })
        .then((res)=>{
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err)=>{
          console.log(err)
        })
    },

    logIn(context, payload){
      axios({
        method:'post',
        url:`${Api_URL}/accounts/login/`,
        data:{
          username:payload.username,
          password:payload.password,
        }
      })
        .then((res)=>{
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err)=>{
          console.log(err)
        })
    },

  },
  modules: {
  }
})
