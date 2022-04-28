<template>
  <v-hover>
    <template v-slot="{ hover }">
      <v-card
        @click="() => {}"
        v-on="$listeners"
      >
        <v-img
          :class="{
            'v-image--hovered': hover
          }"
          :src="src"
          height="350"
        />

        <v-overlay
          :opacity=".8"
          :value="hover"
          absolute
          z-index="0"
        >
<!--          <v-fade-transition appear>-->
<!--            <v-icon-->
<!--              size="88"-->
<!--              color="#FFFFFFE6"-->
<!--            >-->
<!--              mdi-mdiStar-->
<!--            </v-icon>-->
            <div class="Rating-gray">
              <i v-for="(item,index) in itemClasses" :key="index" class="fa fa-3x" :class="item"></i>
            </div>
<!--          </v-fade-transition>-->
        </v-overlay>
      </v-card>
    </template>
  </v-hover>
</template>

<script>
// 星星长度
import service from "../uitl/request";

const LENGTH = 5;
// 星星对应的class,亮星
const CLS_ON = "fa-star";
// 半星
const CLS_HALF = "fa-star-half-empty";
// 灰星
const CLS_OFF = "fa-star-o";
  export default {
    beforeCreate() {
      // service({url: '/getpic',method: 'post'})
      //     .then(response => {
      //       const { data } = response
      //       for(let i=0;i<data.data.length;i++){
      //         this.funk.push(data.data[i])
      //       }
      //       console.log(this.funk)
      //     })
      //     .catch(error => {
      //       console.log(error)
      //     })
    },
    name: 'GalleryCard',
    inheritAttrs: false,
    props: {
      src: {
        type: String,
        required: true,
      },
      datas:{
        type: String
      }
    },
    data:()=>{
      return {
        // rating: this.datas,
        funk:[]
      }
    },
    mounted() {
      console.log(Math.floor(parseInt(this.datas)))
    },
    computed: {
      itemClasses() {
        // 如4.8 四个全星 1个半星
        let result = [];
        // 对分数进行处理, 向下取0.5的倍数
        let score = Math.floor((parseFloat(this.datas)) * 2) / 2;
        // 控制半星
        let hasDecimal = score % 1 !== 0;
        // 全星
        let integer = Math.floor(score);
        // 全星放入到数组中
        for (let i = 0; i < integer; i++) {
          result.push(CLS_ON);
        }

        // 半星
        if (hasDecimal) {
          result.push(CLS_HALF);
        }

        // 补齐
        while (result.length < LENGTH) {
          result.push(CLS_OFF);
        }

        return result;
      }
    }
  }
</script>

<style lang="sass">
  .v-image
    .v-image__image
      transition: .3s ease
    &.v-image--hovered .v-image__image
      transform: scale(1.2)
  .Rating-gray
      margin-right: 1.066667vw
      color: #2c3e50
      display: inline-block
</style>
