<template>
    <v-navigation-drawer
        ref="drawers"
        app
        dark
        style="position: absolute;height: 100%"
        :style="{width:whatapp}"
        permanent
        v-model="drawer"
        v-if="drawer"
    >
      <v-btn style="margin-top: 5px"
             class="mx-2"
             fab
             dark
             large
             color="purple"
      >
        <v-icon dark>
          mdi-halloween
        </v-icon>
      </v-btn>
      <div class="py-3"></div>
      <v-sheet
          light
          rounded="xl"
          :max-width="256"
          class="mx-auto transition-swing accent"
          elevation="15"
          height="78"
          width="100%"
      >{{msg}}
        <br>
        {{tsg}}
      </v-sheet>
      <v-divider class="funks"
      ></v-divider>
      <div class="list1">
        PICTURE
      </div>
      <v-list
          dense
          rounded
      >
        <v-list-item-group v-model="model1"
                           max="1" >
          <v-list-item style="margin: 30px"
              v-for="(item, i) in items1"
              :key="i"
              @click="funk(i)"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

</template>

<script>
// import profileline from "@/components/common/profileline/profileline";
export default {
    name: "navigation",
    data(){
      return {
        whatapp:'280px',
        msg:"One autumn night",
        tsg:"A crack in a mirror :>",
        drawer:true,
        isshow:'none',
        items1:[
          {
            icon: 'mdi-inbox',
            text: 'Inbox',
          },
          // {
          //   icon: 'mdi-star',
          //   text: 'Star',
          // },
          {
            icon: 'mdi-send',
            text: 'Send',
          },
          {
            icon: 'mdi-email-open',
            text: 'Drafts',
          },
        ],
        items2:[
          {
            icon: 'mdi-home',
            text: 'Home',
          },
          {
            icon: 'mdi-map-marker-radius-outline',
            text: 'Outline',
          },
          {
            icon: 'mdi-message-processing-outline',
            text: 'Talk',
          },
          {
            icon: 'mdi-zodiac-libra',
            text: 'libra',
          },
        ],
        model1:this.$store.state.index,
        model2:null,
        models1:null
      }
    }
    ,
    components:{

    },
  mounted() {
      this.$bus.$on('draws',()=>{
          this.drawer=!this.drawer;
          if(this.drawer===true){
            this.whatapp='280px';
          }else{
            this.whatapp='1px';
          }
      });
      this.$bus.$on('touser',()=>{
          this.model1=this.$store.state.index
      });
  },
  watch:{
  },
  methods:{
    funk(num){
      if(num===0){
        this.$router.push('/')
      }else if(num===1){
        this.$router.push('/upload')
      }else if(num===2){
        this.$router.push('/profile')
      }else{
        this.$router.push('/profile')
      }
    }
  }
}

</script>

<style scoped>
 ::v-deep .v-divider {
   margin:30px 0;
 }
 ::v-deep .v-list {
   padding:10px 20px;
   margin-top: 5px;
 }
 ::v-deep .v-sheet {
   padding: 10px;
   font-size: 18px;
 }
.list1 {
  padding-left:20px ;
  font-weight: lighter;
  color: white;
  width: 200px;
  margin-top:50px;
}
 .toggle {
   background-color: red;
   width: 1px;
 }
</style>
