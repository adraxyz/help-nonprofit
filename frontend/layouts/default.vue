<template>

  <v-app>

    <CookiesSnackbar/>
    <CookiesPreferences/>

    <TopLeft :logo="logo"/>

    <NavBar :navs="default_layout.pages"/>

    <TopRight :navs="default_layout.pages"
              :donation_button="default_layout.donation_button"
              :christmas_button="default_layout.christmas_button"
              :contact_button="default_layout.contact_button"/>

    <transition name="fade">
      <MiddleRight v-show="!hideMiddleRight"/>
    </transition>

    <transition name="fade">
      <BottomLeft class="d-none d-lg-inline-block" v-if="!hideBottom"/>
    </transition>

    <transition name="fade">
      <BottomRight v-if="!hideBottom"
                   :donation_button="default_layout.donation_button"
                   :contact_button="default_layout.contact_button"
                   :small_button="small_button"/>
    </transition>

    <!-- Sizes your content based upon application components -->
    <v-content class="page-container" v-scroll="onScroll">
<!--      <v-content class="elastic-container" v-scroll="onScroll">-->

      <!-- NUXT content -->
      <nuxt/>

      <Footer v-intersect="{handler: onFooterIntersect, options: {threshold: [0, 0.5, 1.0]}}"
              :data="default_layout.footer"
              :donation_button="default_layout.donation_button"
              :contact_button="default_layout.contact_button"/>

    </v-content>

  </v-app>

</template>

<script>
  import TopLeft from "../components/layouts/default/TopLeft";
  import NavBar from "../components/layouts/default/NavBar";
  import TopRight from "../components/layouts/default/TopRight";
  import MiddleRight from "../components/layouts/default/MiddleRight";
  import BottomLeft from "../components/layouts/default/BottomLeft";
  import BottomRight from "../components/layouts/default/BottomRight";
  import Footer from "../components/Footer";
  import { mapState } from 'vuex';
  import CookiesSnackbar from "../components/layouts/default/CookiesSnackbar";
  import CookiesPreferences from "../components/layouts/default/CookiesPreferences";

  export default {
    name: 'default_layout',
    components: {
      CookiesSnackbar,
      CookiesPreferences,
      TopLeft,
      NavBar,
      TopRight,
      MiddleRight,
      BottomLeft,
      BottomRight,
      Footer
    },
    head() {
      return {
        meta: this.default_layout.meta_tags
      }
    },
    data: () => ({
      hideBottom: false,
      hideSocialIcons: false,
      small_button: true
    }),
    computed: {
      ...mapState(['locale', 'default_layout', 'logo']),
      hideMiddleRight() {
        return this.$vuetify.breakpoint.mdAndDown || this.hideSocialIcons
      }
    },
    methods: {
      onScroll (e) {
        // let scrolling_element = e.target.scrollingElement
        // this.small_button = scrolling_element.scrollTop > scrolling_element.clientHeight/4
        //   || scrolling_element.scrollTop === 0
      },
      onFooterIntersect (entries, observer, isIntersecting) {
        let threshold_over = entries[0].intersectionRatio > 0.5
        // this.hideSocialIcons = isIntersecting
        // this.hideBottom = isIntersecting
        this.hideSocialIcons = threshold_over
        this.hideBottom = threshold_over
      }
    },
    mounted() {
      if (process.client && window) {
        window.history.scrollRestoration = 'auto';
        // We listen to the resize event
        // window.addEventListener('resize', () => {
        //   let vh = window.innerHeight * 0.01;
        //   document.documentElement.style.setProperty('--vh', `${vh}px`);
        // });
     }
    }
  }
</script>

<style lang="scss">
  /* Hide scrollbar for Chrome, Safari and Opera */
  body::-webkit-scrollbar {
    display: none;
  }
  /* Hide scrollbar for IE and Edge */
  body {
    -ms-overflow-style: -ms-autohiding-scrollbar;
    overflow-y: -moz-scrollbars-none;
    overflow-x: hidden;
  }
  a {
    outline: none;
    color: inherit;
  }
  a:hover {
      color: black;
      text-decoration: none;
      cursor:pointer;
  }
  .v-btn {
    text-transform: none !important;
  }
  .v-dialog {
    border-radius: unset !important;
    border: 2px solid black;
  }
  .elastic-container {
    align-self: center;
    /*width: $base-width;*/
    /*max-width: $max-width !important;*/
    /*margin-left: $min-margin-x;
    margin-right: $min-margin-x;*/
  }
  /* Buttons */
  .white-button {
    background-color: white !important;
    box-shadow: -$box-shadow-side $box-shadow-bottom #E99F33 !important;
    border: 2px solid black !important;
  }
  .nav-button {
    width: $nav-button-width !important;
    height: $nav-button-height !important;
    border-width: 2px !important;
  }
  .error-button {
    box-shadow: -$box-shadow-side $box-shadow-bottom #3D9D9B !important;
    font-family: 'Crossten ExtraBold';
  }
  .big-button {
    width: $big-button-width !important;
    height: $big-button-height !important;
  }
  .rounded-btn {
    width: $circle-icon-size !important;
    height: $circle-icon-size !important;
    .v-btn__content {
      text-decoration: none;
    }
  }
  .contact-icon {
    height: $circle-icon-size * 0.7;
    width: $circle-icon-size * 0.7;
    background-size: 100% !important;
    background: url('~assets/icons/contact-icon.png') center center no-repeat;
  }
  .underlined-title {
    background-image: linear-gradient(to top, $secondary-color 50%, transparent 0%);
    font-size: 48px;
    font-family: "Crossten Bold";
  }
  .v-btn--active.no-active::before {
    opacity: 0 !important;
  }
  /* TRANSITIONS */
  .fade-enter-active, .fade-leave-active {
    transition: opacity 1.5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
</style>
