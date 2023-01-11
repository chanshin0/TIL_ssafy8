import { createRouter, createWebHistory } from 'vue-router'
import TheLunch from '../views/TheLunch.vue'
import TheLotto from '../views/TheLotto.vue'

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: TheLunch
  },
  {
    path: '/lotto/6',
    name: 'lotto',
    component: TheLotto
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
