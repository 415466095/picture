// Utilities
import { make } from 'vuex-pathify'
import service from "../../uitl/request";

let image = -1
let picturelist = []
const categories = [
  'All',
  'Interior',
  'Buildings',
  'Fashion',
  'Nature',
  'Lifestyle',
]
var pop1 = []
const state = {
  categories,
  filter: 'All',
  picture: null,
  pictures:function (pop) {
    // console.log(pop.length)
    pop1 = JSON.parse((JSON.stringify(pop)))

    console.log(pop1[0].name)
      return Array.from({length: pop.length}).map(() => {
        image++
        if (image>=pop.length){
          image=0
        }
        // console.log(image)
        return {
          src: `${pop1[image].url}`,
          rank: `${pop1[image].rank}`,
          category: categories[Math.floor(Math.random() * categories.length)],
        }
      })
    // }


  }
      // Array.from({ length: 30 }).map(() => {
      //   image++
      //   return {
      //     src: `https://picsum.photos/id/${image}/600/350`,
      //     // src: `data:image/jpg;base64,'+${picturelist[image].url}`,
      //     category: categories[Math.floor(Math.random() * categories.length)],
      //   }
      // }),
}

const mutations = make.mutations(state)

export default {
  namespaced: true,
  state,
  mutations,
}
// if(image<=picturelist.length-1){
//   console.log("?")
//   return `data:image/jpg;base64,'+${picturelist[image].url}`
// }else{
//   return `https://picsum.photos/id/${image}/600/350`
// }
