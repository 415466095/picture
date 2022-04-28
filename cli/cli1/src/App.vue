<template>
  <v-app style="
  background:#f2f4f4;
">
    <meta name="referrer" content="no-referrer" /> <!--可以让img标签预加载网络图片-->
    <navigation v-if="isshow()" ></navigation>
    <profileline v-if="isshow()"></profileline>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import navigation from "@/components/common/NavigationDrawers/navigation";
import profileline from "@/components/common/profileline/profileline";

export default {
  name: 'App',
  components:{
    navigation,
    profileline,
  },
  data: () => ({
    //
  }),
  methods:{
    isshow(){
      return this.$store.state.shows;
    }
  }
};
</script>




