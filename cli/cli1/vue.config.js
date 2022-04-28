module.exports = {
  lintOnSave:false,//关闭eslintre语法检查,
  devServer: {
    proxy: {
      '/api': {
        // 此处的写法，目的是为了 将 /api 替换成 target
        target: 'http://127.0.0.1:1234',
        // 允许跨域
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/api': '/'
        }
      },
      '/login': {
        // 此处的写法，目的是为了 将 /api 替换成 target
        target: 'http://127.0.0.1:1234',
        // 允许跨域
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/login': '/login'
        }
      },
      '/son': {
        // 此处的写法，目的是为了 将 /api 替换成 target
        target: 'http://127.0.0.1:1234',
        // 允许跨域
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/son': '/son'
        }
      }
      }},
      transpileDependencies: [
        'vuetify'
      ]

}


