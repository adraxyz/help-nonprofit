<template>
  <section id="donations-section-4" class="padding-level-3">
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
        let text = this.data.texts.find(t => t.order === 0)
        if (text) {
          return text.content
        }
        return ''
      }
    }
  }
</script>

<style lang="scss">
  #donations-section-4 {
    margin-top: 15vh;
    margin-bottom: 5vh;
  }
</style>
