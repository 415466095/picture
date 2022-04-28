<template>
  <div>
    <div class="text-center w-100">
      <h1 class="text-h5 mb-2">
        {{ $vuetify.lang.t('$vuetify.auth.sign-in-password.title') }}
      </h1>
      <v-chip
        class="mb-10"
        outlined
        link
        @click="$router.push({ name: 'signin' })"
      >
        <v-avatar left>
          <v-icon color="secondary">
            mdi-account-circle
          </v-icon>
        </v-avatar>
          {{this.$store.state.username}}
        <v-avatar right>
          <v-icon color="secondary">
            mdi-chevron-down
          </v-icon>
        </v-avatar>
      </v-chip>

      <v-form @submit.prevent="next">
        <v-text-field
            ref="input"
            :disabled="disabled"
            :error-messages="error"
            v-model="passwords"
            class="mb-10"
          :append-icon="show ? 'mdi-eye-off-outline' : 'mdi-eye-outline'"
          :label="$vuetify.lang.t('$vuetify.auth.sign-in-password.enter-password')"
          name="password"
          :rules="[rules.required, rules.min]"
            type="text"
          :type="show ? 'input' : 'password'"
          hide-details="auto"
          outlined
          @click:append="show = !show"
        />
      </v-form>

      <div class="d-flex justify-space-between">
        <v-btn
          class="text-none letter-spacing-0 font-weight-bold"
          style="margin-left: -16px;"
          color="primary"
          text
          @click="wip"
        >
          {{ $vuetify.lang.t('$vuetify.auth.sign-in-password.forgot-password') }}
        </v-btn>
        <v-btn
          class="text-none"
          style="min-width: 88px;"
          color="primary"
          depressed
          @click="login"
        >
          {{ $vuetify.lang.t('$vuetify.auth.sign-in-password.next') }}
        </v-btn>
      </div>
    </div>
<!--    <div>{{user}}</div>-->
  </div>
</template>

<script>
import { wip } from '@/helpers.js'
import maps from "@/uitl/passwordshow";
import service from "../../uitl/request";
import Cookies from "js-cookie";
import qs from 'qs'
import vuexStore from "../../store";

export default {
  data: () => ({
    show: false,
    rules:maps.rules,
    error: null,
    disabled: false,
    passwords:''
  }),
  // computed: {
  //   password: {
  //     get () {
  //       return this.$store.state.password
  //     },
  //     set (value) {
  //       this.$store.commit('updatePassword', value)
  //     }
  //   }
  //   // ...mapState({
  //   //   user:state => state.userData,
  //   // })
  // },
  methods: {
    wip,
    login(){
      //验证密码表单
        if (!this.validEmail(this.passwords)) {
          this.error = 'password contains invalid characters!';
          this.$refs.input.focus();
          return
        }
        this.error = null;
        //申请登录，请求后端

        service({url:'/login',method:'post',data:qs.stringify(
            {
              username: this.$store.state.username,
              password: this.passwords
            }
          )}).then(response=>{
              const {data}=response;
              // 由于网页cookie难以判断有效时间，这里的逻辑交给后端判断,sessionID判断
              Cookies.set('Authorization',data.data.token)
          //这里设置token对接后端后不进入验证token路由而是直接创建
              if(data.msg){
                setTimeout(()=>{
                  alert("欢迎回来!"+'\n'+data.user)
                },100)
                vuexStore.commit("getindex",0)
                this.$router.push('/')
                // setTimeout(()=>{
                //     //后端验证token，表明目前为登录状态
                //     service({url: '/first',method: 'get'})
                //         .then(response => {
                //           const { data } = response
                //           // alert('firstPage!!!' +'\n'+ data.data.token+data.data.tips)
                //           setTimeout(()=>{
                //             this.$store.commit("setshows")
                //           },100)
                //           this.$router.push('/');
                //         })
                //         .catch(error => {
                //           console.log(error)
                //         })
                // })
              }else{
                alert("message："+'\n'+data.data)
              }
            })
        .catch(error=>{
          console.log(error)
        })



          // this.$emit('next', this.password)
        //这里可以提交到Auth中的next事件,执行加载效果展示
          // this.$router.push({ name: 'password' })
        //设置用户信息存储
        // this.$store.commit('userDataFix','nmsl');
        // this.$store.commit("setshows");
        // this.$router.push({name:'hello'})
    },

    validEmail (email) {
      var re = /^[A-Za-z0-9]+$/g
      //只包含数字和字母的正则
      return re.test(email)
    }
  },
  beforeRouteEnter(to,from,next){
    if(localStorage.getItem("userData")!==null){
        next({path:'/'})
    }
      //   else{
    //     console.log(this.$store.state.shows);
    //     next()
    //   }
    // console.log(localStorage.getItem("userData"));
    next()
  }
}
</script>
