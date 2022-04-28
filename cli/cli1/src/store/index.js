import Vue from 'vue'
import Vuex from 'vuex'
import Storage from '@/uitl/Storagehandle'
import service from "../uitl/request";
import Cookies from "js-cookie";
import qs from 'qs'
import pathify from 'vuex-pathify'
import * as modules from './modules'

Vue.use(Vuex)
console.log(Storage)

const vuexStore = new Vuex.Store({
  modules,
  state: {
    drawer: false,
    links: [
      'Home',
      'About me',
      'Portfolio',
      'Blog',
      'Contact',
    ],

    username:'',
    shows:false,
    identifier: '',
    password: '',
    loading: false,
    disabled: false,
    lastshows:false,
    index:0,
    cookie: 0,
    //检验token
    token:Storage.getItem("token")||null,
    userData:Storage.getItem("userData")||null
  },
  getters:{
    // show:()=>Storage.getItem("userData") !== null
    //检验token
    // token:()=>Storage.getItem("token")||null,
    // userData:()=>Storage.getItem("userData")||null
  },
  mutations: {
    getuser (state,username) {
      state.username=username;
    },

    setshows (state) {
      //在每次发请求并收到回复之后执行，判断session是否存在
      // state.shows=null;
      state.shows=true;
      // state.userData=Storage.getItem("userData")||null;
      // console.log(state.userData);
      // state.shows=!(state.userData==null);
      // state.lastshows=state.shows;
    },
    setshowsoff (state) {
      //在每次发请求并收到回复之后执行，判断session是否存在
      // state.shows=null;
      state.shows=false;
      // state.userData=Storage.getItem("userData")||null;
      // console.log(state.userData);
      // state.shows=!(state.userData==null);
      // state.lastshows=state.shows;
    },
    getindex (state,num) {
      state.index=num;
    },
    //新加入
    SET_DRAWER (state, payload) {
      state.drawer = payload
    },

    updateIdentifier (state, identifier) {
      state.identifier = identifier
    },

    updatePassword (state, password) {
      state.password = password
    },

    setLoading (state, loading) {
      state.loading = loading
    },

    setDisabled (state, disabled) {
      state.disabled = disabled
    },
    //赋值token
    tokenFix (state, token) {
      Storage.setItem(`token`, token)
      state.token = token
    },
    //赋值用户信息
    userDataFix (state,data) {
      Storage.setItem(`userData`, data)
      console.log("!");
      // state.userData = userData
    },
  },
  actions:{
    //提交修token
    updatetoken (context,value) {
      context.commit('token',value)
    },
    //提交修改用户信息
    updateuserData (context,value) {
      context.commit('userData',value)
    }
  },
  plugins: [pathify.plugin],
})

export default vuexStore


// export default createStore({
//   state: {
//     identifier: '',
//     password: '',
//     loading: false,
//     disabled: false
//   },
//
//   mutations: {
//     updateIdentifier (state, identifier) {
//       state.identifier = identifier
//     },
//
//     updatePassword (state, password) {
//       state.password = password
//     },
//
//     setLoading (state, loading) {
//       state.loading = loading
//     },
//
//     setDisabled (state, disabled) {
//       state.disabled = disabled
//     }
//   }
// })
