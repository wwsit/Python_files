
import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/page/home.vue'
import ElementPage from '@/page/elementTablePage.vue'
import Pagination from '@/page/elementPagination.vue'
import TableOpen from '@/page/elementTableOpen.vue'


//定义routes路由的集合，数组类型
const router = createRouter({

  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { show: false }
    },

    {
        path:"/elementTable",
        component:ElementPage,
        meta: { show: true }
    },
    {
        path:"/elementPagination",
        component:Pagination,
        meta: { show: true }
    },

    {
        path:"/elementTableOpen",
        component:TableOpen,
        meta: { show: true }
    }

   
    



  ]
});

export default router