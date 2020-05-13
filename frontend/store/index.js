// STATE
export const state = () => ({
  locales: [],
  locale: '',
  default_layout: {},
  logo: {},
  privacy_text: '',
  page_content: {},
  projects: [],
  project: {},
  projects_categories: [],
  contact_form_messages: [],
  contact_form_labels: {}
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
  SET_PRIVACY_TEXT(state, text) {
    state.privacy_text = text
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
  SET_CONTACT_FORM_MESSAGES(state, messages) {
    state.contact_form_messages = messages
  },
  SET_CONTACT_FORM_LABELS(state, labels) {
    state.contact_form_labels = labels
  }
}
// ACTIONS
export const actions = {
  setLanguage({commit}, {locale}) {
    commit('SET_LOCALE', locale)
  },
  setLogo({commit, state}, {content_type}) {
    if (state.default_layout) {
      let logo = state.default_layout.logo.content
      if (content_type && content_type === 'alt') {
        logo = state.default_layout.logo.alt_content
      }
      commit('SET_LOGO', {content: logo, content_type: content_type})
    }
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
    let response = await this.$axios.get(state.locale + '/api/projects-categories/')
    commit('SET_PROJECTS_CATEGORIES', response.data)
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
  async nuxtServerInit({ commit, state }, { app }) {
    commit('SET_LOCALE', app.i18n.locale)
    commit('SET_LOCALES', app.i18n.locales)
    try {
      let response = await this.$axios.get(state.locale + '/api/layouts/default')
      commit('SET_DEFAULT_LAYOUT', response.data)
      commit('SET_PRIVACY_TEXT', response.data.privacy_text)
      // commit('SET_LOGO', {content: response.data.logo.content, content_type: ''})
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
