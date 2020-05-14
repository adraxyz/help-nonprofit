<template>
  <section id="about-section-4" class="padding-level-3">
    <div class="section-title-center text-center">
      <span class="section-title">{{data.title}}</span>
    </div>
    <v-row no-gutters>
      <v-col cols="12" lg="6">
      <v-img class="section-image" :src="sectionImage" contain></v-img>
      </v-col>
      <v-col cols="12" lg="6" class="pl-lg-5">
        <div class="section-part first-part">
          <span class="d-block text-title">{{text(0).title}}</span>
          <span class="text-content d-block" v-html="text(0).content"/>
        </div>
        <div class="section-part second-part">
          <span class="d-block text-title">{{text(1).title}}</span>
          <span class="text-content d-block" v-html="text(1).content"/>
        </div>
        <div class="section-part third-part">
          <span class="d-block text-title">{{text(2).title}}</span>
          <span class="text-content d-block" v-html="text(2).content"/>
        </div>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  export default {
    name: "Section_4",
    props: {
      data: Object
    },
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
      text(index) {
        return this.data.texts.find(t => t.order === index)
      }
    }
  }
</script>

<style lang="scss">
  #about-section-4 {
    .section-image {
      max-height: calc(100vh - #{$logo-size});
    }
    .section-part {
      margin-bottom: 3vh;
    }
    .first-part {
      color: $secondary-color;
    }
    .second-part {
      color: $primary-color;
    }
    .third-part {
      color: $error-color;
    }
    .text-title {
      margin-bottom: 1vh;
      line-height: 110%;
      font-size: $font-size-30;
    }
    .text-content {
      color: black;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #about-section-4 {
      .section-image {
        margin-bottom: 7vh;
        max-height: calc(100vh - #{$md-logo-size});
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #about-section-4 {
      .text-title {
        font-size: $font-size-20;
      }
    }
  }
</style>
