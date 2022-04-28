<template>
  <v-container
      fluid
      style="height: 300px"
  >
    <v-row justify="center">
      <v-menu
          bottom
          min-width="200px"
          rounded
          offset-y
      >
        <template v-slot:activator="{ on }">
          <v-btn
              icon
              x-large
              v-on="on"
          >
            <v-avatar
                color="brown"
                size="48"
            >
              <span class="white--text text-h5">{{ user.initials }}</span>
            </v-avatar>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <v-avatar
                  color="brown"
              >
                <span class="white--text text-h5">{{ user.initials }}</span>
              </v-avatar>
              <h3>{{ user.fullName }}</h3>
              <p class="text-caption mt-1">
                {{ user.email }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn
                  depressed
                  rounded
                  text
                  @click="toedit"
              >
                Edit Account
              </v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn
                  depressed
                  rounded
                  text
                  @click="logout()"
              >
                Disconnect
              </v-btn>
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
    </v-row>
  </v-container>
</template>


<script>
import Storage from "@/uitl/Storagehandle";
import service from "../../../uitl/request";
import Cookies from "js-cookie";
import qs from 'qs'
import vuexStore from "../../../store";


export default {
  name: "avatars",
  data: () => ({
    user: {
      initials: 'JD',
      fullName: 'John Doe',
      email: '',
    },
  }),
  mounted() {
    service({url: '/first',method: 'get'})
        .then(response => {
          const {data} = response
          // alert('当前用户为:' +'\n'+data.data.tips)
          if (typeof (data.data.tips) === "undefined") {
              console.log("未登录")
          }else{
            this.user.email=data.data.tips
          }
        })
        .catch(error => {
          console.log(error)
        })
  },
  methods:{
    toedit(){
      this.$store.commit("getindex",2)
      this.$bus.$emit('touser');
      this.$router.push({name:'profile'})
    },
    logout(){
      // localStorage.removeItem('userData')
      // this.$store.commit("setshows");
      // this.$router.push({name:'signin'})
        //登出
      service({url: '/logout',method: 'get'})
          .then(response => {
              const { data } = response
              alert('logout!!!!' +'\n'+ data.data.tips)
              setTimeout(()=>{
                this.$store.commit("setshows");
              },200)
              this.$router.push({name:'signin'})
          })
          .catch(error => {
              console.log(error)
          })


    }
  }
}
</script>

<style scoped>

</style>
