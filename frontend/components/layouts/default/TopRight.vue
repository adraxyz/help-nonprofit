<template>
  <div>
    <div id="top-right" class="text-right">

      <!-- Donation button -->
      <v-btn id="top-right-donation-button" :to="localePath(checkRoute(donation_button.to))"
             class="d-none d-lg-inline-flex error-button big-button error"
             tile dark outlined nuxt active-class="no-active">
        {{ donation_button.text_1 }}
      </v-btn>
      <div class="d-block"></div>

      <!-- Christmas button
      <v-btn id="top-right-christmas-button"
             :to="localePath(checkRoute(christmas_button.to))"
             v-if="(!$nuxt.$route.path.includes(localePath('/donations/christmas-2020'))) &&
             christmas_button.active"
             class="mt-4 d-none d-lg-inline-flex error-button"
             tile dark outlined nuxt active-class="no-active">
        {{ christmas_button.text_1 }}
      </v-btn>-->

      <!-- WW store button -->
      <v-btn id="top-right-store-button"
             :href="store_button.href"
             :target="store_button.target"
             v-if="store_button.active"
             class="mt-4 d-none d-lg-inline-flex error-button"
             tile dark outlined nuxt active-class="no-active">
        {{ store_button.text_0 }}
      </v-btn>

      <!-- Burger button -->
      <v-app-bar-nav-icon id="burger-button"
                          class="d-lg-none white-button"
                          @click="drawer=true" outlined/>

      <!-- WW store button mobile -->
      <v-btn id="top-right-store-button-md"
             :href="store_button.href"
             :target="store_button.target"
             v-if="store_button.active"
             class="mt-4 d-block d-lg-none error-button button-shadow-error-left"
             fab dark nuxt small active-class="no-active"
             width="37" height="37" color="primary">
        <v-icon size="24" class="store-button-icon">{{ store_icon }}</v-icon>
      </v-btn>

      <!-- Christmas button mobile
      <v-btn id="top-right-christmas-button-md"
             :to="localePath(checkRoute(christmas_button.to))"
             v-if="(!$nuxt.$route.path.includes(localePath('/donations/christmas-2020'))) &&
             christmas_button.active"
             class="mt-4 d-block d-lg-none error-button button-shadow-error-left"
             fab dark nuxt small active-class="no-active"
             width="37" height="37" color="primary">
        <v-icon size="20" class="christmas-button-icon">{{ gift_icon }}</v-icon>
      </v-btn>-->

      <!-- Christmas shopping cart
      <keep-alive>
        <ShoppingCart v-if="$nuxt.$route.path.includes(localePath('/donations/christmas-2020'))"/>
      </keep-alive>-->

      <!-- Back to the store button
      <div v-if="$nuxt.$route.path.includes(localePath('/donations/christmas-2020')) &&
                 $nuxt.$route.path!=localePath('/donations/christmas-2020')"
           class="back-to-store mt-4 text-left">
        <v-btn class="button-shadow-secondary-left circle-button"
               fab text width="37" height="37"
               :to="localePath(checkRoute(christmas_button.to))">
          <v-icon>{{ left_arrow_icon }}</v-icon>
        </v-btn>
        <span v-show="$vuetify.breakpoint.mdAndUp" class="mr-2">{{ getLabel('back_to_store') }}</span>
      </div>-->

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
        <v-col cols="12" class="text-center extra-button-col" align-self="center">
          <v-btn id="drawer-donation-button" :to="localePath(checkRoute(donation_button.to))"
                 class="nav-button error"
                 tile dark nuxt active-class="no-active">
            {{ donation_button.text_1 }}
          </v-btn>
        </v-col>
        <!--
        <v-col cols="12" class="text-center extra-button-col" align-self="center">
          <v-btn id="drawer-christmas-button"
                 :to="localePath(checkRoute(christmas_button.to))"
                 v-if="(!$nuxt.$route.path.includes(localePath('/donations/christmas-2020'))) &&
                 christmas_button.active"
                 class="nav-button white"
                 tile nuxt active-class="no-active">
            {{ christmas_button.text_1 }}
          </v-btn>
        </v-col>-->

        <!-- WW store drawer button -->
        <v-col cols="12" class="text-center extra-button-col" align-self="center">
          <v-btn id="drawer-store-button"
                 :href="store_button.href"
                 :target="store_button.target"
                 v-if="store_button.active"
                 class="nav-button white"
                 tile nuxt active-class="no-active">
            {{ store_button.text_0 }}
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
import ShoppingCart from "./ShoppingCart";
import { mapState } from 'vuex';
import { mdiGift, mdiArrowLeft, mdiTshirtCrew } from "@mdi/js"

export default {
  name: "TopLeft",
  props: {
    navs: Array,
    section: Object,
    contact_button: Object,
    donation_button: Object,
    christmas_button: Object
  },
  components: {
    ShoppingCart,
    LanguagesSwitcher,
    SocialIcons
  },
  data: () => ({
    drawer: false,
    drawer_height: 0,
    checkRoute: checkRoute,
    gift_icon: mdiGift,
    left_arrow_icon: mdiArrowLeft,
    store_icon: mdiTshirtCrew
  }),
  computed: {
    ...mapState(['privacy_policy', 'cookies_policy', 'terms_of_use', 'shopping_cart_labels']),
    store_button() {
      if (this.section) {
        let btn = this.section.buttons.find(b => b.order == 0)
        if (btn) {
          return btn
        }
      }
      return {active: false}
    }
  },
  methods: {
    onResize () {
      this.drawer_height = window.innerHeight
    },
    getLabel(item) {
      if (this.shopping_cart_labels instanceof Array) {
        let label = this.shopping_cart_labels.find(l => l.item === item)
        if (label) {
          return label.label
        }
      }
      return ''
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
    #top-right-christmas-button {
      background-color: $primary-color !important;
      box-shadow: -$box-shadow-side $box-shadow-bottom $error-color !important;
      font-size: large;
      border-width: 0px !important;
    }
    #top-right-store-button {
      background-color: $primary-color !important;
      box-shadow: -$box-shadow-side $box-shadow-bottom $error-color !important;
      font-size: large;
      border-width: 0px !important;
    }
    .christmas-button-icon {
      width: $circle-icon-size !important;
      height: $circle-icon-size !important;
    }
    .store-button-icon {
      width: $circle-icon-size !important;
      height: $circle-icon-size !important;
    }
    #burger-button {
      margin-top: $logo-size/2 - $circle-icon-size/2;
    }
    #shopping-cart {
      width: 100%;
    }
    .circle-button {
      border: 2px solid black !important;
    }
    .back-to-store {
      font-family: "Crossten Book";
      letter-spacing: 0.15rem !important;
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
    #drawer-christmas-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom $error-color !important;
      font-family: "Crossten ExtraBold";
      border: 2px solid black !important;
    }
    #drawer-store-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom $error-color !important;
      font-family: "Crossten ExtraBold";
      border: 2px solid black !important;
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
        .extra-button-col {
          max-width: 50%;
          display: inline;
        }
        #drawer-donation-button {
          margin-left: 10px !important;
        }
        #drawer-christmas-button {
          margin-left: 15px !important;
        }
        #drawer-store-button {
          margin-left: 15px !important;
        }
      }
    }
  }
</style>
