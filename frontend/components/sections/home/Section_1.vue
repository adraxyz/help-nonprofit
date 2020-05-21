<template>
  <section id="home-section-1" class="padding-level-2">

    <div class="section-title-right text-right">
      <h1 class="section-title">{{ data.title }}</h1>
    </div>

    <v-row class="section-row" no-gutters v-for="t in data.texts" :key="t.order">
      <v-col class="section-image-col" :order="t.order + 1" :order-md="t.order - 1">
        <v-img :src="findImage(t.order)" contain class="section-image"></v-img>
      </v-col>
      <v-col :order="t.order - 1" :order-md="t.order + 1" align-self="end" class="square-col">
        <Square class="section-square"
          :black_title="t.title"
          :first_light_title="t.subtitle"
          :second_light_title="t.content"
          :number="t.order + 1"
          backg_color="white"
          number_color="secondary"
          border="2px black solid !important"/>
      </v-col>
    </v-row>

  </section>
</template>

<script>
  import Square from "../../Square";
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
    components: {
      Square
    },
    methods: {
      findImage(index) {
        let image = this.data.images.find(i => i.order === index)
        return image.content
      }
    }
  }
</script>

<style lang="scss">
  #home-section-1 {
    .section-row {
      margin-bottom: 5vh;
    }
    .section-image-col {
      max-width: calc(100% - #{$square-size} + #{$square-overlap});
      margin-right: -$square-overlap;
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #home-section-1 {
      .section-image-col {
        max-width: 100%;
        margin-left: 0px !important;
        margin-right: 0px !important;
      }
      .square-col {
        margin-bottom: 5vh;
      }
    }
  }
</style>
