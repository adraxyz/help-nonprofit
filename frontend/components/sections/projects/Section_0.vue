<template>
  <section id="projects-section-0" class="padding-level-3" v-resize="onResize">
      <v-row no-gutters class="section-row" align-content="center">
        <v-col cols="12" md="4" order="1" order-md="0" align-self="center" class="section-text">
          <div class="text-title" v-html="baseProject.title"/>
          <div class="text-subtitle" v-html="baseProject.subtitle"/>
          <v-btn :to="localePath(checkRoute('/projects/' + baseProject.slug))"
                 class="section-button button-shadow-error-right"
                 nuxt tile active-class="no-active">
              {{detailsButton.text_0}}
          </v-btn>
        </v-col>
        <v-col cols="12" md="8" order="0" order-md="1" class="image-col">
          <v-img class="section-image" contain
                 :src="$vuetify.breakpoint.mdAndUp ? sectionImage.content : sectionImage.alt_content"/>
        </v-col>
      </v-row>
  </section>
</template>

<script>
import {checkRoute} from "../../../utils/route.utils";

export default {
  name: "Section_0",
  props: {
    data: Object,
    projects: Array
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
    sectionImage() {
      return this.data.images.find(i => i.order === 0)
    },
    baseProject() {
      return this.projects.find(p => p.order === 0)
    },
    detailsButton() {
      return this.baseProject.buttons.find(b => b.order === 0)
    }
  },
  methods: {
    onResize () {
      this.section_height = window.innerHeight
      document.documentElement.style.setProperty('--100vh', `${this.section_height}px`);
    }
  }
}
</script>

<style lang="scss">
  #projects-section-0 {
    padding-top: $logo-size;
    .section-row {
      min-height: calc(var(--100vh) - #{$logo-size});
    }
    .section-text {
      padding-right: 1vw;
    }
    .section-button {
      margin-top: 5vh;
    }
    .section-image {
      max-height: calc(var(--100vh) - #{$logo-size});
      height: 100%;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #projects-section-0 {
      padding-top: $md-logo-size;
      .section-row {
        min-height: calc(var(--100vh) - #{$md-logo-size});
      }
      .section-image {
        max-height: calc(var(--100vh) - #{$md-logo-size});
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #projects-section-0 {
      .section-text {
        margin-top: 2vh;
        margin-bottom: 2vh;
      }
      .section-button {
        margin-top: 3vh;
        margin-bottom: 3vh;
      }
      .text-title {
        margin-bottom: 1vh;
      }
      @media (max-aspect-ratio: 1/1) {
        .section-image {
          max-height: 40vh !important;
        }
      }
    }
    @media (min-aspect-ratio: 1/1) {
      #projects-section-0 {
        .section-text {
          max-width: 50%;
          padding-left: 1vw;
        }
        .image-col {
          max-width: 50%;
        }
      }
    }
  }
</style>
