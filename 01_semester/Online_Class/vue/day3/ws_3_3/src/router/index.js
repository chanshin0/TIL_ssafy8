import Vue from 'vue'
import VueRouter from 'vue-router'
import NotFound from '@/views/404'
import Nocolor from '@/views/Nocolor'
import Ssafleaf from '@/views/Ssafleaf'
import Ssafling from '@/views/Ssafling'
import Ssaflower from '@/views/Ssaflower'

Vue.use(VueRouter)

const routes = [
  {
    path:'/notFound',
    name:'notFound',
    components:NotFound,
  },
  {
    path:'/ssafLeaf',
    name:'ssafLeaf',
    components:Ssafleaf,
  },
  {
    path:'/ssafLing',
    name:'ssafLing',
    components:Ssafling,
  },
  {
    path:'/ssafLower',
    name:'ssafLower',
    components:Ssaflower,
  },
  {
    path:'/noClolor',
    name:'noColor',
    components:Nocolor,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next)=>{
  to.name ? next():next({name:"notfound"})
})

export default router
