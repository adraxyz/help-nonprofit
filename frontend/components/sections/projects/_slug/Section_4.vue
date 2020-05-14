<template>
  <section id="projects-details-section-4" class="padding-level-3">

    <div class="section-title-left">
      <span class="section-title">{{data.title}}</span>
    </div>

    <div class="text-content" v-html="design_description.content"/>
    <v-row no-gutters class="pt-5 section-row">
      <v-col cols="12" sm="8">
        <v-img :src="design_image.content" contain/>
      </v-col>
      <v-col cols="12" sm="4" class="section-text">
        <div v-for="t in design_texts" :key="t.order" class="text-container">
          <span class="text-title" :style="'color: ' + textColor(t.order) + ';'">
            {{t.title}}
          </span>
          <br>
          <span class="text-subtitle" :style="'color: ' + textColor(t.order) + ';'">
            {{t.subtitle}}
          </span>
          <br>
          <span class="text-content">{{t.content}}</span>
        </div>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  export default {
    name: "Section_4",
    props: {
      data: Object,
      project: Object
    },
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      design_texts() {
        return this.project.texts.filter(
          t => t.project_section === "design" && t.order != 0
        )
      },
      design_description() {
        return this.project.texts.find(
          t => t.project_section === "design" && t.order === 0
        )
      },
      design_image() {
        return this.project.images.find(
          i => i.project_section === "design" && i.order === 1
        )
      }
    },
    methods: {
      textColor(index) {
        switch (index) {
          case 1:
            return this.$vuetify.theme.themes.dark.primary
            break
          case 2:
            return this.$vuetify.theme.themes.dark.warning
            break
          case 3:
            return this.$vuetify.theme.themes.dark.secondary
            break
          case 4:
            return this.$vuetify.theme.themes.dark.error
            break;
        }
      }
    }
  }
</script>

<style lang="scss">
  #projects-details-section-4 {
    .section-text {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #projects-details-section-4 {
      .text-container {
        margin-top: 3vh;
      }
    }
  }
</style>
