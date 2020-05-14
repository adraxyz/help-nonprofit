<template>
  <section id="about-section-0" class="padding-level-2" v-resize="onResize">
    <div class="section-title-container">
      <span class="section-title">{{data.title}}</span>
    </div>
    <div>
      <v-img class="section-image" :src="sectionImage" contain/>
    </div>
    <div>
      <v-row no-gutters>
        <v-col class="text-center pa-3 team-col">
          <span class="text-title error--text d-block">{{teamMember(0).title}}</span>
          <span class="text-subtitle">{{teamMember(0).content}}</span>
        </v-col>
        <v-col class="text-center pa-3 team-col">
          <span class="text-title success--text d-block">{{teamMember(1).title}}</span>
          <span class="text-subtitle">{{teamMember(1).content}}</span>
        </v-col>
        <v-col class="text-center pa-3 team-col">
          <span class="text-title info--text d-block">{{teamMember(2).title}}</span>
          <span class="text-subtitle">{{teamMember(2).content}}</span>
        </v-col>
        <v-col class="text-center pa-3 team-col">
          <span class="text-title primary--text d-block">{{teamMember(3).title}}</span>
          <span class="text-subtitle">{{teamMember(3).content}}</span>
        </v-col>
        <v-col class="text-center pa-3 team-col">
          <span class="text-title secondary--text d-block">{{teamMember(4).title}}</span>
          <span class="text-subtitle">{{teamMember(4).content}}</span>
        </v-col>
      </v-row>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_0",
    props: {
      data: Object
    },
    data: () => ({
      section_height: 0
    }),
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      sectionImage() {
        return this.data.images[0].content
      }
    },
    methods: {
      teamMember(index) {
        return this.data.texts.find(m => m.order === index)
      },
      onResize () {
        this.section_height = window.innerHeight
        document.documentElement.style.setProperty('--100vh', `${this.section_height}px`);
      }
    }
  }
</script>

<style lang="scss">
  #about-section-0 {
    .section-image {
      max-height: calc(100vh - #{$logo-size} - 60px);
    }
    .section-title-container {
      margin-top: $logo-size;
      text-align: center;
    }
    .text-subtitle {
      line-height: 120%;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #about-section-0 {
      .section-image {
        max-height: calc(100vh - #{$md-logo-size} - 40px);
      }
      .section-title-container {
        margin-top: $md-logo-size;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    @media (min-aspect-ratio: 1/1) {
      #about-section-0 {
        .section-title-container {
          margin-top: $circle-icon-size;
        }
        .section-image {
          max-height: calc(100vh - #{$circle-icon-size} - 40px);
        }
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #about-section-0 {
      .team-col {
        line-height: 100%;
        padding-bottom: 1vh !important;
      }
    }
  }
</style>
