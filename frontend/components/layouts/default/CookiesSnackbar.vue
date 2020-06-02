<template>

  <v-snackbar class="cookies-banner" v-model="cookies_snackbar.show"
              :vertical="true" :timeout="0" color="secondary"
              :bottom="true" :left="true">

    <v-row no-gutters align="center" class="head-container">
      <v-col>
        <h1 class="cookies-title">{{cookies_snackbar.content.title}}</h1>
      </v-col>
      <v-col>
        <v-icon class="float-right" @click="hideCookiesSnackbar">
          {{ close_icon }}
        </v-icon>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col v-html="cookies_snackbar.content.info_text">
      </v-col>
    </v-row>

    <v-row no-gutters class="actions-container" align="center">
      <v-col>
        <a @click="showCookiesPreferences">{{cookies_snackbar.content.cookies_preferences_link_label}}</a>
      </v-col>
      <v-col class="text-right">
        <v-btn tile class="button-shadow-primary-left section-button cookies-button"
          @click="acceptAll">
          {{cookies_snackbar.content.accept_button_label}}
        </v-btn>
      </v-col>
    </v-row>

  </v-snackbar>

</template>

<script>
  import { mapState } from 'vuex';
  import { mdiCloseThick } from '@mdi/js'
  export default {
    name: "CookiesSnackbar",
    data: () => ({
      close_icon: mdiCloseThick
    }),
    async fetch() {
      await this.$store.dispatch('loadCookiesSnackbar')
    },
    computed: {
      ...mapState(['privacy_policy', 'cookies_policy', 'terms_of_use', 'cookies_snackbar'])
    },
    methods: {
      hideCookiesSnackbar() {
        this.$store.dispatch('showHideCookiesSnackbar', {show: false})
      },
      showCookiesPreferences() {
        this.$store.dispatch('showHideCookiesPreferences', {show: true})
      },
      acceptAll() {
        this.hideCookiesSnackbar()
        this.$ga.enable()
        this.$fb.enable()
      }
    }
  }
</script>

<style lang="scss">
  .cookies-banner {
    font-family: "Crossten Book";
    letter-spacing: 0.15rem;
    line-height: 110%;
    a {
      outline: none;
      color: inherit;
      text-decoration: none;
      font-family: "Crossten ExtraBold";
    }
    a:hover {
      color: $accent-color;
      cursor:pointer;
    }
    .cookies-title {
      font-family: "Crossten ExtraBold";
    }
    .v-snack__wrapper {
      border-radius: 0 !important;
      border: 2px solid black !important;
    }
    .v-snack__content {
      padding: 16px !important;
    }
    .head-container {
      margin-bottom: 12px;
    }
    .actions-container {
      margin-top: 12px;
    }
    .cookies-button {
      font-size: $font-size-15 !important;
      padding: 8px !important;
      margin: 0 !important;
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    .cookies-banner {
      font-size: $font-size-12 !important;
      .cookies-button {
        font-size: $font-size-12 !important;
        padding: 6px !important;
      }
    }
  }
</style>
