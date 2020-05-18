<template>
  <section id="donations-section-3" class="padding-level-3">

    <div class="section-title-center text-center">
      <span class="section-title">{{ data.title }}</span>
    </div>

    <v-row no-gutters v-for="t in data.texts" :key="t.order"
           class="section-row" align="center">
      <v-col cols="12" :md="image(t.order) ? 6 : 12" :order="t.order" :order-md="mdTextOrder(t.order)"
             class="section-text">
        <div class="text-title" v-html="t.title"/>
        <v-img v-show="$vuetify.breakpoint.smAndDown && image(t.order)"
               class="section-image" :src="image(t.order)" contain></v-img>
        <div class="text-subtitle pt-2" v-html="t.subtitle"/>
        <div class="text-content pt-2" v-html="t.content"/>
      </v-col>
      <v-col v-show="$vuetify.breakpoint.mdAndUp && image(t.order)"
             cols="12" md="6" :order="t.order+1" :order-md="mdImageOrder(t.order)">
        <v-img class="section-image" :src="image(t.order)" contain></v-img>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  export default {
    name: "Section_3",
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
  #donations-section-3 {
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
    #donations-section-3 {
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
