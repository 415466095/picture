<template>
  <div
    v-scroll="onScroll"
    class="v-gallery"
  >
    <v-filter />

    <v-container
      :fluid="!isScrolling"
      class="transition-swing"
    >
      <v-row
        :no-gutters="!isScrolling"
        class="transition-swing mx-n4"
      >
        <v-col
          v-for="(pic, i) in paginatedPictures"
          :key="pic.src"
          cols="12"
          md="4"
          class="transition-swing"
        >
          <gallery-card
            :src="'data:image/jpg;base64,'+pic.src"
            :datas="pic.rank"
            @click.stop="setPicture(i)"
          />
        </v-col>
      </v-row>
    </v-container>

    <v-responsive
      v-if="paginatedPictures.length <= sdata.length"
      class="white py-12 mx-n3 text-center"
    >
      <v-btn
        text
        @click="page++"
      >
        Load More Works
      </v-btn>
    </v-responsive>

    <gallery-carousel :datas="this.sdata" v-model="dialog" />
  </div>
</template>

<script>
  // Utilities
  import {
    get,
    sync,
  } from 'vuex-pathify'
  import service from "../uitl/request";
  import qs from 'qs'
  export default {
    name: 'Gallery',
    beforeCreate() {
      service({url: '/getpic',method:'post',data:qs.stringify({"name":"1"})})
          .then(response => {
            const { data } = response
            for(let i=0;i<data.data.length;i++){
              this.sdata.push(data.data[i])
            }
            //备用
            this.below = this.sdata;
          })
          .catch(error => {
            console.log(error)
          })
    },
    mounted() {
      this.$bus.$on('result',(data)=>{
        this.sdata = data
      });
      this.$bus.$on('goback',()=>{
        this.sdata = this.below
      });
    },
    components: {
      VFilter: () => import('../components/Filter'),
      GalleryCard: () => import('../components/GalleryCard'),
      GalleryCarousel: () => import('../components/GalleryCarousel'),
    },
    data: () => ({
      dialog: false,
      isScrolling: false,
      page: 1,
      sdata:[],
      below:[],
      initial:0
    }),
    computed: {
      ...sync('photographs', [
        'filter',
        'picture',
      ]),
      pictures: get('photographs/pictures'),
      filteredPictures () {
        console.log('saa')
        // console.log(this.sdata)
        return this.filter === 'All'
          // ? this.pictures(this.srcs):{name:'1',url:'https://picsum.photos/id/1/600/350'}
            ? this.pictures(this.sdata)
          : this.pictures().filter(p => p.category === this.filter)
      },
      paginatedPictures () {
          // console.log(this.filteredPictures.slice(0, this.page * 12))
          console.log(this.sdata)
          if(this.initial===0){
            this.initial=1
            return [{src:'aaa',category:'cat'}]
          }
          console.log(this.filteredPictures.slice(0, this.page * 5))
          console.log(this.sdata.length)
          return this.filteredPictures.slice(0, this.page * 9)
      },
    },
    methods: {
      onScroll () {
        this.isScrolling = window.pageYOffset > 50
      },
      setPicture (index) {
        this.picture = index

        this.$nextTick(() => (this.dialog = true))
      },
    },
  }
</script>

<style lang="sass">
  .gallery
    // max-width: 1280px
</style>
