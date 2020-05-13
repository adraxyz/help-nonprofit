<template>
  <div id="top-left">
    <nuxt-link id="nuxt-logo-link" :to="localePath('/')">
      <transition name="fade" mode="out-in">
        <div id="logo-container" :key="logo.content"
             :style="'background: '+ logoBackgColor + ' url(' + logo.content + ') center center no-repeat;'"/>
      </transition>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  name: "TopLeft",
  props: {
    logo: Object,
    window_width: 0
  },
  computed: {
    logoBackgColor() {
      if (this.logo.content_type === 'alt') {
        return 'transparent'
      }
      return 'white'
    }
  }
}
</script>

<style lang="scss">
  #top-left {
    position: fixed;
    /*left: calc(#{$min-margin-x} - #{$logo-margin});*/
    z-index: 2;
    #logo-container {
      border-radius: 50%;
      border-top-left-radius: 0%;
      height: $md-up-top-bar-height;
      width: $md-up-top-bar-height;
      /*background: white url('~assets/img/HELP_LOGO.png') center center no-repeat;*/
      background-size: 75% !important;
    }
    #nuxt-logo-link {
      width: calc(#{$md-up-top-bar-height} - 18px);
    }
    .fade-enter-active, .fade-leave-active {
      transition: opacity 0.3s;
    }
  }
  @media only screen and (min-width: $max-width) {
    #top-left {
      left: calc((100vw - #{$max-width})/2);
    }
  }
  /* Media queries */
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #top-left {
      #logo-container {
        height: $md-down-top-bar-height;
        width: $md-down-top-bar-height;
      }
      #nuxt-logo-link {
        width: calc(#{$md-down-top-bar-height} - 18px);
      }
    }

  }
</style>
