<template>
  <section id="get-involved-section-0" class="padding-level-3"
           v-resize="onResize">
    <v-row no-gutters class="section-row" align="center">
      <v-col :cols="show_middle_image ? 12 : 6" md="6" class="text-center texts-col">
        <h1 class="text-title d-block" v-for="t in texts" :key="t.order">
          {{t.text}}
        </h1>
        <v-img v-if="show_middle_image" class="section-image-middle" :src="image.content" contain/>
        <h2 class="text-subtitle d-block">
          {{subtitle}}
        </h2>
      </v-col>
      <v-col v-if="!show_middle_image" cols="6" md="6" class="text-center image-col">
        <v-img class="section-image" :src="image.content" contain/>
      </v-col>
    </v-row>
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
      subtitle: '',
      show_middle_image: false
    }),
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      texts() {
        let result = []
        let string = this.data.texts.find(t => t.order === 0)
        if (string) {
          this.subtitle = string.subtitle
          let items = string.content.split("|")
          items.forEach(i => result.push({oreder: i.split('-')[0], text: i.split('-')[1]}))
        }
        return result
      },
      image() {
        return this.data.images.find(i => i.order === 0)
      }
    },
    methods: {
      onResize () {
        this.section_height = window.innerHeight
        document.documentElement.style.setProperty('--100vh', `${this.section_height}px`);
        let real_aspect_ratio = window.innerWidth/window.innerHeight
        if (this.$vuetify.breakpoint.smAndDown && real_aspect_ratio < 1) {
          this.show_middle_image = true
        } else {
          this.show_middle_image = false
        }
      }
    }
  }
</script>

<style lang="scss">
  #get-involved-section-0 {
    height: 100%;
    .section-row {
      padding-top: $logo-size;
      min-height: var(--100vh);
    }
    .text-title {
      line-height: 110%;
      margin-bottom: 2vh;
      font-size: $font-size-30;
    }
    .text-subtitle {
      margin-top: 5vh;
    }
    .section-image {
      max-height: calc(var(--100vh) - #{$logo-size} - #{$logo-margin});
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #get-involved-section-0 {
      .section-row {
        padding-top: $md-logo-size;
      }
      .section-image {
        max-height: calc(var(--100vh) - #{$md-logo-size} - #{$md-logo-margin});
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #get-involved-section-0 {
      .texts-col {
        margin-bottom: 3vh;
      }
      .text-title {
        margin-bottom: 1.5vh;
        font-size: $font-size-18;
      }
      .text-subtitle {
        margin-top: 3vh;
        font-size: $font-size-15;
      }
      .section-image-middle {
        margin-top: 3vh !important;
        max-height: 40vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #get-involved-section-0 {
      .texts-col {
        margin-bottom: 2vh;
      }
      .text-title {
        margin-bottom: 1vh;
        font-size: $font-size-15;
      }
      .text-subtitle {
        margin-top: 3vh;
        font-size: $font-size-12;
      }
    }
  }
</style>
