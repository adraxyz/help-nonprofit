<template>
  <section id="home-section-2" class="padding-level-1">
    <div class="section-title-center text-center">
      <h1 class="section-title">{{data.title}}</h1>
    </div>
    <div class="image-conatiner">
      <v-img class="section-image" :src="sectionImage" contain></v-img>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_2",
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
    }
  }
</script>

<style lang="scss">
  #home-section-2 {
    .section-image {
      max-height: calc(100vh - #{$md-up-top-bar-height});
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #home-section-2 {
      .section-image {
        max-height: calc(100vh - #{$md-down-top-bar-height});
      }
    }
  }
</style>
