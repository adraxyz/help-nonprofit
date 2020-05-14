<template>
  <section id="about-section-3" class="padding-level-2" v-resize="onResize">
    <div class="section-title-center text-center">
      <span class="section-title">{{data.title}}</span>
    </div>
    <div class="relative-div">
      <v-img class="section-image" :src="sectionImage" contain></v-img>
      <div class="first-address">
        <span class="d-block">{{text(0).title}}</span>
        <span class="address d-block">{{text(0).subtitle}}</span>
      </div>
      <div class="second-address">
        <span class="d-block">{{text(1).title}}</span>
        <span class="address d-block">{{text(1).subtitle}}</span>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_3",
    props: {
      data: Object
    },
    data: () => ({
      section_height: 0
    }),
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      sectionImage() {
        return this.data.images[0].content
      }
    },
    methods: {
      text(index) {
        return this.data.texts.find(t => t.order === index)
      },
      onResize () {
        this.section_height = window.innerHeight
        document.documentElement.style.setProperty('--100vh', `${this.section_height}px`);
      }
    }
  }
</script>

<style lang="scss">
  #about-section-3 {
    .relative-div {
      position: relative;
    }
    .section-image {
      max-width: 90%;
      max-height: calc(var(--100vh) - #{$logo-size} - #{$logo-margin});
    }
    .first-address {
      font-family: "Crossten Bold";
      font-size: 40px;
      line-height: 100%;
      color: $secondary-color;
      letter-spacing: 0.15rem;
      position: absolute;
      left: 50%;
      top: 10%;
    }
    .second-address {
      font-family: "Crossten Bold";
      font-size: 40px;
      line-height: 100%;
      color: $error-color;
      letter-spacing: 0.15rem;
      position: absolute;
      top: 35%;
      right: 10%;
      max-width: 30%;
    }
    .address {
      font-family: "Crossten Thin";
      font-size: 20px;
      color: black;
      line-height: 100%;
      padding-top: 0.5vh;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #about-section-3 {
      .first-address {
        left: 40%;
      }
      .second-address {
        top: 35%;
        right: 5%;
        max-width: 40%;
      }
      .section-image {
        max-height: calc(var(--100vh) - #{$md-logo-size} - #{$md-logo-margin});
        padding-top: 0px !important;
        max-width: 80%;
      }
    }
    /*@media (min-aspect-ratio: 1/1) {
      @media (max-height: 700px) {
        #about-section-3 {
          .first-address {
            left: 50%;
          }
          .second-address {
            top: 40%;
          }
        }
      }
    }*/
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #about-section-3 {
      .first-address {
        font-size: 25px;
      }
      .second-address {
        font-size: 25px;
        right: 0;
      }
      .address {
        font-size: 18px;
      }
      .section-image {
        padding-top: 0;
      }
    }
    @media (min-aspect-ratio: 1/1) {
      #about-section-3 {
        .first-address {
          left: 60% !important;
        }
        .second-address {
          top: 40%;
        }
      }
    }
    /*@media (min-width: 650px) {*/
    /*  #about-section-3 {*/
    /*    .section-image {*/
    /*      max-width: 80%;*/
    /*    }*/
    /*    .second-address {*/
    /*      top: 35%;*/
    /*      !*max-width: 50% !important;*!*/
    /*    }*/
    /*    .first-address {*/
    /*      top: 5%;*/
    /*    }*/
    /*  }*/
    /*}*/
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #about-section-3 {
      .first-address {
        top: 0;
        font-size: 18px;
        right: 0;
      }
      .second-address {
        top: 30%;
        font-size: 18px;
        max-width: 33%;
      }
      .address {
        font-size: 15px;
      }
      .section-image {
        padding-top: 0vh !important;
        max-width: 80%;
      }
    }
    @media (min-aspect-ratio: 1/1) {
      #about-section-3 {
        .second-address {
          top: 35%;
          max-width: 60% !important;
        }
      }
    }
    @media (max-width: 400px) {
      #about-section-3 {
        .section-image {
          padding-top: 10vh !important;
          max-width: 70%;
        }
      }
    }
  }
</style>
