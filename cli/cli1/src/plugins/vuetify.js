import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import en from '../locale/en'

Vue.use(Vuetify);

Vue.component('signin', {
  methods: {
    changeLocale () {
      this.$vuetify.lang.current = 'en'
    }
  }
})

export default new Vuetify({
  lang:{
    locales:{en},
    current:'en'
  },
  theme:{
    theme:{
      light:{
          primary: '#1976D2',
          secondary: '#424242',
          accent: '#82B1FF',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FFC107',
      },
      dark:{

      }
    }
  }
});
