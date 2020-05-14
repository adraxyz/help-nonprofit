<template>
  <section id="donations-section-1" v-resize="onResize">
    <v-row no-gutters class="donation-row accent padding-level-3" align="center">
      <v-col v-for="t in data.texts" :key="t.order" cols="12" md="4"
             class="donation-col">
        <DonationCard
          :intro="t.subtitle"
          :title="t.title"
          :content="t.content"
          :image="getSectionImage(t.order, data.order)"/>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  import DonationCard from "../../DonationCard";
  import { mapGetters } from 'vuex';
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
      DonationCard
    },
    computed: {
      ...mapGetters(['getSectionImage']),
    },
    methods: {
      onResize() {
        document.documentElement.style.setProperty('--100vh', `${window.innerHeight}px`);
      }
    }
  }
</script>

<style lang="scss">
  #donations-section-1 {
    min-height: calc(var(--100vh)/10*7);
    .donation-row {
      margin-top: 7vh;
      padding-top: 5vh;
      padding-bottom: 5vh;
    }
    .donation-col {
      padding-left: 1.5vw;
      padding-right: 1.5vw;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    /*#donations-section-1 {*/
    /*  margin-top: 1vh;*/
    /*}*/
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #donations-section-1 {
      /*.donation-row {*/
      /*  padding-top: 0px;*/
      /*}*/
      /*.donation-col {*/
      /*  margin-bottom: 2vh;*/
      /*}*/
    }
  }
</style>
