<template>
  <section id="projects-details-section-0" class="padding-level-2" v-resize="onResize">
    <div class="content-container">
      <v-img class="section-image" contain
             :src="alt_img_content ? final_image.alt_content : final_image.content"/>
      <div class="section-text text-center">
<!--        <span class="d-block">{{data.title}}</span>-->

        <PulsingArrow/>

      </div>
    </div>
  </section>
</template>

<script>
  import PulsingArrow from "../../../PulsingArrow";
  export default {
    name: "Section_0",
    props: {
      data: Object,
      project: Object
    },
    components: {
      PulsingArrow
    },
    data () {
      return {
        alt_img_content: false
      }
    },
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      final_image() {
        return this.project.images.find(
          i => i.project_section === "design" && i.order === 0
        )
      }
    },
    methods: {
      onResize() {
        this.alt_img_content = window.innerWidth/window.innerHeight < 1
      }
    }
  }
</script>

<style lang="scss">
  #projects-details-section-0 {
    padding-top: $logo-size;
    min-height: 100vh;
    .content-container {
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      height: calc(100vh - #{$logo-size + $logo-margin});
    }
    .section-image {
      max-height: calc(100vh - #{$logo-size + $logo-margin});
    }
    .section-text {
      position: absolute;
      font-family: "Crossten Book";
      color: $primary-color;
      font-size: 40px;
      /*margin-left: 15vw;*/
      right: 15vw;
      padding-bottom: 20vh;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #projects-details-section-0 {
      padding-top: $md-logo-size;
    }
    @media (max-height: 600px) and (min-aspect-ratio: 1/1){
      #projects-details-section-0 {
        padding-top: $md-logo-margin;
        .content-container {
          height: calc(100vh - #{$md-logo-margin}*2);
        }
        .section-image {
          max-height: 100%;
        }
        .section-text {
          font-size: 25px;
        }
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #projects-details-section-0 {
      .section-text {
        font-size: 25px;
      }
      .section-text {
        padding-left: 0px;
      }
    }
  }
</style>
