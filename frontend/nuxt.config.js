require('dotenv').config()

export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    titleTemplate: 'HELP %s',
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: '~/components/loading.vue',
  /*
   ** Global CSS
   */
  css: [
    'video.js/dist/video-js.css',
    '~assets/fonts/Crossten/Crossten.css'
  ],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    { src: '~plugins/nuxt-video-player-plugin.js', ssr: true },
    { src: '~plugins/i18n.js'},
    { src: '~plugins/vuelidate', ssr: false }
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    // '@nuxtjs/eslint-module',
    '@nuxtjs/vuetify',
    '@nuxtjs/dotenv'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    // Doc: https://github.com/nuxt-community/dotenv-module
    '@nuxtjs/dotenv',
    '@nuxtjs/proxy',
    '@nuxtjs/device',
    'nuxt-i18n',
    'nuxt-leaflet',
    'cookie-universal-nuxt'
  ],
  i18n: {
    locales: [
      {code: 'it', name: 'Italiano', iso: 'it'},
      {code: 'en', name: 'English', iso: 'gb'}
    ],
    defaultLocale: 'it',
    strategy: 'prefix_except_default',
    parsePages: false
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: process.env.API_BASE_URL
  },
  // proxy: {
    // '/api/': process.env.API_BASE_URL,
  // },
  /*
   ** vuetify module configuration
   ** https://github.com/nuxt-community/vuetify-module
   */
  vuetify: {
    customVariables: [
      '~/assets/scss/variables.scss',
      '~/assets/scss/base.scss'
    ],
    treeShake: true,
    theme: {
      // dark: true,
      themes: {
        dark: {
          primary: "#3D9D9B",
          secondary: "#E99F33",
          accent: "#2E637D",
          error: "#F06843",
          success: "#6A9682",
          warning: "#D97827",
          info: "#751C49",
          grey: "#53626b",
          tile: "#fb8c2a",
          bordeaux: "#8e4152"
        },
        light: {
          primary: "#3D9D9B",
          secondary: "#E99F33",
          accent: "#2E637D",
          error: "#F06843",
          success: "#6A9682",
          warning: "#D97827",
          info: "#751C49",
          grey: "#53626b",
          tile: "#fb8c2a",
          bordeaux: "#8e4152"
        }
      }
    }
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {}
  }
  // server: {
  //   port: "3000",
  //   host: "0.0.0.0"
  // }
}
