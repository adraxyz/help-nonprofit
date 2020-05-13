<template>
  <div id="navbar" class="d-none d-lg-block">
    <v-btn v-for="nav in navs" :key="nav.order" tile outlined :to="localePath(checkRoute(nav.name))"
           class="nav-button button-shadow-secondary-left mx-3" nuxt active-class="nav-active">
      {{ nav.title }}
    </v-btn>
  </div>
</template>

<script>
  import {checkRoute} from "../../../utils/route.utils";

  export default {
    name: "Navbar",
    props: {
      navs: Array
    },
    data: () => ({
      checkRoute: checkRoute
    })
  }
</script>

<style lang="scss">
  #navbar {
    position: fixed;
    align-self: center;
    z-index: 2;
    top: calc(#{$md-up-top-bar-height/2} - 20px);
    /*.white-button {
      box-shadow: -$box-shadow-side $box-shadow-bottom $secondary-color;
      color: black !important;
    }
    .nav-button {
      font-size: medium;
    }*/
    /*.nav-active {
      box-shadow: -$box-shadow-side $box-shadow-bottom $primary-color !important;
    }*/
  }
  /* Media queries */
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #navbar {
      top: $md-down-top-bar-height/2 - $nav-button-height/2;
    }
  }
</style>
