// STATE
export const state = () => ({
  locales: [],
  locale: '',
  default_layout: {},
  logo: {},
  page_content: {},
  projects: [],
  project: {},
  projects_categories: [],
  products: [],
  product: {},
  shopping_cart: [],
  shopping_cart_labels: {},
  paypal_free_shop: {},
  shop_item_labels: {},
  contact_form_messages: [],
  contact_form_labels: {},
  shipment_form_messages: [],
  shipment_form_labels: {},
  shipment_form_dialog: false,
  privacy_policy: {file: ''},
  cookies_policy: {file: ''},
  terms_of_use: {file: ''},
  cookies_snackbar: {
    show: true,
    content: null
  },
  cookies_preferences: {
    show: false,
    content: null
  },
  cookies_categories: [],
  socials: []
})
// MUTATIONS
export const mutations = {
  SET_LOCALE(state, locale) {
    state.locale = locale
  },
  SET_LOCALES(state, locales) {
    state.locales = locales
  },
  SET_PAGE_CONTENT(state, page_content) {
    state.page_content = page_content
  },
  SET_DEFAULT_LAYOUT(state, layout) {
    state.default_layout = layout
  },
  SET_LOGO(state, logo) {
    state.logo = logo
  },
  SET_PROJECTS(state, projects) {
    state.projects = projects
  },
  SET_PROJECT(state, project) {
    state.project = project
  },
  SET_PROJECTS_CATEGORIES(state, categories) {
    state.projects_categories = categories
  },
  SET_PRODUCTS(state, products) {
    state.products = products
  },
  SET_PRODUCT(state, product) {
    state.product = product
  },
  RESET_SHOPPING_CART(state) {
    state.shopping_cart.forEach(i => i.products = [])
  },
  SET_SHOPPING_CART(state, shopping_cart) {
    state.shopping_cart = shopping_cart
  },
  SET_PAYPAL_FREE_SHOP(state, shop) {
    state.paypal_free_shop = shop
  },
  SET_SHOPPING_CART_LABELS(state, labels) {
    state.shopping_cart_labels = labels
  },
  SET_SHOP_ITEM_LABELS(state, labels) {
    state.shop_item_labels = labels
  },
  ADD_TO_SHOPPING_CART(state, product) {
    state.shopping_cart.find(pc =>
      (pc.order === product.category.order)
      &&
      (pc.products.filter(p => p.order === product.order).length < product.availability)
      &&
      (pc.products.push(product))
    )
  },
  REMOVE_FROM_SHOPPING_CART(state, product) {
    state.shopping_cart.find(pc =>
      (pc.order === product.category.order)
      &&
      (pc.products.find(p => p.order === product.order))
      &&
      (pc.products.splice(
        pc.products.findIndex(p => p.order === product.order),
        1
      ))
    )
  },
  SET_CONTACT_FORM_MESSAGES(state, messages) {
    state.contact_form_messages = messages
  },
  SET_CONTACT_FORM_LABELS(state, labels) {
    state.contact_form_labels = labels
  },
  SET_SHIPMENT_FORM_MESSAGES(state, messages) {
    state.shipment_form_messages = messages
  },
  SET_SHIPMENT_FORM_LABELS(state, labels) {
    state.shipment_form_labels = labels
  },
  SET_SHIPMENT_FORM_DIALOG(state, show) {
    state.shipment_form_dialog = show
  },
  SET_PRIVACY_POLICY(state, doc) {
    state.privacy_policy = doc
  },
  SET_COOKIES_POLICY(state, doc) {
    state.cookies_policy = doc
  },
  SET_TERMS_OF_USE(state, doc) {
    state.terms_of_use = doc
  },
  SHOW_HIDE_COOKIES_SNACKBAR(state, show) {
    state.cookies_snackbar.show = show
  },
  SHOW_HIDE_COOKIES_PREFERENCES(state, show) {
    state.cookies_preferences.show = show
  },
  SET_COOKIES_CATEGORIES(state, cookies_categories) {
    state.cookies_categories = cookies_categories
  },
  SET_COOKIES_SNACKBAR(state, content) {
    state.cookies_snackbar.content = content[0]
  },
  SET_COOKIES_PREFERENCES(state, content) {
    state.cookies_preferences.content = content[0]
  },
  SET_SOCIALS(state, socials) {
    state.socials = socials
  }
}
// ACTIONS
export const actions = {
  setLanguage({commit}, {locale}) {
    commit('SET_LOCALE', locale)
  },
  setLogo({commit, state}, {content_type}) {
    if (state.default_layout && state.default_layout.logo) {
      let logo = state.default_layout.logo.content
      if (content_type && content_type === 'alt') {
        logo = state.default_layout.logo.alt_content
      }
      commit('SET_LOGO', {content: logo, content_type: content_type})
    }
  },
  setShipmentFormDialog({commit}, {show}) {
    commit('SET_SHIPMENT_FORM_DIALOG', show)
  },
  resetShoppingCart({ commit }) {
    commit('RESET_SHOPPING_CART')
  },
  showHideCookiesSnackbar({commit, state}, {show}) {
    commit('SHOW_HIDE_COOKIES_SNACKBAR', show)
  },
  showHideCookiesPreferences({commit, state}, {show}) {
    commit('SHOW_HIDE_COOKIES_PREFERENCES', show)
  },
  async loadDefaultLayout({commit, state}) {
    let response = await this.$axios.get(state.locale + '/api/layouts/default')
    commit('SET_DEFAULT_LAYOUT', response.data)
  },
  async loadPageContent({ commit, state }, { page }) {
    let response = await this.$axios.get(state.locale + '/api/pages/' + page)
    commit('SET_PAGE_CONTENT', response.data)
  },
  async loadProjects({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/projects')
    commit('SET_PROJECTS', response.data)
  },
  async loadProject({ commit, state }, { slug }) {
    let response = await this.$axios.get(
      state.locale + '/api/projects/' + slug,
      {params: {full_data: true}}
    )
    commit('SET_PROJECT', response.data)
  },
  async loadProjectsCategories({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/projects-categories')
    commit('SET_PROJECTS_CATEGORIES', response.data)
  },
  async loadProducts({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/shop/products')
    commit('SET_PRODUCTS', response.data)
  },
  async loadProduct({ commit, state }, { slug }) {
    let response = await this.$axios.get(state.locale + '/api/shop/products/' + slug)
    commit('SET_PROJECT', response.data)
  },
  async loadShoppingCart({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/shop/products-categories')
    let shopping_cart = response.data.filter(pc => pc.internal === true)
    shopping_cart.forEach(i => i.products = [])
    commit('SET_SHOPPING_CART', shopping_cart)
  },
  async loadShoppingCartLabels({ commit, state }) {
    let response = await this.$axios.get(
      state.locale + '/api/labels',
      {params: {topic: 'shopping_cart'}}
    )
    commit('SET_SHOPPING_CART_LABELS', response.data)
  },
  async loadShopItemLabels({ commit, state }) {
    let response = await this.$axios.get(
      state.locale + '/api/labels',
      {params: {topic: 'shop_item'}}
    )
    commit('SET_SHOP_ITEM_LABELS', response.data)
  },
  async addProductToShoppingCart({ commit }, { product }) {
    commit('ADD_TO_SHOPPING_CART', product)
  },
  async removeProductToShoppingCart({ commit }, { product }) {
    commit('REMOVE_FROM_SHOPPING_CART', product)
  },
  async loadPaypalFreeShop({commit, state}) {
    let response = await this.$axios.get(state.locale + '/api/shop/shops/paypal_free_shop')
    commit('SET_PAYPAL_FREE_SHOP', response.data)
  },
  async loadContactFormMessages({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/contact_form')
    commit('SET_CONTACT_FORM_MESSAGES', response.data)
  },
  async loadContactFormLabels({ commit, state }) {
    let response = await this.$axios.get(
      state.locale + '/api/labels',
      {params: {topic: 'contact_form'}}
    )
    commit('SET_CONTACT_FORM_LABELS', response.data)
  },
  async loadShipmentFormMessages({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/shipment_form')
    commit('SET_SHIPMENT_FORM_MESSAGES', response.data)
  },
  async loadShipmentFormLabels({ commit, state }) {
    let response = await this.$axios.get(
      state.locale + '/api/labels',
      {params: {topic: 'shipment_form'}}
    )
    commit('SET_SHIPMENT_FORM_LABELS', response.data)
  },
  async loadPrivacyPolicy({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/documents/privacy_policy')
    commit('SET_PRIVACY_POLICY', response.data)
  },
  async loadCookiesPolicy({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/documents/cookies_policy')
    commit('SET_COOKIES_POLICY', response.data)
  },
  async loadTermsOfUse({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/documents/terms_of_use')
    commit('SET_TERMS_OF_USE', response.data)
  },
  async loadCookiesCategories({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/cookies_categories')
    commit('SET_COOKIES_CATEGORIES', response.data)
  },
  async loadCookiesSnackbar({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/cookies_snackbar')
    commit('SET_COOKIES_SNACKBAR', response.data)
  },
  async loadCookiesPreferences({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/cookies_preferences')
    commit('SET_COOKIES_PREFERENCES', response.data)
  },
  async loadSocials({ commit, state }) {
    let response = await this.$axios.get(state.locale + '/api/socials')
    commit('SET_SOCIALS', response.data)
  },
  async nuxtServerInit({ commit, state, dispatch }, { app }) {
    commit('SET_LOCALE', app.i18n.locale)
    commit('SET_LOCALES', app.i18n.locales)
    try {
      let response = await this.$axios.get(state.locale + '/api/layouts/default')
      commit('SET_DEFAULT_LAYOUT', response.data)
      await dispatch('loadPrivacyPolicy')
      await dispatch('loadCookiesPolicy')
      await dispatch('loadTermsOfUse')
    } catch (e) {
      // console.log(e)
    }
  }
}
// GETTERS
export const getters =  {
  getSectionImage: (state) => (order, section) => {
    return state.page_content.sections.find(s => s.order === section).images.find(i => i.order === order)
  }
}
