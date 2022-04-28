import Vue from "vue";
import axios from "axios";
import Cookies from 'js-cookie'

const service=axios.create({
  baseURL:'http://127.0.0.1:1234',
  timeout: 111165000
})

//判断是否为JSON类型
function isJSON(str){
  let jsonData = JSON.stringify(str);
  try {
    return typeof JSON.parse(jsonData) == "object";
  }
  catch (e){
    return false;
  }
}


//取得token密文
service.interceptors.request.use(
    config=>{
      config.headers['Authorization']=Cookies.get('Authorization')
      // console.log(config)
      return config
    },
    error => {
      console.log(error)
      return Promise.reject(error)
    }
)

// cope with the response
service.interceptors.response.use(
    response=>{
      const {data}=response
      // console.log(data.data)
      if(data.data==='hello world'){
        console.log("ok")
        Cookies.set('Authorization','aastart')
      }
      if(isJSON(data.data)){
        let jsonObj = JSON.parse(JSON.stringify(data.data));
        if(Object.prototype.hasOwnProperty.call(jsonObj,"token")){
          console.log('update token');
          // Cookies.set('Authorization',jsonObj.token)
        }}
        else{
          // console.log('not has')
        }
        return response;
      },
    error => {
        console.log(error);
        return Promise.reject(error);
    }
    //   console.log(response)
    //   if(response.data.result==='TRUE'){
    //     return response.data;
    //   }
    // },
    // error => {
    //   console.log(error)
    //   return Promise.reject(error)
    // }
)



export  default service;


