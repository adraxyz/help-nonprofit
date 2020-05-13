<template>
  <div class="small-white-card">
    <div>
      <span class="number-title">{{ number }}</span>
      <span class="numbered-title d-block" v-html="title"/>
    </div>
    <div class="relative-div">
      <div class="content-container">
        <span class="numbered-subtitle d-block" v-html="subtitle"/>
        <span class="text-content mt-2 d-block" v-html="content"/>
      </div>
    </div>
    <v-btn v-if="button"
           class="card-button error-button error" tile :target="button.target"
           :href="button.href" :to="localePath(checkRoute(button.to))">
      {{ button.text_0 }}
    </v-btn>
  </div>
</template>

<script>
  import { checkRoute} from "../utils/route.utils";
  export default {
    name: "SmallWhiteCard",
    props: {
      number: Number,
      title: String,
      subtitle: String,
      content: String,
      button: Object
    },
    data: () => ({
      checkRoute: checkRoute
    })
  }
</script>

<style lang="scss">
  .small-white-card {
    position: relative;
    height: 100%;
    background-color: white;
    .number-title {
      color: $secondary-color;
    }
    .numbered-title {
      position: relative;
      top: 57px;
      left: 8px;
    }
    .numbered-subtitle {
      line-height: 150%;
    }
    .relative-div {
      position: relative;
    }
    .card-button {
      position: absolute;
      bottom: -$nav-button-height/2;
      padding: 8px !important;
      font-size: 20px;
      box-shadow: $box-shadow-side $box-shadow-bottom $primary-color !important;
    }
    .content-container {
      margin-top: 60px;
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    .small-white-card {
      .content-container {
        margin-top: 30px;
      }
      .number-title {
        line-height: 100%;
      }
      .numbered-title {
        top: 22px;
        left: 5px;
      }
      .numbered-subtitle {
        line-height: 100%;
      }
    }
  }
</style>
