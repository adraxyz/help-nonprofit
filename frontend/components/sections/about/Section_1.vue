<template>
  <section id="about-section-1" class="padding-level-5">

    <div class="section-title-center text-center">
      <span class="section-title">{{ data.title }}</span>
    </div>

    <div class="text-content text-center">
      <p v-for="t in data.texts" :key="t.order" v-html="t.content"/>
    </div>


  </section>
</template>

<script>
  export default {
    name: "Section_1",
    props: {
      data: Object
    },
    head() {
      return {
        meta: this.data.meta_tags
      }
    }
  }
</script>

<style lang="scss">
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #about-section-1 {
      padding-left: $circle-icon-size;
      padding-right: $circle-icon-size;
    }
  }
</style>
