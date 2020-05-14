<template>
  <section id="get-involved-section-2" class="padding-level-3">
    <div class="quote-text text-center primary--text">
      <span v-html="sectionText"></span>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_2",
    props: {
      data: Object
    },
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      sectionText() {
        return this.data.texts[0].content
      }
    }
  }
</script>

<style lang="scss">
  #get-involved-section-2 {
    margin-top: 15vh;
    margin-bottom: 5vh;
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #get-involved-section-2 {
      margin-top: 15vh;
      margin-bottom: 5vh;
      .quote-text {
        padding-left: 0px;
        padding-right: 0px;
      }
    }
  }
</style>
