<template>
  <div class="donate-card">
    <div>
      <span :class="'number-title ' + intro_opt_class">{{ intro }}</span>
      <h1 :class="'numbered-title d-block ' + title_opt_class" v-html="title"/>
    </div>
    <div :class="'content-container ' + content_opt_class">
      <h2 class="text-subtitle d-block" v-html="subtitle"/>
      <h3 class="text-content" v-html="content"/>
    </div>
    <v-btn :class="'card-button error-button error ' + button_opt_class"
           v-if="button && !paypal" tile :target="button.target" nuxt
           :to="button.href ? '' : localePath(checkRoute(button.to))" :href="button.href">
      {{ button.text_0 }}
    </v-btn>
    <form v-if="button && paypal"
          action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_blank">
      <input type="hidden" name="cmd" value="_s-xclick" />
      <input type="hidden" name="hosted_button_id" :value="button.href" />
      <v-btn :class="'card-button error-button error ' + button_opt_class" tile type="submit">
        {{ button.text_0 }}
      </v-btn>
    </form>
  </div>
</template>

<script>
  import { checkRoute} from "../utils/route.utils";
  export default {
    name: "DonateCard",
    props: {
      intro: String,
      title: String,
      subtitle: String,
      content: String,
      button: Object,
      intro_opt_class: String,
      title_opt_class: String,
      content_opt_class: String,
      button_opt_class: String,
      paypal: Boolean
    },
    data: () => ({
      checkRoute: checkRoute
    })
  }
</script>

<style lang="scss">
  .donate-card {
    padding: 25px;
    border: 2px solid black !important;
    background-color: white;
    height: 100%;
    position: relative;
    .content-container {
      margin-top: -30px;
      margin-bottom: 3vh;
    }
    .number-title {
      position: relative;
      color: $secondary-color;
      line-height: 100%;
    }
    .numbered-title {
      position: relative;
      top: -42px;
      left: 8px;
    }
    .right-button {
      right: 5% !important;
    }
    .text-subtitle {
      font-size: $font-size-20;
      margin-bottom: 1vh;
      line-height: 110%;
    }
    .text-content {
      line-height: 110%;
    }
    .card-button {
      margin-bottom: -25px;
      bottom: 0;
      position: absolute;
      width: calc(80% - 50px);
      margin-left: 10%;
      height: 50px !important;
      font-size: 20px;
      box-shadow: $box-shadow-side $box-shadow-bottom $primary-color !important;
    }
    .iban-container {
      font-size: $font-size-30;
    }
    .iban-label {
      padding-top: 2vh;
      margin-bottom: 2vh;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    .donate-card {
      .iban-container {
        font-size: $font-size-25;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    .donate-card {
      padding: 10px;
      .text-subtitle {
        font-size: $font-size-15;
      }
      .iban-container {
        font-size: $font-size-20;
      }
      .numbered-title {
        top: -28px;
        left: 6px;
      }
      .content-container {
        margin-top: -25px;
      }
      .card-button {
        width: calc(80% - 30px);
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    .donate-card {
      .iban-container {
        font-size: $font-size-15;
      }
      .card-button {
        margin-bottom: -20px;
        height: 40px !important;
        font-size: $font-size-18;
      }
    }
    @media (max-width: 350px) {
      .donate-card {
        .iban-container {
          font-size: $font-size-12;
        }
      }
    }
  }
</style>
