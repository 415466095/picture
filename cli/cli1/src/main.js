import Vue from 'vue'
import App from './App.vue'
import router from "./router/index";
import vuetify from './plugins/vuetify'
import store from './store/index'
import '@/styles/styles.scss'
// import Axios from "axios";
import axios from "axios";
import VueAxios from "vue-axios";
import './font-awesome-4.7.0/css/font-awesome.min.css'

Vue.config.productionTip = false
// Vue.prototype.$axios=Axios
// Axios.defaults.baseURL='/api'
axios.defaults.withCredentials=true
axios.defaults.crossDomain=true

Vue.use(VueAxios,axios)

//创建一个事件总线,组件之间可以发送事件到bus总线,也可以同时监听该总线上的事件
Vue.prototype.$bus=new Vue();

// router.beforeEach((to,form,next)=> {
//   if (to.meta.loginRequest) {
//     console.log("进入");
//     if (localStorage.getItem("userData") !== null) {
//         console.log("login!");
//         store.commit("setshows");
//         console.log(store.state.shows);
//         // this.goback();
//         next()
//       }
//       next()
//     }
//   next();
// })
// router.beforeEach((to,form,next)=>{
//   if(to.meta.loginRequest){
//     if(localStorage.getItem('user')){
//       next()
//     } else {
//       console.log("?");
//       next({
//         path:'/auth/signin/identifier',
//         query:{
//           redirect:to.fullPath
//         }
//       })
//     }
//   }
//   else{
//     next()
//   }
// })
// router.beforeEach((to,form,next)=>{
//   if(to.meta.ok){
//     if(localStorage.getItem('userData')===undefined){
//       next()
//     }else {
//       console.log(1+'   '+to.path);
//       if (to.path === '/password') {
//         next({
//           path: from.path
//         })
//       }
//     }
// }})
// if (!getToken()) {
// ...
// } else {
//   if (to.path === '/login') {
//     next({
//       path: from.path
//     })
//   } else {
//   ...
//   }
// }
// router.beforeEach((to, from, next)=>{
// //   // console.log(to.meta);
//   if(to.meta.ok){
//     if (localStorage.getItem('userData')===null) { // 这里检查是否获取到cookie
//       console.log("已登出！");
//       next()
      // '/auth/signin/identifier'
      // } else {
      // next()
//       console.log("gggg");
//         next({
//           path:'/',
//           // query:{
//           // redirect:to.fullPath
//           // }
//         })
//       }
//   }
//   else{
//     console.log("kkkk");
//     next()
//   }
//   next()
// }})

new Vue({
  render: h => h(App),
  vuetify,
  store,
  router,

}).$mount('#app')
