<template>
  <div v-on:keyup.enter="search">
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-text-field
            solo-inverted
            hide-details
            label="请输入关键词"
            append-icon="mdi-magnify"
            v-model="text"
            class="input-search"
            autocomplete="off"
            v-on="on"
            ref="search"
            dense
            loading="blue"
            @keyup.enter.native="searchs"
        ></v-text-field>
      </template>
      <v-list v-if="items.length > 0" class="border-list" dense>
        <v-list-item v-for="(item, index) in items" :key="index" @click="itemClick(item)">
          <v-list-item-title>{{ item.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>
<script>
import service from "../../../uitl/request";
import qs from "qs";

export default {
  name:"search",
  data () {
    return {
      text: '',
      showSelect: true,
      items: [],
      mindgame: {}
    }
  },
  watch: {
    text: 'inputHandle'
  },
  methods: {
    itemClick (item) {
      this.text = item.name
      this.$refs.search.blur()
      // this.$router.push()
    },
    inputHandle (text) {
      if (text.trim() !== '') {
        this.showSelect = true
        setTimeout(() => {
          this.getEntity()
        }, 300)
      }
    },
    getEntity () {
      // 请求接口更新 items 数据
      this.items = [
        {
          key: '1234',
          name: '1234'
        },
        {
          key: 'abc',
          name: 'abc'
        },
        {
          key: 'def',
          name: 'def'
        },
        {
          key: 'ccc',
          name: 'ccc'
        },
        {
          key: 'ccc',
          name: 'ccc'
        },
        {
          key: 'ccc',
          name: 'ccc'
        }
      ]
    },
    search () {
      this.$refs.search.blur()
      console.log(this.text)
      // this.$router.push()
    },
    searchs(){
      if(this.text ===''){
        alert("输入为空！")
        this.$bus.$emit("goback")
        return "不能为空"
      }
      this.mindgame.name = this.text
      service({url: '/getlabel',method: 'post',data:qs.stringify(this.mindgame)})
          .then(response => {
            const { data } = response
            console.log(data.data)
            if(data.data!=="没有找到相关标签的图片!"){
              this.$bus.$emit("result",data.data)
            }else{
              // console.log("2")
              alert("未找到相关搜索结果，请换一个标签试试！")
            }
          })
          .catch(error => {
            console.log(error)
          })
    }

  }
}
</script>
<style scoped>
.input-search {
  width: 100%;
  /*margin: auto;*/
}
.width-20-percent {
  width: 20%;
}
.img-div {
  margin: 16vh 0 40px 0;
  text-align: center;
}
.v-menu__content {
  box-shadow: none !important;
}
.border-list {
  border: 1px solid #eee !important;
}
</style>
