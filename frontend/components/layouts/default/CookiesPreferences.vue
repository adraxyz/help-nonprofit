<template>

  <!-- Cookies preferences dialog -->
  <v-dialog v-model="cookies_preferences.show" class="cookies-preferences"
            scrollable persistent max-width="800px">
    <div class="cookies-dialog-container pa-4 pb-0">
      <v-row no-gutters align="center">
        <v-col>
          <h1 class="cookies-title">{{cookies_preferences.content.title}}</h1>
        </v-col>
        <v-col>
          <v-icon class="float-right" @click="hideCookiesPreferences">
            {{ close_icon }}
          </v-icon>
        </v-col>
      </v-row>
      <div class="cookies-form-container mt-4">
        <div class="mb-4" v-html="cookies_preferences.content.info_text"/>
        <v-expansion-panels :accordion="true" :multiple="true" :hover="true" :tile="true" :flat="true">
          <v-expansion-panel v-for="cc in cookies_categories" :key="cc.name" class="cookies-panel">
            <v-expansion-panel-header>{{cc.title}}</v-expansion-panel-header>
            <v-expansion-panel-content>
              <span>{{cc.description}}</span>
              <div v-for="provider in cc.cookies_providers" :key="provider.name">
                <v-row no-gutters align="center" align-content="space-between">
                  <v-col>
                    <span class="cookie-provider-title">{{provider.title}}</span>
                  </v-col>
                  <v-col>
                  <v-switch @change="onSwitch(provider)" class="float-right"
                            :input-value="provider.default" :readonly="provider.readonly"/>
                  </v-col>
                </v-row>
                <div v-for="c in provider.cookies" :key="c.name">
                <div class="cookies-description d-inline-block mb-3">
                  <span class="d-block pb-2 cookies-name">{{c.name}}</span>
                  <span>{{c.purpose}}</span>
                </div>
                </div>
              </div>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
        <v-row no-gutters align="center" class="mt-6 mb-6">
          <v-col>
            <v-btn class="button-shadow-secondary-right section-button cookies-button float-left"
              tile active-class="nav-active" @click="hideCookiesPreferences">
              {{cookies_preferences.content.save_button_label}}
            </v-btn>
          </v-col>
          <v-col class="text-right">
            <v-btn class="button-shadow-error-left section-button cookies-button"
              tile active-class="nav-active" @click="rejectAll">
              {{cookies_preferences.content.reject_all_button_label}}
            </v-btn>
          </v-col>
          <v-col class="text-right">
            <v-btn class="button-shadow-primary-left section-button cookies-button"
              tile active-class="nav-active" @click="acceptAll">
              {{cookies_preferences.content.accept_all_button_label}}
            </v-btn>
          </v-col>
        </v-row>
      </div>
    </div>
  </v-dialog>

</template>

<script>
  import { mapState } from 'vuex';
  import { mdiCloseThick } from '@mdi/js'

  export default {
    name: "Cookies",
    computed: {
      ...mapState(['cookies_preferences', 'cookies_policy', 'cookies_categories'])
    },
    data: () => ({
      close_icon: mdiCloseThick,
      accept: false
    }),
    async fetch() {
      await this.$store.dispatch('loadCookiesCategories')
      await this.$store.dispatch('loadCookiesPreferences')
    },
    methods: {
      hideCookiesSnackbar() {
        this.$store.dispatch('showHideCookiesSnackbar', {show: false})
      },
      showCookiesPreferences() {
        this.$store.dispatch('showHideCookiesPreferences', {show: true})
      },
      hideCookiesPreferences() {
        this.$store.dispatch('showHideCookiesPreferences', {show: false})
      },
      acceptAll() {
        this.hideCookiesSnackbar()
        this.hideCookiesPreferences()
        this.$ga.enable()
        this.$fb.enable()
      },
      rejectAll() {
        this.hideCookiesSnackbar()
        this.hideCookiesPreferences()
        this.$ga.disable()
        // this.$cookies.removeAll()
        this.cookies_categories.forEach(
          cc => cc.cookies_providers.forEach(
            cp => cp.cookies.forEach(
              c => this.$cookies.remove(c.name)
            )
          )
        )
      },
      onSwitch(provider) {
        this.accept = !this.accept
        if (this.accept) {
          if (provider.name === 'google_analytics') {
            this.$ga.enable()
          } else if (provider.name === 'facebook') {
            this.$fb.enable()
          }
        } else {
          if (provider.name === 'google_analytics') {
            this.$ga.disable()
          } else if (provider.name === 'facebook') {
            provider.cookies.forEach(
              c => this.$cookies.remove(c.name)
            )
          }
        }
      }
    }
  }
</script>

<style lang="scss">
  .v-dialog {
    background-color: white;
  }
  .cookies-preferences {
    z-index: 1001;
  }
  .cookies-dialog-container {
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
      cursor: pointer;
    }
    .v-expansion-panel-header {
      font-family: "Crossten SemiBold";
      letter-spacing: 0.15rem;
    }
    .cookies-title {
      font-family: "Crossten ExtraBold" !important;
    }
    .cookies-description {
      font-family: "Crossten Thin";
    }
    .cookies-name {
      font-family: "Crossten Book";
    }
    .cookies-button {
      font-size: $font-size-15 !important;
      padding: 8px !important;
      margin: 0 !important;
    }
    .cookie-provider-title {
      font-family: "Crossten SemiBold";
    }
    .cookies-panel {
      border: 2px solid black;
      margin-top: 6px !important;
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    .cookies-dialog-container {
      font-size: $font-size-12;
      .v-expansion-panel-header {
        font-size: $font-size-12;
      }
      .cookies-button {
        margin-top: 12px !important;
      }
      .cookies-button {
        padding: 6px !important;
        font-size: $font-size-12 !important;
      }
    }
  }
</style>
