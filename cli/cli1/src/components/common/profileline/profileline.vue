<template>
  <div>
    <v-toolbar style="text-align: center"
      color="white"
      flat
      prominent
      height="70px"
      rounded="lg"
    >
      <v-app-bar-nav-icon style="margin-top: 7px"
      @click="toggle"
      ></v-app-bar-nav-icon>
<!--      <v-toolbar-title style="margin-left: 40px; margin-top: 39px;-->
<!--      ">-->
<!--      </v-toolbar-title>-->
      <search style="margin-left: 20px; margin-top: 12px;
       width: 9864px;margin-right: -80px;
      "
       ></search>
      <avatars style="margin-left: 1000px; margin-top: 6px" ></avatars>
    </v-toolbar>
<!--    <search style="margin-left: 300px"></search>-->
  </div>
</template>

<script>
import avatars from "@/components/common/avatar/avatars";
import search from "@/components/common/search/search";
export default {
  name: "profileline",
  components:{
    avatars,
    search
  },
  data(){
    return {
      item:[
          "1","2","3"
      ]
    }
  },
  methods:{
    dddd(){
      console.log("??!");
    },
    toggle(){
      this.$bus.$emit('draws');
    }
  }
}
</script>

<style scoped>
::v-deep .v-sheet {
    margin-top: 20px;
    margin-left: 300px;
    margin-right: 4px;
  }

</style>