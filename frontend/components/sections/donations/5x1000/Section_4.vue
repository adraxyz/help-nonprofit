<template>
  <section id="fivepermille-section-4" class="padding-level-3 accent">

    <div class="section-title-center text-center">
      <h1 class="section-title">{{data.title}}</h1>
    </div>

    <div class="text-content text-center">
      <h3>{{data.subtitle}}</h3>
    </div>

    <div class="text-center btn-container">

      <!--      Whatsapp-->
      <v-btn text
             v-ripple="{class: 'no-effects-on-btn-click'}"
             v-if="buttons(0) && buttons(0).active"
             class="custom-btn"
             id="custom-whatsapp-btn"
             data-action="share/whatsapp/share"
             :target="buttons(0).target"
             :href="buttons(0).href">
      </v-btn>
      <!--       Email-->
      <v-btn text
             v-ripple="{class: 'no-effects-on-btn-click'}"
             v-if="buttons(1) && buttons(1).active"
             class="custom-btn"
             id="custom-email-btn"
             :target="buttons(1).target"
             :href="buttons(1).href">
      </v-btn>
      <!--       Facebook-->
      <v-btn text
             v-ripple="{class: 'no-effects-on-btn-click'}"
             v-if="buttons(2) && buttons(2).active"
             class="custom-btn"
             id="custom-facebook-btn"
             :target="buttons(2).target"
             :href="buttons(2).href">
      </v-btn>
      <!--       Linkedin-->
      <v-btn text
             v-ripple="{class: 'no-effects-on-btn-click'}"
             v-if="buttons(3) && buttons(3).active"
             class="custom-btn"
             id="custom-linkedin-btn"
             :target="buttons(3).target"
             :href="buttons(3).href">
      </v-btn>

    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_4",
    props: {
      data: Object
    },
    head() {
      return {
        meta: this.data ? this.data.meta_tags : null
      }
    },
    methods: {
      buttons(index) {
        return this.data.buttons.find(b => b.order === index)
      },
      text(index) {
        return this.data.texts.find(t => t.order === index)
      }
    }
  }
</script>

<style lang="scss">
  #fivepermille-section-4 {
    margin-bottom: 10vh;
    .section-title-center {
      padding-top: 2vh;
    }
    .section-title {
      margin-bottom: 5vh;
      background-image: unset;
      color: white;
    }
    .text-content {
      color: white;
      font-family: "Crossten SemiBold";
    }
    .btn-container {
      padding-top: 3vh;
      padding-bottom: 3vh;
    }
    .no-effects-on-btn-click {
      color: transparent !important;
    }
    .custom-btn:hover:before, .custom-btn:focus:before {
        background-color: unset !important;
    }
    .custom-btn {
      height: 100% !important;
      width: auto !important;
      .v-btn__content {
        background-size: contain !important;
        height: $big-button-height !important;
        width: $big-button-height !important;
        min-width: unset !important;
      }
    }
    #custom-whatsapp-btn {
      .v-btn__content {
        background: url('~assets/icons/custom-whatsapp-icon.png') center center no-repeat;
      }
    }
    #custom-facebook-btn {
      .v-btn__content {
        background: url('~assets/icons/custom-facebook-icon.png') center center no-repeat;
      }
    }
    #custom-linkedin-btn {
      .v-btn__content {
        background: url('~assets/icons/custom-linkedin-icon.png') center center no-repeat;
      }
    }
    #custom-email-btn {
      .v-btn__content {
        background: url('~assets/icons/custom-email-icon.png') center center no-repeat;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #fivepermille-section-4 {
      .text-subtitle {
        font-size: $font-size-18;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #fivepermille-section-4 {
    }
  }
</style>
