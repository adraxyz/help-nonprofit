<template>
  <section id="home-section-4" class="padding-level-3">
    <div class="quote-text text-center primary--text">
      <span v-html="sectionText"></span>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_4",
    props: {
      data: Object
    },
    computed: {
      sectionText() {
        return this.data.texts[0].content
      }
    }
  }
</script>

<style lang="scss">
  #home-section-4 {
    margin-top: 15vh;
    margin-bottom: 5vh;
  }
</style>
