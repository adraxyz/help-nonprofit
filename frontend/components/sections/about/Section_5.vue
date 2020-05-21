<template>
  <section id="about-section-5" class="padding-level-3">
    <div class="section-title-center text-center">
      <h1 class="section-title">{{data.title}}</h1>
    </div>
    <v-row no-gutters>
      <v-col class="section-col py-5 pa-sm-10"
        cols="12" :sm="12/data.documents.length" v-for="d in data.documents" :key="d.order">
        <WhiteCard :intro="d.title" :title="d.subtitle"
                   :content="d.description" :button="button(d)"/>
<!--                   :button_opt_class="'right-button'"/>-->
      </v-col>
    </v-row>
  </section>
</template>

<script>
  import WhiteCard from "../../WhiteCard";
  export default {
    name: "Section_5",
    props: {
      data: Object
    },
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    components: {
      WhiteCard
    },
    methods: {
      button(doc) {
        let button = this.data.buttons.find(b => b.order === doc.order)
        return button ? {
          target: button.target,
          href: doc.file,
          to: null,
          text_0: button.text_0
        } : null
      }
    }
  }
</script>

<style lang="scss">
  #about-section-5 {
    margin-bottom: 5vh;
  }
</style>
