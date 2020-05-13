export default function ({ app, store }) {
  // beforeLanguageSwitch called right before setting a new locale
  app.i18n.beforeLanguageSwitch = (oldLocale, newLocale) => {
    store.dispatch('setLanguage', { locale: newLocale })
    store.dispatch('loadDefaultLayout')
  }
}
