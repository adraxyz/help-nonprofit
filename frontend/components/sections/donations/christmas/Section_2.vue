<template>
  <section id="christmas-section-2" class="padding-level-3">
    <div class="quote-text text-center error--text">
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
  #christmas-section-2 {
    margin-top: 7vh;
    margin-bottom: 10vh;
    .quote-text {
      font-size: $font-size-60;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #christmas-section-2 {
      .quote-text {
        font-size: $font-size-40;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #christmas-section-2 {
      .quote-text {
        padding-left: 0px;
        padding-right: 0px;
        font-size: $font-size-30;
      }
    }
  }
</style>
