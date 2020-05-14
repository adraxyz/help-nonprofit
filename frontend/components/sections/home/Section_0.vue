<template>
  <section id="home-section-0" v-resize="onResize" :style="`height: ${section_height}px;`">

    <div id="text-area" class="accent">
      <!-- Data row -->
      <v-row no-gutters class="data-row padding-level-2">
        <v-col v-for="t in titles" :key="t.order" cols="12" class="data-col text-center">
          <v-row no-gutters class="data-row-text">
<!--            <v-col cols="6" sm="12" :class="{-->
<!--              'big-title-col': true,-->
<!--              'text-right': $vuetify.breakpoint.xsOnly-->
<!--            }">-->
            <v-col cols="12" class="data-col-text">
              <div>
                <span class="title-number" v-html="t.title"/>
                <span class="text-subtitle" v-html="t.subtitle"/>
              </div>
<!--            </v-col>-->
<!--            <v-col cols="6" sm="12" :class="{-->
<!--              'small-title-col': true,-->
<!--              'pl-2 text-left': $vuetify.breakpoint.xsOnly-->
<!--            }">-->
              <span class="text-content" v-html="t.content"/>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <!-- Action row -->
      <v-row no-gutters id="take-action-row" class="text-center">
        <v-col id="action-col">
          <v-row no-gutters class="action-row padding-level-2 mb-md-1">
            <v-col cols="12" class="text-title" v-html="actionText.title"/>
          </v-row>
          <v-row no-gutters class="action-row padding-level-2 mb-1 mb-md-3 md-down-white-bg">
            <v-col cols="12" class="text-content" v-html="actionText.content"/>
          </v-row>
          <v-row no-gutters class="action-row padding-level-2 md-down-white-bg button-row">
            <v-col cols="12" id="action-button-col">
              <v-btn class="section-button take-action-button" tile nuxt
                     :to="localePath(checkRoute(actionButton.to))" v-intersect="onTextAreaIntersect"
                     @mouseover="show_alternate=true" @mouseleave="show_alternate=false">
                {{actionButton.text_0}}
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

    </div>

    <div>
      <v-img class="base-image" :src="backg_img" :key="backg_img"
             transition="fade" contain></v-img>
    </div>

  </section>
</template>

<script>
  import { checkRoute} from "../../../utils/route.utils";
  export default {
    name: "Section_0",
    props: {
      data: Object
    },
    data: () => ({
      checkRoute: checkRoute,
      section_height: 0,
      show_alternate: false,
      timeoutID: null
    }),
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      titles () {
        return this.data.texts.filter(t => t.order != 4).sort(
          (a, b) => a.order - b.order
        )
      },
      actionText () {
        return this.data.texts.find(t => t.order === 4)
      },
      actionButton () {
        return this.data.buttons[0]
      },
      backg_img () {
        let img = this.data.images.find(i => i.order === 0)
        if (this.show_alternate) {
          return img.alt_content
        }
        return img.content
      }
    },
    methods: {
      onTextAreaIntersect (entries, observer, isIntersecting) {
        let client_rect = entries[0].boundingClientRect
        let content_type = 'alt'
        if (!isIntersecting && client_rect.width>0 && client_rect.height>0) {
          content_type = false
        }
        this.$store.dispatch('setLogo', {content_type: content_type})
      },
      onResize () {
        this.section_height = window.innerHeight
        document.documentElement.style.setProperty('--100vh', `${this.section_height}px`);
      }
    },
    mounted() {
      this.timeoutID = setTimeout(
        () => {
          if (this.$device.isMobileOrTablet) {
            this.show_alternate = true
          }
        },
        5000
      );
    }
  }
</script>

<style lang="scss">
  /* TRANSITIONS */
  .fade-enter-active, .fade-leave-active {
    transition: opacity 1s;
  }
  .fade-enter, .fade-leave {
    opacity: 0.1;
  }
  /* BASE STYLE */
  #home-section-0 {
    position: relative;
    background-size: contain !important;
    #text-area {
      position: absolute;
      color: white;
    }
    .data-row {
      z-index: 1;
      position: relative;
      margin-bottom: 4vh;
    }
    .data-col {
      margin-top: 2vh;
      margin-bottom: 2vh;
    }
    .base-image {
      position: absolute;
      z-index: 0;
      bottom: 0;
      right: 0;
      max-height: calc(var(--100vh) - #{$logo-size});
    }
    .title-number {
      color: $error-color;
      line-height: 100%;
    }
    .text-subtitle {
      font-family: "Crossten Ultra";
      font-size: $font-size-20;
      color: $error-color;
      line-height: 100%;
    }
    .text-content {
      font-family: "Crossten Book";
      line-height: 100%;
      z-index: 1;
    }
    .text-title {
      z-index: 1;
    }
    .take-action-button {
      box-shadow: $box-shadow-side $box-shadow-bottom $error-color !important;
      height: 120% !important;
      text-transform: unset !important;
      font-family: 'Crossten Bold';
      line-height: 100%;
      letter-spacing: 0.1rem;
      font-size: $font-size-20;
      z-index: 1;
    }
  }
  /* MEDIA QUERIES */
  /* HORIZONTAL */
  @media (min-aspect-ratio: 1/1) {
    #home-section-0 {
      #text-area {
        padding-top: $logo-size;
        width: 40%;
        height: var(--100vh);
      }
      .base-image {
        width: 75%;
      }
    }
    @media (max-height: 900px) {
      #home-section-0 {
        .title-number {
          font-size: $font-size-50;
        }
        .text-title {
          font-size: $font-size-30;
        }
        .take-action-button {
          padding: 12px !important;
        }
      }
    }
    @media (max-height: 800px) {
      #home-section-0 {
        .data-row {
          margin-bottom: 2vh;
        }
        .data-col {
          margin-top: 1vh;
          margin-bottom: 1vh;
        }
      }
    }
    @media (max-height: 700px) {
      #home-section-0 {
        #text-area {
          width: 50%;
        }
        .base-image {
          width: 60%;
        }
      }
    }
    @media (max-height: 550px) {
      #home-section-0 {
        #text-area {
          width: 60%;
        }
        .base-image {
          width: 50%;
        }
        .title-number {
          font-size: $font-size-40;
        }
        .text-title {
          font-size: $font-size-25;
        }
        .text-subtitle {
          font-size: $font-size-18;
        }
        .text-content {
          font-size: $font-size-18;
        }
        .take-action-button {
          padding: 10px !important;
          font-size: $font-size-18 !important;
        }
      }
    }
    @media (max-height: 450px) {
      #home-section-0 {
        .take-action-button {
          padding: 6px !important;
          font-size: $font-size-15 !important;
        }
      }
    }
    @media #{map-get($display-breakpoints, 'md-and-down')} {
      #home-section-0 {
        #text-area {
          padding-top: $md-logo-margin;
          width: 50%;
        }
        .base-image {
          width: 60%;
          max-height: calc(var(--100vh) - #{$md-logo-margin});
        }
      }
      @media (max-width: 800px) {
        #home-section-0 {
          .data-col-text {
            text-align: right;
          }
          #take-action-row {
            text-align: left !important;
          }
        }
      }
      @media (max-width: 700px) {
        #home-section-0 {
          .title-number {
            font-size: $font-size-30;
          }
          .text-title {
            font-size: $font-size-20;
          }
          .text-subtitle {
            font-size: $font-size-15;
          }
          .text-content {
            font-size: $font-size-15;
          }
        }
      }
      @media (max-width: 600px) {
        #home-section-0 {
          .title-number {
            font-size: $font-size-25;
          }
          .text-title {
            font-size: $font-size-18;
          }
          .text-subtitle {
            font-size: $font-size-12;
          }
          .text-content {
            font-size: $font-size-12;
          }
          .take-action-button {
            padding: 4px !important;
            font-size: $font-size-12 !important;
          }
          .data-row {
            padding-right: $md-logo-margin;
          }
          .action-row {
            padding-left: $md-logo-margin;
          }
        }
      }
      @media (max-height: 300px) {
        #home-section-0 {
          #text-area {
            width: 55%;
          }
          .base-image {
            width: 53%;
          }
          .data-row {
            margin-bottom: 0px;
          }
          .data-col-text {
            line-height: 100%;
          }
        }
      }
    }
  }
  /* VERTICAL */
  @media (max-aspect-ratio: 1/1) {
    #home-section-0 {
      #text-area {
        width: 100%;
      }
      .base-image {
        width: 100%;
      }
      .md-down-white-bg {
        background-color: white;
        color: $accent-color;
      }
      .action-row {
        margin-bottom: 0px !important;
      }
    }
    @media #{map-get($display-breakpoints, 'md-and-down')} {
      #home-section-0 {
        #text-area {
          padding-top: $md-logo-size;
        }
        .md-down-white-bg {
          padding-top: 1vh;
        }
        .data-row {
          margin-bottom: 2.5vh;
        }
        .data-col {
          margin-top: 0px;
        }
        .button-row {
          padding-top: 2vh;
        }
      }
    }
    @media (max-height: 900px) {
      #home-section-0 {
        #text-area {
          padding-top: $md-logo-size;
        }
        .data-col {
          margin-top: 0px;
          margin-bottom: 2vh;
        }
        .title-number {
          font-size: $font-size-40;
        }
        .text-title {
          font-size: $font-size-30;
        }
        .md-down-white-bg {
          padding-top: 1vh;
        }
        #action-button-col {
          margin-top: 1vh;
        }
      }
    }
    @media (max-height: 800px) {
      #home-section-0 {
        #text-area {
          padding-top: 0px;
        }
        .title-number {
          font-size: $font-size-30;
        }
        .text-title {
          font-size: $font-size-25;
        }
        .text-subtitle {
          font-size: $font-size-15;
        }
        .text-content {
          font-size: $font-size-15;
        }
        .data-row {
          margin-top: 4vh;
          margin-bottom: 2vh;
        }
        .data-col {
          margin-top: 1vh;
          margin-bottom: 1vh;
        }
        .take-action-button {
          padding: 6px !important;
          font-size: $font-size-15 !important;
        }
      }
    }
    @media (max-height: 600px) {
      #home-section-0 {
        .title-number {
          font-size: $font-size-25;
        }
        .text-title {
          font-size: $font-size-18;
        }
        .text-subtitle {
          font-size: $font-size-12;
        }
        .text-content {
          font-size: $font-size-12;
        }
        .data-row-text {
          line-height: 100%;
        }
      }
    }
  }
</style>
