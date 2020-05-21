<template>
  <section id="fivepermille-section-2" class="padding-level-3">
    <v-row no-gutters v-for="t in data.texts" :key="t.order"
           class="section-row pb-5 pb-md-10">
      <v-col cols="12" md="6" :order="t.order" :order-md="mdTextOrder(t.order)"
             class="section-text">
        <h1 class="text-title" v-html="t.title"/>
        <v-img v-if="$vuetify.breakpoint.smAndDown"
               class="section-image" :src="image(t.order).content" contain></v-img>
        <h2 class="text-subtitle" v-html="t.subtitle"/>
        <div class="text-content pt-2" v-html="t.content"/>
      </v-col>
      <v-col v-if="!$vuetify.breakpoint.smAndDown"
             cols="12" md="6" :order="t.order+1" :order-md="mdImageOrder(t.order)">
        <v-img class="section-image" :src="image(t.order).content" contain></v-img>
      </v-col>
    </v-row>
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
    methods: {
      image(index) {
        return this.data.images.find(i => i.order === index)
      },
      mdTextOrder(i) {
        if (i%2 === 0) {
          return i
        }
        return i + 1
      },
      mdImageOrder(i) {
        if (i%2 === 0) {
          return i + 1
        }
        return i
      }
    }
  }
</script>

<style lang="scss">
  #fivepermille-section-2 {
    margin-top: 15vh;
    .section-text {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #fivepermille-section-2 {
      .section-image {
        max-height: calc(100vh - #{$md-down-top-bar-height} - #{$md-down-logo-margin});
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #fivepermille-section-2 {
      .section-text {
        text-align: center;
        margin-bottom: 7vh;
      }
      .text-title {
        margin-bottom: 2vh;
      }
      .section-image {
        margin-bottom: 5vh;
        max-height: 50vh;
      }
    }
  }
</style>
