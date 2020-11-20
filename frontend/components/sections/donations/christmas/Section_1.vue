<template>
  <section id="christmas-section-1" v-resize="onResize">

    <v-row no-gutters class="donation-row padding-level-3" align="center">
      <v-col cols="12" sm="4" class="donation-col" :order="p.order"
             v-for="p in products" :key="p.order">
        <ShopItemCard :product="p" :texts="texts"/>
      </v-col>
    </v-row>

  </section>
</template>

<script>
  import ShopItemCard from "@/components/ShopItemCard";
  import {mapState} from "vuex";
  export default {
    name: "Section_0",
    props: {
      data: Object
    },
    head() {
      return {
        meta: this.data ? this.data.meta_tags : ''
      }
    },
    async fetch() {
      await this.$store.dispatch('loadProducts')
    },
    components: {
      ShopItemCard
    },
    computed: {
      ...mapState(['products']),
      texts() {
        return this.data.texts.find(t => t.order === 0)
      }
    },
    methods: {
      onResize() {
        document.documentElement.style.setProperty('--100vh', `${window.innerHeight}px`);
      }
    }
  }
</script>

<style lang="scss">
  #christmas-section-1 {
    min-height: calc(var(--100vh)/10*7);
    .donation-row {
      padding-top: 5vh;
      padding-bottom: 5vh;
    }
    .donation-col {
      padding-left: 2vw;
      padding-right: 2vw;
      padding-bottom: 5vh;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    /*#christmas-section-1 {*/
    /*  margin-top: 1vh;*/
    /*}*/
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #christmas-section-1 {
      .donation-row {
        padding-left: 10vw;
        padding-right: 10vw;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #christmas-section-1 {
      .donation-col {
        padding-top: 7vh;
        padding-bottom: 7vh;
        padding-left: 10vw;
        padding-right: 10vw;
      }
    }
  }
</style>
