<template>
  <section id="projects-details-section-3" class="padding-level-3">

    <div class="section-title-left">
      <h1 class="section-title">{{data.title}}</h1>
    </div>

    <div class="text-content" v-html="state_of_art_text.content"/>
    <div class="section-gallery">
      <v-row no-gutters class="section-row">
        <span v-if="false">{{state_of_art_images}}</span>
        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
          <template v-slot:activator="{ on }">
            <v-col v-for="i in state_of_art_images" :key="i.order"
                   cols="12" :sm="smCols(i.content)" class="section-col">
              <v-img :src="i.alt_content ? i.alt_content : i.content" class="project-image" cover v-on="on"
                     @click="dialog_content=i.content"></v-img>
            </v-col>
          </template>
          <div class="dialog-content-container">
            <v-btn fab color="primary" class="ma-0 ma-md-4 close-btn"
                   right top fixed :small="$vuetify.breakpoint.smAndDown"
                   @click="dialog=false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-img :src="dialog_content" class="fullscreen-image" contain></v-img>
          </div>
        </v-dialog>
      </v-row>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_3",
    props: {
      data: Object,
      project: Object
    },
    data () {
      return {
        dialog: false,
        dialog_content: ''
      }
    },
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      state_of_art_text() {
        return this.project.texts.find(t => t.project_section === "state_of_art")
      },
      state_of_art_images() {
        let images = this.project.images.filter(i => i.project_section === "state_of_art")
        return images.sort((a, b) => b.order - a.order)
      }
    },
    methods: {
      smCols(img_name) {
        if (img_name.toLowerCase().includes("vertical")) {
          return 3
        }
        return 6
      }
    }
  }
</script>

<style lang="scss">
  #projects-details-section-3 {
    .section-gallery {
      margin-top: 3vh;
      margin-bottom: 3vh;
    }
    .project-image {
      max-height: 80vh;
      height: 100%;
    }
    .section-col {
      padding: 1vw;
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #projects-details-section-3 {
      .project-image {
        margin-top: 0px;
        margin-left: 0px;
        margin-right: 0px;
        margin-bottom: $md-down-logo-margin;
      }
    }
  }
</style>
