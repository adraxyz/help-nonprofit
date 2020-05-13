<template>
  <section id="projects-details-section-2" class="padding-level-3">

    <div class="section-title-left">
      <span class="section-title">{{data.title}}</span>
    </div>

    <div class="text-content" v-html="context_text.content"/>
    <div class="section-gallery">
      <v-row no-gutters class="section-row">
        <span v-if="false">{{context_images}}</span>
        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
          <template v-slot:activator="{ on }">
            <v-col v-for="i in context_images" :key="i.order" cols="12"
                   :sm="smCols(i.content)" class="section-col">
              <v-img :src="i.content" class="project-image" cover v-on="on"
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
    name: "Section_2",
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
    computed: {
      context_text() {
        return this.project.texts.find(t => t.project_section === "context")
      },
      context_images() {
        let images = this.project.images.filter(i => i.project_section === "context")
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
  .v-dialog__content {
    .dialog-content-container {
      background-color: $grey-color;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .fullscreen-image {
      max-height: 100vh;
      max-width: 100vw;
    }
    .close-btn {
      box-shadow: none !important;
    }
  }
  #projects-details-section-2 {
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
    #projects-details-section-2   {
      .project-image {
        margin-top: 0px;
        margin-left: 0px;
        margin-right: 0px;
        margin-bottom: $md-down-logo-margin;
      }
    }
  }
</style>
