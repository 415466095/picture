<template>
  <v-dialog
    v-model="value"
    fullscreen
    transition="fade-transition"
  >
    <v-card
      color="grey darken-4"
      dark
    >
      <v-app-bar
        color="rgba(0, 0, 0, .6)"
        fixed
        flat
      >
        {{ picture + 1 }} / {{ this.datas.length }}
        <v-spacer />

        <v-btn
          class="mx-1 mx-md-3"
          icon
          small
          @click="zoomed = !zoomed"
        >
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-btn
          class="mx-1 mx-md-3"
          icon
          small
          @click="toggleFullscreen"
        >
          <v-icon>mdi-arrow-expand-all</v-icon>
        </v-btn>
<!--        <v-menu-->
<!--          bottom-->
<!--          left-->
<!--          offset-y-->
<!--        >-->
<!--        下面为评价板块-->
        <v-row style="margin-left: 3px">
          <v-dialog
              v-model="dialogone"
              scrollable
              max-width="300px"
          >
            <template v-slot:activator="{ attrs, on }">
              <v-btn
                  icon
                  small
                  class="mx-1 mx-md-3"
                  v-bind="attrs"
                  v-on="on"
              >
                <v-icon>mdi-star-outline</v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-card-title>图片评分等级：</v-card-title>
              <v-divider></v-divider>
              <v-card-text style="height: 300px;">
                <v-radio-group
                    v-model="dialogm1.star"
                    column
                >
                  <v-radio style="margin-top: 13px"
                      label="1(我认为这张图很糟糕)"
                      value="1"
                  ></v-radio>
                  <v-radio style="margin-top: 13px"
                      label="2(我认为这张图质量较差)"
                      value="2"
                  ></v-radio>
                  <v-radio style="margin-top: 13px"
                      label="3(我认为这张图比较一般)"
                      value="3"
                  ></v-radio>
                  <v-radio style="margin-top: 13px"
                      label="4(我认为这张图不错)"
                      value="4"
                  ></v-radio>
                  <v-radio style="margin-top: 13px"
                      label="5(我认为这张图棒极了)"
                      value="5"
                  ></v-radio>
                </v-radio-group>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
<!--                <v-btn-->
<!--                    color="blue darken-1"-->
<!--                    text-->
<!--                    @click="dialog = false"-->
<!--                >-->
<!--                  Save-->
<!--                </v-btn>-->
                <v-row><v-dialog
                    v-model="dialogtwo"
                    persistent
                    max-width="350">
                  <template v-slot:activator="{ attrs, on }">
                    <v-btn
                        color="blue darken-1"
                        text
                        v-bind="attrs"
                        v-on="on"
                        @click=""
                    >
                      Save
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title class="text-h5">
                      你确定要给{{this.ranksname}}打分吗?
                    </v-card-title>
                    <v-card-text>用户的主观打分将体现在图片的总分中，注意
                    每位用户一次只能为一张图打一次分数，如果重复打分那么最新一次的分数将覆盖你上次一
                      对本图片的打分哦！
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="green darken-1"
                          style="margin-right: 150px"
                          text
                          @click="dialogtwo = false"
                      >
                        Disagree
                      </v-btn>
                        <v-btn
                            color="green darken-1"
                            text
                            @click="dafen"
                            >
                          Submit
                        </v-btn>
                    </v-card-actions>
                  </v-card>
                  </v-dialog></v-row>
<!--                sss-->
                <v-btn
                    color="blue darken-1"
                    text
                    @click="dialogone = false"
                    style="margin-left: 150px "
                >
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
<!--          <template v-slot:activator="{ attrs, on }">-->
<!--            <v-btn-->
<!--              icon-->
<!--              small-->
<!--              class="mx-1 mx-md-3"-->
<!--              v-bind="attrs"-->
<!--              v-on="on"-->
<!--            >-->
<!--              <v-icon>mdi-share</v-icon>-->
<!--            </v-btn>-->
<!--          </template>-->
<!--          <v-list dense>-->
<!--            <v-list-item link>-->
<!--              <v-list-item-title @click="dafen">为该图片打分</v-list-item-title>-->
<!--            </v-list-item>-->

<!--            <v-list-item link>-->
<!--              <v-list-item-title @click="label">为该图片贴标签</v-list-item-title>-->
<!--            </v-list-item>-->

<!--            <v-list-item link>-->
<!--              <v-list-item-title>Share on Instagram</v-list-item-title>-->
<!--            </v-list-item>-->
<!--          </v-list>-->
<!--        </v-menu>-->
          </v-row>


<!--        下面为标签板块-->
        <v-row style="margin-left: -1008px;margin-top: -10px">
          <v-dialog
              v-model="dialogthree"
              persistent
              max-width="600px"
          >
            <template v-slot:activator="{ attrs, on }">
              <v-btn
                  icon
                  small
                  v-bind="attrs"
                  v-on="on"
              >
                <v-icon>mdi-tag-multiple-outline</v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">请填写你要为本图打的标签:</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <v-text-field v-model="name"
                                    :error-messages="nameErrors"
                                    :counter="10"
                                    label="Name"
                                    required
                                    @input="$v.name.$touch()"
                                    @blur="$v.name.$touch()"
                      >
                      </v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="clear"
                >
                  Close
                </v-btn>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="tipsub"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>


        <v-btn
          class="mx-1 mx-md-3"
          icon
          small
          @click="$emit('change', false)"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-app-bar>

      <v-responsive min-height="100vh">
        <v-container
          class="pa-0 fill-height"
          fluid
        >
          <v-row
            align="center"
            class="fill-height mx-0"
            style="max-width: 100%;"
          >
            <v-carousel
              v-model="picture"
              height="700"
              hide-delimiters
            >
              <v-carousel-item
                v-for="(pic, i) in this.datas"
                :key="i"
                :class="{
                  'v-carousel-item--zoomed': zoomed
                }"
                :src="'data:image/jpg;base64,'+pic.url"
              />
            </v-carousel>
          </v-row>
        </v-container>
      </v-responsive>
    </v-card>
  </v-dialog>
</template>

<script>
  // Mixins
  import Proxyable from 'vuetify/lib/mixins/proxyable'
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
  // Utilities
  import {
    get,
    sync,
  } from 'vuex-pathify'
  import axios from "axios";
  import service from "../uitl/request";
  import qs from 'qs'
  export default {
    name: 'GalleryCarousel',
    mixins: [Proxyable,validationMixin],
    validations:{
      name:{required,maxLength:maxLength(8)}
    },
    data: () => ({
      name:'',
      isFullscreen: false,
      zoomed: false,
      ranksname:0,
      dialogm1: {name:'',star:''},
      dialogm2: {name:'',label:''},
      dialogone: false,
      dialogtwo: false,
      dialogthree: false,
      dataname:[]
    }),
    props:{
      datas:{
        type:Array
      }
    },
    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
      },
      picture: sync('photographs/picture'),
      pictures: get('photographs/pictures'),
    },
    // beforeMount() {
    //   this.dialogm1=1;
    // },
    watch:{
      //确保图片名称对应
      picture(news,olds){
        // console.log(news+1)
        for(let i=0;i<this.datas.length;i++){
          if(i===news){
            this.ranksname=this.datas[i].name;
          }
        }
        console.log(this.ranksname)
      }
    },
    methods: {
      toggleFullscreen () {
        // console.log("?")
        // console.log(this.pictures)
        // console.log(this.filteredPictures())
        if (document.fullscreenElement) {
          document.exitFullscreen()
          this.isFullscreen = false
        } else {
          document.documentElement.requestFullscreen()
          this.isFullscreen = true
        }
      },
      bitch(pic){
        console.log(pic.name)
      },
      dafen(){
        if(this.dialogm1.star===''){
          alert('请打分！')
          this.dialogtwo=false
        }else{
          this.dialogm1.name=this.ranksname
          service({url: '/accountstar',method: 'post',data:qs.stringify(this.dialogm1)})
            .then(response => {
              const { data } = response
              console.log("加载完毕:"+data.data)
            })
            .catch(error => {
              console.log(error)
            })
          console.log(this.dialogm1.star)
          alert("你的打分已提交，感谢你的贡献！")
          this.dialogone=false
        }
      },
      fenshu(){

      },
      label(){

      },
      loadover(data){
        // this.ranksname=data
        // console.log(this.dataname)
      },
      submit(){
        this.$v.$touch()
      },
      clear(){
        this.$v.$reset()
        this.name = ''
        this.dialogthree = false
      },
      tipsub(){
        if(this.name===''){
          alert("输入为空！")
          return "不能为空"
        }
        this.dialogm2.name = this.ranksname;
        this.dialogm2.label = this.name;
        service({url: '/labels',method: 'post',data:qs.stringify(this.dialogm2)})
            .then(response => {
              const { data } = response
              alert(data.data.msg)
              console.log("加载完毕:"+data.data.msg)
            })
            .catch(error => {
              console.log(error)
            })
        this.name = ''
        this.dialogthree = false
      }
    },
  }
</script>

<style lang="sass">
  .v-carousel-item--zoomed .v-image__image
    transform: scale(1.2)
</style>
