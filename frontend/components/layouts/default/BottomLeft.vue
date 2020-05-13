<template>
  <div id="bottom-left">
    <LanguagesSwitcher :drawer="false"/>
  </div>
</template>

<script>
  import LanguagesSwitcher from "./LanguagesSwitcher";
  export default {
    name: "BottomLeft",
    components: {
        LanguagesSwitcher
    }
  }
</script>

<style lang="scss" scoped>
  #bottom-left {
    position: fixed;
    left: $logo-margin * 0.8;
    bottom: $min-margin-y;
    z-index: 2;
  }
  @media only screen and (min-width: $max-width) {
    #bottom-left {
      left: calc((100vw - #{$max-width})/2 + #{$logo-margin});
    }
  }
  @media only screen and (max-width: $max-width) {
    /*#bottom-left {
      left: $logo-margin;
    }*/
  }
</style>
