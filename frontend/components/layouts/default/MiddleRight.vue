<template>
  <div id="middle-right">
    <SocialIcons :vertical="true" :shadow="true"/>
  </div>
</template>

<script>
  import SocialIcons from "./SocialIcons";
  export default {
    name: "MiddleRight",
    components: {
      SocialIcons
    }
  }
</script>

<style lang="scss" scoped>
  #middle-right {
    position: fixed;
    z-index: 2;
    /*right: $min-margin-x;*/
    top: 40%;
  }
  /* Media queries */
  @media only screen and (max-width: $max-width) {
    #middle-right {
      right: 0;
    }
  }
  @media only screen and (min-width: $max-width) {
    #middle-right {
      right: calc((100vw - #{$max-width})/2);
    }
  }
</style>
