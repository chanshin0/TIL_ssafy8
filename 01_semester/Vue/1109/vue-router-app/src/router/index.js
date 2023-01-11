import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import Loginview from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter)
const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path :'/hello/:userName',
    name : 'hello',
    component: HelloView
  },
  {
    path:'/login',
    name: 'login',
    component: Loginview,
    beforeEnter(to, from, next){
      if (isLoggedIn==true){
        console.log('이미 로그인')
        next({name:'home'})
      } else {
        next()
      }
    }
  },
  {
    path:'/404',
    name: 'NotFound404',
    component:NotFound404
  },
  {
    path:'/dog/:breed',
    name:'dog',
    component:DogView
  },
  {
    path:'*',
    redirect:'/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next)=>{
//   // 로그인 여부
//   const isLoggedIn = false
//   // 로그인이 필요한 페이지
//   const authPages = ['hello']
  
//   const isAuthRequired = authPages.includes(to.name)

//   // 요청한 페이지가 로그인이 필요하면서, 현재 로그인 되어있지 않다면
//   if (isAuthRequired && !isLoggedIn){
//     // 로그인 페이지로 이동
//     next({name:'login'})
//   } else {
//     // 아닌 페이지는 그냥 이동
//     next()
//   }
// }


export default router
