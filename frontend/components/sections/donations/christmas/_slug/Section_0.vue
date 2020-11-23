<template>

  <section id="product-details-section-0" class="padding-level-3"
           v-resize="onResize">

    <v-row no-gutters class="section-row" align="center">
      <v-col :cols="show_middle_image ? 12 : 6" md="6" class="text-center texts-col pa-2">
        <h1 class="text-title d-block" v-html="product.title"/>
        <v-img v-show="show_middle_image && !product.video" class="section-image-middle"
               :src="product.image_0 ? product.image_0 : ''" contain/>
        <img v-show="show_middle_image && product.video" class="section-gif-middle"
           :src="product.video ? product.video : ''" width="100%"/>
        <h2 class="text-subtitle d-block" v-html="product.subtitle"/>
        <h3 class="text-content d-block" v-html="product.description"/>

        <v-row v-show="product.category.internal" no-gutters class="mt-4">
          <v-col cols="6" class="help-font actions-info-col text-right pr-3" align-self="center">
            <span class="available-quantity">{{available_quantity}}</span>
            <span class="available-info">{{ getLabel('product_availability') }}</span>
          </v-col>
          <v-col cols="6" class="actions-info-col text-left pl-3">
            <v-btn class="button-shadow-error-left circle-button mr-2"
               fab text width="37" height="37" @click="removeFromShoppingCart(product)">
              <v-icon>{{minus_icon}}</v-icon>
            </v-btn>
            <v-btn class="button-shadow-primary-left circle-button"
               fab text width="37" height="37" @click="addToShoppingCart(product)">
              <v-icon>{{plus_icon}}</v-icon>
            </v-btn>
          </v-col>
        </v-row>

        <div v-show="!product.category.internal" class="mt-5">
          <span class="text-content info-text">
            {{ getLabel('available') }}
          </span>
          <h1 class="text-content title-text">
            {{product.category.title}}
          </h1>
        </div>
        <div v-show="!product.category.internal" class="help-font">
          <span class="mr-2 available-info">{{ getLabel('go_to_store') }}</span>
          <v-btn class="button-shadow-secondary-left circle-button"
                 target="_blank" fab text width="37" height="37" :href="product.shop_link" >
            <v-icon>{{arrow_right_icon}}</v-icon>
          </v-btn>
        </div>

      </v-col>
      <v-col v-show="!show_middle_image" cols="6" md="6" class="text-center image-col pa-2">
        <v-img class="section-image" v-show="!product.video"
               :src="product.image_0 ? product.image_0 : ''" contain/>
        <img class="section-image px-2" v-show="product.video"
           :src="product.video ? product.video : ''" width="100%"/>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="6">
        <v-img class="section-image" :src="product.image_1 ? product.image_1 : ''" contain/>
      </v-col>
      <v-col cols="12" md="6">
        <v-img class="section-image" :src="product.image_2 ? product.image_2 : ''" contain/>
      </v-col>
      <v-col cols="12" md="6">
        <v-img class="section-image" :src="product.image_3 ? product.image_3 : ''" contain/>
      </v-col>
      <v-col cols="12" md="6">
        <v-img class="section-image" :src="product.image_4 ? product.image_4 : ''" contain/>
      </v-col>
    </v-row>

  </section>

</template>

<script>
  import { mdiPlus, mdiMinus, mdiArrowRight } from "@mdi/js";
  import {mapState} from "vuex";
  export default {
    name: "Section_0",
    props: {
      data: Object,
      product: Object
    },
    data: () => ({
      section_height: 0,
      show_middle_image: false,
      plus_icon: mdiPlus,
      minus_icon: mdiMinus,
      arrow_right_icon: mdiArrowRight
    }),
    head() {
      return {
        meta: this.data ? this.data.meta_tags : ''
      }
    },
    async fetch() {
      await this.$store.dispatch('loadShopItemLabels')
    },
    computed: {
      ...mapState(['shop_item_labels', 'shopping_cart']),
      available_quantity() {
        let products_in_the_cart = 0
        this.shopping_cart.forEach(pc => pc.products.forEach(
          p => (p.order === this.product.order) && (products_in_the_cart +=1)))
        return this.product.count - products_in_the_cart
      }
    },
    methods: {
      onResize () {
        this.section_height = window.innerHeight
        document.documentElement.style.setProperty('--100vh', `${this.section_height}px`);
        let real_aspect_ratio = window.innerWidth/window.innerHeight
        if (this.$vuetify.breakpoint.smAndDown && real_aspect_ratio < 1) {
          this.show_middle_image = true
        } else {
          this.show_middle_image = false
        }
      },
      addToShoppingCart(product) {
        if (this.product.availability > 0) {
          this.$store.dispatch('addProductToShoppingCart', {
            product: product
          })
        }
      },
      removeFromShoppingCart(product) {
        this.$store.dispatch('removeProductToShoppingCart', {
          product: product
        })
      },
      getLabel(item) {
        if (this.shop_item_labels instanceof Array) {
          let label = this.shop_item_labels.find(l => l.item === item)
          if (label) {
            return label.label
          }
        }
        return ''
      }
    }
  }
</script>

<style lang="scss">
  #product-details-section-0 {
    height: 100%;
    margin-bottom: 10vh;
    .section-row {
      padding-top: $logo-size;
      min-height: var(--100vh);
    }
    .text-title {
      line-height: 110%;
      margin-bottom: 2vh;
      font-size: $font-size-30;
    }
    .text-subtitle {
      margin-top: 2vh;
      margin-bottom: 1vh;
    }
    .section-image {
      max-height: calc(var(--100vh) - #{$logo-size} - #{$logo-margin});
    }
    .circle-button {
      border: 2px solid black !important;
    }
    .help-font {
      font-family: "Crossten Light";
      letter-spacing: 0.15rem !important;
    }
    .available-quantity {
      font-family: "Crossten Book";
    }
    .available-info {
      font-size: $font-size-12;
    }
    .title-text {
      font-family: "Crossten Bold";
      color: $secondary-color !important;
    }
    .info-text {
      font-family: "Crossten Thin" !important;
    }
    .section-gif-middle {
      padding-left: 7vw;
      padding-right: 7vw;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #product-details-section-0 {
      .section-row {
        padding-top: $md-logo-size;
      }
      .section-image {
        max-height: calc(var(--100vh) - #{$md-logo-size} - #{$md-logo-margin});
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #product-details-section-0 {
      .texts-col {
        margin-bottom: 3vh;
      }
      .text-title {
        margin-bottom: 1.5vh;
        font-size: $font-size-20;
      }
      .text-subtitle {
        margin-top: 3vh;
        font-size: $font-size-18;
        line-height: 110% !important;
        //font-family: "Crossten Light" !important;
      }
      .section-image-middle {
        margin-top: 3vh !important;
        max-height: 28vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #product-details-section-0 {
      .texts-col {
        margin-bottom: 2vh;
      }
      .text-title {
        margin-bottom: 1vh;
        font-size: $font-size-18;
      }
      .text-subtitle {
        margin-top: 3vh;
        font-size: $font-size-15;
      }
    }
  }
</style>
