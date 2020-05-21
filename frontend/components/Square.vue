<template>
  <div :class="'square-div ' + backg_color" :style="'border: ' + border + ';'">
    <div class="square-content">
      <span :class="'number-title ' + number_color + '--text'">{{ number }}</span>
      <h2 class="numbered-title">{{ black_title }}</h2>
      <div class="numbered-subtitle">
        <h2>{{ first_light_title }}</h2>
<!--&lt;!&ndash;      <br v-if="$vuetify.breakpoint.mdAndUp">&ndash;&gt;-->
        <h2>{{ second_light_title }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Square",
    props: {
      black_title: String,
      first_light_title: String,
      second_light_title: String,
      backg_color: String,
      number: Number,
      number_color: String,
      border: String
    }
  }
</script>

<style lang="scss" scoped>
  .square-div {
    width: $square-size;
    height: $square-size;
  }
  .square-content {
    padding: 16%;
    height: 100%;
  }
  .numbered-title {
    position: relative;
    top: 57px;
    margin-left: 8px;
  }
  .numbered-subtitle {
    position: relative;
    top: 60px;
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    .square-div {
      width: unset;
      height: 100px;
    }
    .square-content {
      padding: 5px !important;
    }
    .numbered-title {
      top: 34px;
      margin-left: 5px;
    }
    .numbered-subtitle {
      top: 35px;
      display: block;
    }
    @media (min-width: 600px) {
      .square-div {
        margin-left: $md-down-top-bar-height;
        max-width: 50vw;
      }
    }
  }
</style>
