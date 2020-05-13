<template>
  <section id="fivepermille-section-0" class="padding-level-3" v-resize="onResize">

    <div class="section-text">

      <div class="text-title" v-html="sectionText.content"/>

      <v-img v-if="show_image_middle" :src="sectionImage.alt_content"
             contain class="section-image"/>

      <div class="section-text-titles">
        <span class="text-subtitle d-block" v-html="sectionText.title"/>
        <span class="text-content" v-html="sectionText.subtitle"/>
      </div>

    </div>

    <v-img v-if="!show_image_middle"
           :src="$vuetify.breakpoint.smAndDown ? sectionImage.alt_content : sectionImage.content"
           contain class="section-image"/>

  </section>
</template>

<script>
  export default {
    name: "Section_0",
    props: {
      data: Object
    },
    data: () => ({
      section_height: 0,
      show_image_middle: false
    }),
    computed: {
      sectionText() {
        return this.data.texts.find(t => t.order === 0)
      },
      sectionImage() {
        return this.data.images.find(i => i.order === 0)
      }
    },
    methods: {
      onResize () {
        this.section_height = window.innerHeight
        document.documentElement.style.setProperty('--100vh', `${this.section_height}px`);
        if (window.innerWidth/window.innerHeight < 1) {
          this.show_image_middle = true
        } else {
          this.show_image_middle = false
        }
      }
    }
  }
</script>

<style lang="scss">
  #fivepermille-section-0 {
    background-size: contain !important;
    margin-top: $logo-size;
    min-height: calc(var(--100vh) - #{$logo-size});
    display: flex;
    flex-direction: column;
    justify-content: center;
    .section-image {
      max-height: calc(var(--100vh) - #{$logo-size} - #{$logo-margin});
    }
    .section-text-titles {
      margin-top: 5vh;
    }
    .text-content {
      font-family: "Crossten Bold";
      font-size: $font-size-40;
    }
  }
  @media (min-aspect-ratio: 1/1) {
    #fivepermille-section-0 {
      .section-text {
        position: absolute;
        top: calc(#{$logo-size} + #{$logo-margin} + 5vh);
        max-width: 40%;
      }
    }
  }
  @media (max-aspect-ratio: 1/1) {
    #fivepermille-section-0 {
      .section-text {
        max-width: 100%;
        position: relative;
        text-align: center;
      }
      .text-title {
        margin-bottom: 3vh;
        padding-left: 10%;
        padding-right: 10%;
      }
      .section-image {
        max-width: 100%;
        left: unset;
        max-height: 50vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #fivepermille-section-0 {
      margin-top: $md-logo-size;
      min-height: calc(var(--100vh) - #{$md-logo-size});
      @media (min-aspect-ratio: 1/1) {
        .section-image {
          max-height: calc(var(--100vh) - #{$md-logo-size} - #{$md-logo-margin});
        }
      }
      @media (max-height: 700px) {
        .section-text {
          top: $md-logo-size + $md-logo-margin;
        }
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #fivepermille-section-0 {
      .text-title {
        line-height: 110%;
      }
      .text-subtitle {
        font-size: $font-size-20;
      }
      .section-text {
        top: unset;
      }
      @media (min-aspect-ratio: 1/1) {
        .section-image {
          max-width: 50%;
          left: 50%;
        }
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #fivepermille-section-0 {
      .text-title {
        line-height: 120% !important;
        padding-left: 0;
        padding-right: 0;
      }
      .text-content {
        font-size: $font-size-25;
      }
      @media (max-aspect-ratio: 1/1) {
        .section-image {
          max-height: 50vh;
        }
      }
    }
  }
</style>
