<template>
  <div class="white-card pa-5">
    <div>
      <span :class="'number-title ' + intro_opt_class">{{ intro }}</span>
      <span :class="'numbered-title d-block ' + title_opt_class" v-html="title"/>
    </div>
    <div class="relative-div">
      <div :class="'content-container ' + content_opt_class">
        <span class="text-subtitle" v-html="subtitle"/>
        <span class="text-content" v-html="content"/>
      </div>
    </div>
    <v-btn :class="'donate-button error-button error ' + button_opt_class"
           v-if="button" tile :target="button.target" nuxt
           :to="button.href ? '' : localePath(checkRoute(button.to))" :href="button.href">
      {{ button.text_0 }}
    </v-btn>
  </div>
</template>

<script>
  import { checkRoute} from "../utils/route.utils";
  export default {
    name: "WhiteCard",
    props: {
      intro: String,
      title: String,
      subtitle: String,
      content: String,
      button: Object,
      intro_opt_class: String,
      title_opt_class: String,
      content_opt_class: String,
      button_opt_class: String
    },
    data: () => ({
      checkRoute: checkRoute
    })
  }
</script>

<style lang="scss">
  .white-card {
    position: relative;
    border: 2px solid black !important;
    height: 100%;
    background-color: white;
    .number-title {
      position: relative;
      line-height: 100%;
      color: $secondary-color;
    }
    .numbered-title {
      margin-top: -25px;
      line-height: 100%;
      z-index: 1;
      position: relative;
    }
    .right-button {
      right: 5% !important;
    }
    .relative-div {
      position: relative;
      margin-top: 2vh;
      margin-bottom: 2vh;
    }
    .donate-subtitle {
      font-family: "Crossten Thin";
      font-size: 20px;
      line-height: 120%;
      margin-bottom: 20px;
    }
    .donate-content {
      font-family: "Crossten Book";
      font-size: 20px;
      line-height: 120%;
      margin-bottom: 20px;
    }
    .donate-button {
      position: absolute;
      /*width: 100%;*/
      width: calc(60% - 40px);
      margin-left: 20%;
      bottom: -25px;
      font-size: 20px;
      height: 50px !important;
      box-shadow: $box-shadow-side $box-shadow-bottom $primary-color !important;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    .white-card {
      .number-title {
        font-size: $font-size-60;
      }
      .donate-button {
        width: calc(80% - 40px);
        margin-left: 10%;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    .white-card {
      .number-title {
        font-size: $font-size-30;
      }
      .numbered-title {
        margin-top: -10px;
        font-size: $font-size-18;
      }
      .donate-button {
        width: calc(80% - 40px);
        margin-left: 10%;
        bottom: -20px;
        height: 40px !important;
        font-size: $font-size-18;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    .white-card {
      .number-title {
        font-size: $font-size-50;
      }
      .numbered-title {
        margin-top: -15px;
        font-size: $font-size-20;
      }
    }
  }
</style>
