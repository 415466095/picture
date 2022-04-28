<template>
  <div>
    <div class="text-center">
      <h1 class="headline mb-2">
        {{ $vuetify.lang.t('$vuetify.auth.sign-in.title') }}
      </h1>
      <span class="d-inline-block mb-8">{{ $vuetify.lang.t('$vuetify.auth.sign-in.subtitle') }}</span>
    </div>


<!--    第一个input-->
    <v-form ref="loginForm" :model="loginData" @submit.prevent="next">
      <v-text-field style="margin-top:25px"
                    :rules="[rules.required1, rules.authorizations]"
                    ref="input"
        prop="username"
        class="mb-2"
        v-model="loginData.username"
        :label="$vuetify.lang.t('$vuetify.auth.sign-in.label')"
        name="login"
        type="username"
        hide-details="auto"
        outlined
        :disabled="disabled"
        :error-messages="error"
      />
<!--      <v-text-field-->
<!--          ref="input"-->
<!--          prop="password"-->
<!--          class="mb-2"-->
<!--          v-model="loginData.password"-->
<!--          :label="$vuetify.lang.t('$vuetify.auth.sign-in.label')"-->
<!--          name="login"-->
<!--          type="password"-->
<!--          hide-details="auto"-->
<!--          outlined-->
<!--          :disabled="disabled"-->
<!--          :error-messages="error"-->
<!--      />-->

<!--      <a-->
<!--        href="#"-->
<!--        class="d-inline-block text-body-2 text-decoration-none font-weight-bold mb-8"-->
<!--        @click="wip"-->
<!--      >{{ $vuetify.lang.t('$vuetify.auth.sign-in.forgot-email') }}</a>-->
    </v-form>

    <div class="text-body-2 text--secondary mb-8">
      {{ $vuetify.lang.t('$vuetify.auth.sign-in.private') }}
      <a
        href="#"
        class="d-inline-block text-none text-decoration-none font-weight-bold"
      >{{ $vuetify.lang.t('$vuetify.auth.sign-in.learn-more') }}</a>
    </div>


    <div class="d-flex justify-space-between" style="margin-top: 100px">
      <v-btn
        class="text-none letter-spacing-0"
        style="margin-left: -16px;"
        color="primary"
        text
        @click="$router.push({ name: 'signup' })"
      >
        {{ $vuetify.lang.t('$vuetify.auth.sign-in.create-account') }}
      </v-btn>



      <v-btn
        class="text-none"
        style="min-width: 88px;"
        color="primary"
        depressed
        @click="next"
      >
        {{ $vuetify.lang.t('$vuetify.auth.sign-in.next') }}
      </v-btn>

<!--      <v-btn-->
<!--          class="text-none"-->
<!--          style="min-width: 88px;"-->
<!--          color="primary"-->
<!--          depressed-->
<!--          @click="logout"-->
<!--      >-->
<!--        {{ $vuetify.lang.t('$vuetify.auth.sign-in.next') }}-->
<!--      </v-btn>-->

<!--      <v-btn-->
<!--          class="text-none"-->
<!--          style="min-width: 88px;"-->
<!--          color="primary"-->
<!--          depressed-->
<!--          @click="tests"-->
<!--      >-->
<!--        {{'test'}}-->
<!--      </v-btn>-->

    </div>
  </div>
</template>

<script>
import { wip } from '@/helpers.js'
//网络导入
import Cookies from "js-cookie";
import qs from 'qs'
import maps from "../../uitl/passwordshow"
import service from "@/uitl/request";

export default {
  data: () => ({
    error: null,
    disabled: false,
    rules:maps.rules,
    loginData:{
      username:'',
      password:''
    },
    datas:{}
  }),
  watch:{
    'loginData.username'(val){
         this.$store.commit("getuser",val);
    }
  },
  computed: {
    identifier: {
      get () {
        return this.$store.state.identifier
      },
      set (value) {
        this.$store.commit('updateIdentifier', value)
      }
    }
  },

  methods: {
    next () {
      //校验账号是否符合规范
      if(this.rules.required1(this.loginData.username)==='Required.'||
          this.rules.authorizations(this.loginData.username
          )==='It is not an valid email.'){
        this.$refs.input.focus()
        return
      }else{
        //请求后端看该账户是否存在数据库
        service({url:'/finduser',method:'post',data:qs.stringify(this.loginData)})
            .then(response=>{
              const {data}=response;
              this.datas=data.data;
              //这里的逻辑交给后端判断
              // Cookies.set('Authorization',data.data.token)
              // this.$refs.input.focus()
            })
            .catch(error=>{
              console.log(error)
            })
      }
      setTimeout(()=>{
        if(this.datas.msg){
          this.error = null
          this.$emit('next', this.loginData.username)
        }else{
            alert(this.datas.data)
        }
      },300)
      // this.error = null
      // this.$emit('next', this.loginData.username)
      // this.$router.push({ name: 'password' })
    },
    // validEmail (email) {
    //   var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    //   return re.test(email)
    // },
    wip,
    logout(){
      //登出
        service({url: '/logout',method: 'get'})
            .then(response => {
              const { data } = response
              alert('logout!!!!' +'\n'+ data.data.tips)
            })
            .catch(error => {
              console.log(error)
            })
    },
    tests(){
      //后端验证token，表明目前为登录状态
        service({url: '/first',method: 'get'})
            .then(response => {
              const { data } = response
              alert('firstPage!!!' +'\n'+ data.data.token+data.data.tips)
            })
            .catch(error => {
              console.log(error)
            })
    }

  },
  // beforeRouteEnter(to,from,next){
  //   if(localStorage.getItem("userData")!==null){
  //     next({path:'/'})
  //   }
  //   next()
  // }
}
</script>
