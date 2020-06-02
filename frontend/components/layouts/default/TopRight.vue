<template>
  <div>
    <div id="top-right">
      <!-- Donation button -->
      <v-btn id="top-right-donation-button" :to="localePath(checkRoute(donation_button.to))"
             class="d-none d-lg-inline-flex error-button big-button error"
             tile dark outlined nuxt active-class="no-active">
        {{ donation_button.text_1 }}
      </v-btn>
      <!-- Burger button -->
      <v-app-bar-nav-icon id="burger-button"
                          class="d-lg-none white-button"
                          @click="drawer=true" outlined/>
    </div>
    <!-- Navigation drawer -->
    <v-navigation-drawer id="nav-drawer" color="primary" v-model="drawer" temporary right app
                         v-resize="onResize" :style="`height: ${drawer_height}px;`">

      <v-row no-gutters class="drawer-navigation-row d-inline-block button-row">

        <v-col cols="12" class="button-col text-center" v-for="nav in navs" :key="nav.order" align-self="center">
          <v-btn  tile outlined nuxt :to="localePath(checkRoute(nav.name))"
                  active-class="drawer-nav-active" class="nav-button button-shadow-secondary-left">
            {{ nav.title }}
          </v-btn>
        </v-col>
        <v-col cols="12" class="text-center" align-self="center">
          <v-btn id="drawer-donation-button" :to="localePath(checkRoute(donation_button.to))"
                 class="nav-button error"
                 tile dark nuxt active-class="no-active">
            {{ donation_button.text_1 }}
          </v-btn>
        </v-col>
      </v-row>

      <v-row class="drawer-navigation-row d-inline-block" no-gutters>
        <v-col cols="12" class="mt-3">
          <div class="d-inline-block">
            <SocialIcons class="d-inline-block" :vertical="false" :shadow="false"/>
          </div>
          <div class="d-inline-block float-right ml-3">
            <LanguagesSwitcher :drawer="true" />
          </div>
        </v-col>
        <v-col cols="12" class="drawer-footer-col mt-3">
<!--          <div class="privacy-parent-div d-inline-block">-->
<!--            <div class="privacy-div">-->
<!--              <a class="link-text" :href="privacy_policy.file" target="_blank">Privacy Policy</a>-->
<!--            </div>-->
<!--            <div class="privacy-div">-->
<!--              <a class="link-text" :href="cookies_policy.file" target="_blank">Cookies Policy</a>-->
<!--            </div>-->
<!--            <div class="privacy-div">-->
<!--              <a class="link-text" :href="terms_of_use.file" target="_blank">Terms of use</a>-->
<!--            </div>-->
<!--          </div>-->
          <div class="d-inline-block float-right ml-3">
            <v-btn fab outlined color="white" class="rounded-btn"
                   :to="localePath(checkRoute(contact_button.to))">
              <i class="contact-icon"/>
            </v-btn>
          </div>
        </v-col>
      </v-row>

    </v-navigation-drawer>

  </div>
</template>

<script>
import { checkRoute } from "../../../utils/route.utils";
import SocialIcons from "./SocialIcons";
import LanguagesSwitcher from "./LanguagesSwitcher";
import { mapState } from 'vuex';

export default {
  name: "TopLeft",
  props: {
    navs: Array,
    contact_button: Object,
    donation_button: Object,

  },
  components: {
    LanguagesSwitcher,
    SocialIcons
  },
  data: () => ({
    drawer: false,
    drawer_height: 0,
    checkRoute: checkRoute
  }),
  computed: {
    ...mapState(['privacy_policy', 'cookies_policy', 'terms_of_use'])
  },
  methods: {
    onResize () {
      this.drawer_height = window.innerHeight
    }
  }
}
</script>

<style lang="scss">
  #top-right {
    position: fixed;
    right: $logo-margin;
    z-index: 2;
    #top-right-donation-button {
      margin-top: $logo-size/2 - $big-button-height/2;
      font-size: large;
    }
    #burger-button {
      margin-top: $logo-size/2 - $circle-icon-size/2;
    }
  }
  .v-navigation-drawer {
    width: unset !important;
    padding-top: 40px - 12px;
    padding-left: 40px;
    padding-right: 40px;
    .drawer-navigation-row::-webkit-scrollbar {
      display: none;
    }
    .drawer-navigation-row {
      flex: unset !important;
      -ms-overflow-style: -ms-autohiding-scrollbar;
      overflow-y: -moz-scrollbars-none;
      overflow-x: hidden;
      margin-bottom: calc(#{$logo-size}/2 - #{$circle-icon-size}/2);
    }
    #drawer-donation-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom $darken-primary-color !important;
      font-family: "Crossten ExtraBold";
    }
    .mail-button {
      width: $circle-icon-size !important;
      height: $circle-icon-size !important;
    }
    .nav-button {
      margin-bottom: 20px;
      margin-left: 16px;
      font-size: $font-size-15 !important;
      /*width: 100% !important;*/
      /*min-width: 100% !important;*/
      /*min-height: 45px;*/
    }
    .white-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom #E99F33 !important;
    }
    .error-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom #f06843 !important;
      border-color: black !important;
      border-width: 2px !important;
      background-color: white !important;
    }
    .flag-icon {
      box-shadow: -$box-shadow-side $box-shadow-bottom white !important;
    }
    .contact-icon {
      height: $circle-icon-size * 0.45;
      width: $circle-icon-size * 0.45;
    }
    #drawer-footer-first-div {
      width: 100%;
    }
    .link-text {
      text-decoration: none;
      color: white;
      font-family: "Crossten Medium";
    }
    .drawer-footer-col {
      height: $circle-icon-size;
    }
    .privacy-parent-div {
      height: 100%;
    }
    .privacy-div {
      height: 100%;
      flex-direction: column;
      justify-content: flex-end;
      display: flex;
    }
    .v-btn {
      text-transform: none !important;
      font-size: 1rem;
    }
  }
  .v-navigation-drawer__content {
    /*max-width: 80vw !important;*/
    /*min-width: 30vw !important;*/
    align-self: center;
    flex-direction: column;
    justify-content: space-between;
    display: flex;
  }
  /* Media queries */
  @media only screen and (min-width: $max-width) {
    #top-right {
      right: calc((100vw - #{$max-width})/2 + #{$logo-margin});
    }
  }
  @media only screen and (max-width: $max-width) {
    #top-right {
      right: $logo-margin * 0.8;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #top-right {
      right: $md-logo-margin;
      #top-right-donation-button {
        margin-top: $md-logo-size/2 - $big-button-height/2;
      }
      #burger-button {
        margin-top: $md-logo-size/2 - $circle-icon-size/2;
      }
    }
    .v-navigation-drawer {
      .drawer-navigation-row {
        margin-bottom: calc(#{$md-logo-size}/2 - #{$circle-icon-size}/2);
      }
    }
  }
  @media (max-height: 500px) {
    .v-navigation-drawer {
      padding-top: $md-logo-margin;
    }
    @media (min-aspect-ratio: 1/1) {
      .v-navigation-drawer {
        padding-top: $md-logo-margin;
        padding-left: $md-logo-margin;
        padding-right: $md-logo-margin;
        .button-row {
          max-width: 400px;
        }
        .button-col {
          max-width: 50%;
          display: inline-block;
        }
        .nav-button {
          font-size: $font-size-15 !important;
          margin-left: 0px;
        }
        .drawer-navigation-row {
          margin-bottom: $md-logo-margin !important;
        }
      }
    }
  }
</style>
