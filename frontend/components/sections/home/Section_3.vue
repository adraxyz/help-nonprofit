<template>
  <section id="home-section-3" class="padding-level-2">
    <div class="sm-title text-right" v-show="$vuetify.breakpoint.smAndDown">
      <h1 class="section-title">{{ data.title }}</h1>
    </div>
    <v-row no-gutters>
      <v-col cols="12" md="8">
        <v-img class="section-image" :src="sectionGif" contain></v-img>
      </v-col>
      <v-col cols="12" md="4" class="pt-8 pa-md-8 pt-md-0 section-text-col">
        <div class="mb-md-4" v-show="$vuetify.breakpoint.mdAndUp">
          <h1 class="section-title">{{ data.title }}</h1>
        </div>
        <div class="pr-lg-6">
          <span v-html="sectionText" class="text-content"/>
        </div>
        <v-btn class="section-button button-shadow-secondary-left mt-6"
               tile nuxt :to="localePath(checkRoute(sectionButton.to))">
          {{sectionButton.text_0}}
        </v-btn>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  import { checkRoute} from "../../../utils/route.utils";
  export default {
    name: "Section_3",
    props: {
      data: Object
    },
    data: () => ({
      checkRoute: checkRoute
    }),
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      sectionText() {
        return this.data.texts[0].content
      },
      sectionGif() {
        return this.data.images[0].content
      },
      sectionButton() {
        return this.data.buttons[0]
      }
    }
  }
</script>

<style lang="scss">
  #home-section-3 {
    margin-top: 10vh;
    margin-bottom: 5vh;
    .sm-title {
      padding-right: $circle-icon-size - $md-logo-margin;
      margin-bottom: 5vh;
    }
    .section-title {
      line-height: 1;
    }
    .section-image {
      max-height: calc(100vh - #{$md-up-top-bar-height});
      max-width: 100%;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #home-section-3 {
      .section-image {
        max-height: calc(100vh - #{$md-down-top-bar-height});
      }
    }
    @media (max-width: 600px) {
      #home-section-3 {
        .section-text-col {
          padding-left: 0px;
          padding-right: 0px;
        }
      }
    }
  }
</style>
