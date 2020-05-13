<template>
  <div class="donation-card">
    <v-img class="donation-image" :src="image.content" :key="image.order" transition="fade" contain/>
<!--    <v-img v-if="$vuetify.breakpoint.smAndDown"-->
<!--           class="donation-image" :src="image.content" :key="image.order"-->
<!--           transition="fade" contain></v-img>-->
    <div class="donation-texts button-shadow-secondary-right">
      <span class="text-subtitle" v-html="intro"/>
      <span class="title-number" v-html="title"/>
      <span class="text-content d-block" v-html="content"/>
    </div>
<!--    <v-img v-if="!$vuetify.breakpoint.smAndDown"-->
<!--           class="donation-image" :src="image.content" :key="image.order"-->
<!--           transition="fade" contain></v-img>-->
  </div>
</template>

<script>
  export default {
    name: "DonationCard",
    props: {
      intro: String,
      title: String,
      content: String,
      image: Object
      // TODO: button
    }
  }
</script>

<style lang="scss" scoped>
  .donation-card {
    .donation-texts {
      /*border: 2px solid black;*/
      text-align: center;
      background-color: white;
      /*margin-top: -5px;*/
      padding: 20px;
      z-index: 0;
      min-height: 150px;
      color: $accent-color;
    }
    .donation-image {
      z-index: 1;
    }
    .text-subtitle {
      line-height: 100%;
      font-size: $font-size-20;
      font-family: "Crossten Light";
    }
    .title-number {
      position: relative;
      line-height: 100%;
      color: $secondary-color;
    }
    .text-content {
      line-height: 120%;
      font-family: "Crossten Bold";
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    .donation-card {
      .number-title {
        font-size: $font-size-50;
      }
      .text-content {
        line-height: 110%;
      }
      .donation-image {
        max-height: 50vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    .donation-card {
      padding-bottom: 5vh;
      .donation-texts {
        position: relative;
        /*max-width: 100%;*/
        text-align: center;
        min-height: unset;
        margin-left: 15%;
        margin-right: 15%;
      }
      .donation-image {
        margin-top: 0px;
        margin-bottom: 1vh;
      }
      .text-subtitle {
        margin-bottom: 1vh;
      }
      .text-content {
        line-height: 110%;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    .donation-card {
      .donation-texts {
        margin-left: 0;
        margin-right: 0;
      }
    }
  }
</style>
