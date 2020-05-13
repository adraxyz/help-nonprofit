<template>
  <div id="bottom-right">
    <v-btn id="contact-button" v-if="$nuxt.$route.path!=localePath('/contacts')"
           color="primary" :to="localePath(checkRoute(contact_button.to))"
           :tile="bigger_button" :fab="!bigger_button"
           @mouseenter="changeButton" @mouseleave="changeButton"
           @mousedown="changeButton" @mouseup="changeButton"
           :class="[{
             'mail-button d-none d-lg-inline-flex': true,
             'bigger-button': bigger_button
           }]">
      <span v-if="bigger_button">{{ contact_button.text_1 }}</span>
      <i class="contact-icon"/>
    </v-btn>
    <v-btn id="donate-button" v-if="$nuxt.$route.path!=localePath('/donations')"
           :to="localePath(checkRoute(donation_button.to))"
           fab dark outlined nuxt active-class="no-active"
           :class="[{
             'd-lg-none error': true,
             'bigger-button bigger-donation-button': bigger_button,
             'small-button': !bigger_button
           }]">
      <span v-if="bigger_button">{{ donation_button.text_1 }}</span>
      <v-icon id="small-icon">mdi-heart</v-icon>
    </v-btn>
  </div>
</template>

<script>
  import {checkRoute} from "../../../utils/route.utils";

  export default {
    name: "BottomRight",
    props: {
      contact_button: Object,
      donation_button: Object,
      small_button: Boolean
    },
    data: () => ({
      big_button: false,
      checkRoute: checkRoute
    }),
    computed: {
      bigger_button () {
        return this.big_button || !this.small_button
      }
    },
    methods: {
      changeButton() {
        if (this.$vuetify.breakpoint.mdAndUp) {
          this.big_button = !this.big_button
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  #bottom-right {
    position: fixed;
    right: $logo-margin;
    bottom: $min-margin-y;
    z-index: 2;
    #contact-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom $error-color;
      font-family: 'Crossten ExtraBold' !important;
      text-transform: none;
      font-size: large;
    }
    .mail-button {
      height: $big-button-height;
      width: $big-button-height;
    }
    #donate-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom $primary-color !important;
      z-index: 2;
      font-size: large;
    }
    .bigger-button {
      height: $big-button-height;
      width: $bigger-button-width;
      border-top-right-radius: $big-button-height/2;
      border-bottom-right-radius: $big-button-height/2;
      border-top-left-radius: 0%;
      border-bottom-left-radius: 0%;
      font-family: 'Crossten ExtraBold';
      justify-content: space-around !important;
    }
    .bigger-donation-button {
      width: $bigger-button-width * 0.6 !important;
    }
  }
  @media only screen and (min-width: $max-width) {
    #bottom-right {
      right: calc((100vw - #{$max-width})/2 + #{$logo-margin});
    }
  }
  @media only screen and (max-width: $max-width) {
    #bottom-right {
      right: $logo-margin * 0.8;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #bottom-right {
      right: $md-down-logo-margin;
    }
    #donate-button {
      width: $circle-icon-size;
      height: $circle-icon-size;
      text-transform: none;
    }
    .bigger-button {
      height: $circle-icon-size !important;
      max-width: 60vw;
    }
    #small-icon {
      font-size: 20px;
    }
  }
</style>
