<template>
  <section id="get-involved-section-1" class="padding-level-3">
    <v-row no-gutters v-for="t in data.texts" :key="t.order"
           class="section-row">
      <v-col cols="12" md="6" :order="t.order" :order-md="mdTextOrder(t.order)"
             class="section-text">
        <h1 class="text-title d-block" v-html="t.title"/>
        <v-img v-if="$vuetify.breakpoint.smAndDown"
               class="section-image" :src="image(t.order)" contain></v-img>
        <h2 class="text-subtitle d-block pt-2" v-html="t.subtitle"/>
        <div class="text-content pt-2" v-html="t.content"/>
      </v-col>
      <v-col v-if="$vuetify.breakpoint.mdAndUp"
             cols="12" md="6" :order="t.order+1" :order-md="mdImageOrder(t.order)">
        <v-img class="section-image" :src="image(t.order)" contain></v-img>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  export default {
    name: "Section_1",
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
        let img = this.data.images.find(i => i.order === index)
        if (img) {
          return img.content
        }
        return ''
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
  #get-involved-section-1 {
    margin-top: 7vh;
    margin-bottom: 5vh;
    .section-text {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .text-subtitle {
      line-height: 120%;
    }
    .section-row {
      margin-bottom: 10vh;
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #get-involved-section-1 {
      .section-text {
        text-align: center;
      }
      .section-image {
        width: 60%;
        align-self: center;
      }
    }
  }
</style>
