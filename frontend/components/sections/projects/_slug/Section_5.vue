<template>
  <section id="projects-details-section-5" class="padding-level-3">
    <div class="quote-text text-center primary--text">
      <span v-html="sectionText"></span>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_5",
    props: {
      data: Object
    },
    /*head() {
      return {
        meta: this.data.meta_tags
      }
    },*/
    computed: {
      sectionText() {
        return this.data.texts[0].content
      }
    }
  }
</script>

<style lang="scss">
  #projects-details-section-5 {
    margin-top: 15vh;
    margin-bottom: 5vh;
  }
</style>
