<template>
  <section id="about-section-2" class="padding-level-3">

    <div class="section-title-left">
      <span class="section-title">{{ data.title }}</span>
    </div>

    <v-row no-gutters class="section-row" v-for="t in section_texts" :key="t.order">
      <v-col cols="12" md="5" class="section-col">
        <v-row no-gutters class="pl-md-10">
          <SmallWhiteCard
            :number="t.order + 1"
            :title="t.title"
            :subtitle="t.subtitle"
            :content="t.content"/>
        </v-row>
      </v-col>
      <v-col cols="12" md="7" class="section-col">
        <v-img v-if="image(t.order)" class="section-image"
               :src="image(t.order).content" contain>
        </v-img>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  import SmallWhiteCard from "../../SmallWhiteCard";
  export default {
    name: "Section_2",
    props: {
      data: Object
    },
    data: () => ({
      section_texts: []
    }),
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    components: {
      SmallWhiteCard
    },
    methods: {
      image(index) {
        return this.data.images.find(i => i.order === index)
      }
    },
    created() {
      // Quick&Dirty TODO: manage sorting on server side
      this.section_texts.push(...this.data.texts)
      this.section_texts.sort((a, b) => a.order - b.order)
    }
  }
</script>

<style lang="scss">
  #about-section-2 {
    .section-title-container {
      margin-top: 7vh;
      margin-bottom: 5vh;
    }
    .section-row {
      margin-bottom: 5vh;
    }
    .section-image {
      padding-left: 10%;
      padding-right: 10%;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #about-section-2 {
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #about-section-2 {
      .section-image {
        margin-top: 2vh;
        padding-left: 30%;
        padding-right: 30%;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #about-section-2 {
      .section-title {
        margin-left: 0px;
      }
      .section-image {
        padding-left: 10%;
        padding-right: 10%;
      }
    }
  }
</style>
