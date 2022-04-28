<template>
  <div style="margin-left: 40px">
<!--    <v-btn @click="login()">nmsl</v-btn>-->
    <h2></h2>
<!--  <img :src="'data:image/jpg;base64,'+item" alt="" v-for="item in this.srcs"-->
<!--    style="width: 50%;height: 50%">-->
<!--    <div v-for="item in this.srcs"></div>-->
      <!-- each component is wrapped by a waterfall slot -->
<!--        <img :src="'data:image/jpg;base64,'+item.url" alt="/">-->
    <headline />
    <gallery></gallery>>
    <backtop @click.native="comeback" :style="{display:isshow}"
    ></backtop>
  </div>

</template>

<script>
import service from "../../../uitl/request";
import Cookies from "js-cookie";
import qs from 'qs'
import backtop from "../../../components/common/backtop/backtop";
  export default {
    name: 'HelloWorld',
    data: () => ({
      solo:['ss'],
      srcs:[],
      isshow:'none'
    }),
    components:{
      Gallery: () => import('../../../components/Gallery'),
      Headline: () => import('./components/Headline'),
      backtop
    },
    beforeCreate() {
      this.$store.commit("getindex",0)
      // console.log(this.$store.state.index)
    },
    beforeMount() {
      console.log("SD")
      // service({url: '/getpic',method: 'post'})
      //     .then(response => {
      //       const { data } = response
      //       for(let i=0;i<data.data.length;i++){
      //         this.srcs.push(data.data[i])
      //       }
      //     })
      //     .catch(error => {
      //       console.log(error)
      //     })
    },
    mounted() {
        window.addEventListener('scroll',this.handleScroll)
    },
    methods:{
      sum(){
        service({url: '/sum',method: 'get'})
            .then(response => {
              const { data } = response
              // alert('firstPage!!!' +'\n'+ data.data.token+data.data.tips)
              console.log("加载完毕:"+data.data)
              this.solo=data.data
            })
            .catch(error => {
              console.log(error)
            })
      },
      // handleScroll(){
      //   this.scroll = document.documentElement.scrollTop||document.body.scrollTop
      //   // console.log(this.scroll)
      //     if(this.scroll<1000){
      //       this.isshow='none'
      //       console.log("不显示")
      //     }else{
      //       this.isshow='block'
      //       console.log("显示")
      //     }
      // },
      // comeback(){
      //   //实现跳转到顶部
      //   console.log("sassd")
      // },
    },
    destroyed(){
      window.removeEventListener('scroll',this.handleScroll)
    }

  }
</script>

