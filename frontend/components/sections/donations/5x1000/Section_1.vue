<template>
  <section id="fivepermille-section-1" class="padding-level-3">

    <div class="section-title-center text-center">
      <h1 class="section-title">{{data.title}}</h1>
    </div>

    <v-row no-gutters class="section-row">
      <v-col v-for="t in data.texts" :key="t.order"
             cols="12" md="4" class="text-center section-col">
        <v-row no-gutters>
          <v-col cols="12" sm="6" md="12" order="1">
            <v-img :src="image(t.order)" contain class="col-image"/>
          </v-col>
          <v-col cols="12" sm="6" md="12" order="0" class="text-title">
            <h2 v-html="t.title"/>
          </v-col>
          <v-col cols="12" order="2" class="text-content">
            <div v-html="t.content"/>
          </v-col>
        </v-row>
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
      }
    }
  }
</script>

<style lang="scss">
  #fivepermille-section-1 {
    .section-title {
      margin-top: 10vh;
    }
    .section-col {
      padding: 2vh;
    }
    .col-image {
      height: 30vh;
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #fivepermille-section-1 {
      .text-title {
        display: flex;
        flex-direction: column;
        justify-content: center;
        font-size: $font-size-40;
      }
      .text-content {
        font-size: $font-size-25;
      }
      .col-image {
        padding-left: 20%;
        padding-right: 20%;
      }
      .section-col {
        margin-bottom: 7vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #fivepermille-section-1 {
      .text-title {
        margin-bottom: 3vh;
        font-size: $font-size-20;
      }
      .text-content {
        font-size: $font-size-18;
      }
    }
  }
</style>
