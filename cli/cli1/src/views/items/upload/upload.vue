<template>
<!--  <div style="margin-left: 40px">-->
<!--    <h1>upload your own pictures in the down area!</h1>-->
<!--    <div class="hello">-->
<!--      <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"></vue-dropzone>-->
<!--    </div>-->
<!--  </div>-->
  <div class="hello" style="margin-top: 40px">
    <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"
    @vdropzone-file-added="funk" @vdropzone-success="dddd"
    @vdropzone-removed-file="removed"
    ></vue-dropzone>
    <v-btn style="margin-left: 50%;
    transform: translateX(-50%);
    margin-top: 20px;
     font-size: large;border: 1px solid slateblue"
            @click="funks"
            :loading="loading3"
            :disabled="loading3"
            color="blue-grey"
    >Upload
      <v-icon
          right
          dark
      >
        mdi-cloud-upload
      </v-icon></v-btn>
  </div>
</template>

<script>
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import service from "../../../uitl/request";
import Cookies from "js-cookie";
import qs from 'qs'
import vuexStore from "../../../store";

export default {
  name: "upload",
  components: {
    vueDropzone: vue2Dropzone
  },
  // props: {
  //   msg: String
  // },
  beforeCreate() {
    this.$store.commit("getindex",2)
  },
  data : function (){
    return {
      pics:[],
      dropzoneOptions: {
        // url: 'https://httpbin.org/post',
        // thumbnailWidth: 150,
        // maxFilesize: 0.5,
        // headers: { "My-Awesome-Header": "header value" }
        url: 'https://httpbin.org/post',
        thumbnailWidth: 200,
        addRemoveLinks: true,
        size:5.0,
      },
      loader: null,
      loading3: false,
    }
  },
  watch: {
    loader () {
      const l = this.loader
      this[l] = !this[l]

      setTimeout(() => (this[l] = false), 3000)

      this.loader = null
    },
  },
  methods:{
    funk(file){
      console.log(file+"好了")
    },
    dddd(file,response){
      this.pics.push(file)
    },
    funks(){
      this.loader = 'loading3'
      let picture = []
      console.log(this.pics)
      for(let i=0;i<this.pics.length;i++){
          var obj={}
          obj.name = this.pics[i].name
          obj.url=this.pics[i].dataURL
          picture.push(obj)
      }
      console.log(picture)
      service({url:'/rankpic',method:'post',data:qs.stringify(picture)})
          .then(response=>{
            const {data}=response;
            this.datas=data.data;
            // console.log(this.datas)
            alert("成功上传打分！请至主页查看!")
          })
          .catch(error=>{
            console.log(error)
          })
    },
    removed(file){
      console.log(this.pics)
      console.log(file)
      for(let i=0;i<this.pics.length;i++) {
        if(this.pics[i].name===file.name){
            // console.log(this.pics[i].name)
            if(i===0){
              this.pics.shift()
            }
            else{
              this.pics.splice(i,1)
            }
        }
      }
    }
  }
}
</script>

<style scoped>
.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}
@-moz-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-o-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
