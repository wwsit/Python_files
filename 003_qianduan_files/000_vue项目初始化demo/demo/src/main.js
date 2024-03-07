import { createApp } from 'vue'
import App from './App.vue'

import router from './router'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import locale from 'element-plus/es/locale/lang/zh-cn' // 引入分页中文语言包


// .use(ElementPlus, { locale }) 实现分页语言中文

const app = createApp(App);
app.use(router).use(ElementPlus, { locale }).mount('#app')