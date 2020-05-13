<template>
  <section id="project-section-1" class="padding-level-3">

    <div class="section-title-left">
      <span class="section-title">{{ data.title }}</span>
    </div>

    <v-row no-gutters v-for="c in categories" :key="c.order"
           class="section-row pb-5 pb-md-10" align-content="center">
      <v-col cols="12" md="6" :order="c.order" :order-md="mdTextOrder(c.order)"
             class="section-text section-col" align-self="center">
        <div class="text-title" v-html="c.title"/>
        <div class="text-subtitle" v-html="c.subtitle"/>
        <v-img v-if="$vuetify.breakpoint.smAndDown"
               class="section-image" :src="c.image" contain></v-img>
        <div class="text-content pt-2" v-html="c.description"/>
      </v-col>
      <v-col v-if="!$vuetify.breakpoint.smAndDown"
             cols="12" md="6" :order="c.order+1" :order-md="mdImageOrder(c.order)"
             align-self="center" class="section-col">
        <v-img class="section-image" :src="c.image" contain></v-img>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  export default {
    name: "Section_2",
    props: {
      data: Object,
      categories: Array
    },
    methods: {
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
  #project-section-1 {
    margin-bottom: 5vh;
    .section-col {
      padding-left: 1vw;
      padding-right: 1vw;
    }
    .text-subtitle {
      line-height: 120%;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #project-section-1 {
      .section-image {
        max-height: calc(100vh - #{$md-down-top-bar-height} - #{$md-down-logo-margin});
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #project-section-1 {
      .section-row {
        margin-bottom: 3vh;
      }
      .section-text {
        text-align: center;
      }
      .section-image {
        margin-top: 2vh;
        max-height: 50vh;
      }
      .text-title {
        line-height: 150% !important;
      }
      .text-subtitle {
        line-height: 150% !important;
      }
    }
  }
</style>
