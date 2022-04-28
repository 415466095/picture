import Vue from "vue";
import VueRouter from "vue-router"
import service from "../uitl/request";
import vuexStore from "../store";
import Cookies from "js-cookie";


const son= ()=>import('../components/test')
const HelloWorld=()=>import('../views/items/home/HelloWorld')
const NotFoundComponent=()=>import('../components/NotFoundComponent')
const Auth=()=>import('@/views/Auth/Auth')
const Signin=()=>import('@/views/Auth/Signin')
const SigninIdentifier=()=>import('@/views/Auth/SigninIdentifier')
const SigninPassword=()=>import('@/views/Auth/SigninPassword')
const Signup=()=>import('@/views/Auth/Signup')

const query = ()=>import('@/views/items/query/queue')
const upload = ()=>import('@/views/items/upload/upload')
const profile = ()=>import('@/views/items/profile/profile')




//使用插件
Vue.use(VueRouter);


const routes=[
  {
    path: '/auth',
    component: Auth,
    children: [
  {
    path: 'signin',
    component: Signin,
    children: [
      {
        path: 'identifier',
        name: 'signin',
        component: SigninIdentifier,
        meta:{
          title: '账户验证',
          ok:true
        }
      },
      {
        path: 'password',
        name: 'password',
        component: SigninPassword,
        meta:{
          title:'密码输入',
          ok:true
        }
      }
    ],
    meta:{
      title: '登录',
      ok:true
    }
  },
      {
        path: 'signup',
        component: Signup,
        name: 'signup',
        meta:{
          title:'登录',
          ok:true
        }
  }
],
    meta:{
      title: '登录'
    }
},
  {
      path: '*',
      redirect: { name: 'signin'}
  },
    //上面为修改
  {
    path:'/',
    name:'hello',
    component:HelloWorld,
    meta:{
      title: '测试',
      loginRequest:true
    }
  },
  {
    path:'/query',
    name:'query',
    component:query,
    meta:{
      title: '索引',
      loginRequest:true
    }
  },
  {
    path:'/upload',
    name:'upload',
    component:upload,
    meta:{
      title: '上传图片',
      loginRequest:true
    }
  },
  {
    path:'/profile',
    name:'profile',
    component:profile,
    meta:{
      title:"个人页面",
      loginRequest:true
    }
  }
    ,
  {
    path: '/son',
    meta:{
      title:"下一步",
    },
    component:son
  },
  {
    path: '*',
    meta:{
      title:"未找到",
    },
    component: NotFoundComponent
  }
]

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location, onResolve, onReject) {
  if (onResolve || onReject) return originalPush.call(this, location, onResolve, onReject)
  return originalPush.call(this, location).catch(err => err)
}

const router = new VueRouter({
  routes,
  mode:'history'
})

export default router;

//路由守卫
router.beforeEach((to, from, next) => {
  if(to.meta.title){//判断是否有标题
    console.log("ppp")
    document.title = to.meta.title
  }
  next()
  //后端验证token，表明目前为登录状态
  setTimeout(()=>{
    console.log("start")
    service({url: '/first',method: 'get'})
        .then(response => {
          // console.log("1")
          const { data } = response
          // alert('当前用户为:' +'\n'+data.data.tips)
            if(typeof (data.data.tips) === "undefined"){
              // console.log("2")
              setTimeout(() => {
                vuexStore.commit("setshowsoff")
              }, 100)
              if(to.path!=='/auth/signin/identifier'&&
                  to.path!=='/auth/signup'&&
                  to.path!=='/auth/signin/password'){
                // alert("当前未登录，请先登录！");
                // console.log("当前未登录，请先登录！")
                next('/auth/signin/identifier')
              }
              else{
                setTimeout(() => {
                  vuexStore.commit("setshowsoff")
                }, 100)
                // console.log("3")
                next()
              }
            }else {
              // console.log("4")
              if (to.path === '/auth/signin/identifier' ||
                  to.path === '/auth/signup' ||
                  to.path === '/auth/signin/password') {
                next('/')
              } else {
                next()
                setTimeout(() => {
                  vuexStore.commit("setshows")
                }, 100)
                // this.$bus.emit("userload",data.data.tips)
              }
            }
        })
        .catch(error => {
          console.log(error)
        })
  },100)
})




