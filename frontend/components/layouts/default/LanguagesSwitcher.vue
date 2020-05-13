<template>
  <div class="lang-container text-center">
    <nuxt-link v-for="lang in availableLocales" :key="lang.code"
               class="country-flag-icon" :to="switchLocalePath(lang.code)">
      <v-btn v-if="drawer" fab outlined color="white" class="rounded-btn">
        {{ lang.code }}
      </v-btn>
      <CountryFlag v-if="!drawer" class="country-flag-icon" :iso="lang.iso" mode="rounded"/>
    </nuxt-link>
  </div>
</template>

<script>
  import CountryFlag from '@dzangolab/vue-country-flag-icon'
  import { mapState } from 'vuex'
  export default {
    name: "LanguagesSwitcher",
    props: {
      drawer: Boolean
    },
    components: {
      CountryFlag
    },
    computed: {
      ...mapState(['locales', 'locale']),
      availableLocales () {
        return this.locales.filter(i => i.code !== this.locale)
      }
    }
  }
</script>

<style lang="scss">
  @import '~@dzangolab/vue-country-flag-icon/src/assets/scss/country-flag.scss';
  .lang-container {
    height: $circle-icon-size;
    width: $circle-icon-size;
    display: table-cell;
    /*margin-left: $md-up-top-bar-height/2 - $circle-icon-size/2 - 18px;*/
  }
  .country-flag-icon {
    width: 100% !important;
    height: 100% !important;
    display: grid;
    /*border: 1px solid black;*/
  }
  .flag-icon {
    box-shadow: $box-shadow-side $box-shadow-bottom white !important;
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #switcher-container {
      /*left: 0px;*/
    }
  }
</style>
