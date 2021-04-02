<template>
  <section id="fivepermille-section-2" class="padding-level-3 error">

    <v-row no-gutters>
      <v-col class="text-center pa-3" v-if="document(0)">
        <div class="text-content">{{document(0).subtitle}}</div>
        <h1 class="text-title">{{document(0).title}}</h1>
        <br>
        <v-btn text
               v-ripple="{class: 'no-effects-on-btn-click'}"
               class="custom-btn mt-2"
               id="module-btn"
               data-action="share/whatsapp/share"
               target="_blank"
               :href="document(0).file">
      </v-btn>
      </v-col>
      <v-col class="text-center pa-3" v-if="document(1)">
        <div class="text-content">{{document(1).subtitle}}</div>
        <h1 class="text-title">{{document(1).title}}</h1>
        <br>
        <v-btn text
               v-ripple="{class: 'no-effects-on-btn-click'}"
               class="custom-btn mt-2"
               id="communication-kit-btn"
               data-action="share/whatsapp/share"
               target="_blank"
               :href="document(1).file">
      </v-btn>
      </v-col>
    </v-row>

  </section>
</template>

<script>
  export default {
    name: "Section_2",
    props: {
      data: Object
    },
    head() {
      return {
        meta: this.data ? this.data.meta_tags : null
      }
    },
    methods: {
      button(index) {
        return this.data ? this.data.buttons.find(b => b.order === index) : null
      },
      document(index) {
        return this.data ? this.data.documents.find(t => t.order === index) : null
      }
    }
  }
</script>

<style lang="scss">
  #fivepermille-section-2 {
    margin-top: 5vh;
    margin-bottom: 5vh;
    .text-content {
      font-family: "Crossten SemiBold";
      color: white;
    }
    .text-title {
      color: white;
    }
    .no-effects-on-btn-click {
      color: transparent !important;
    }
    .custom-btn:hover:before, .custom-btn:focus:before {
        background-color: unset !important;
    }
    .custom-btn {
      height: $big-button-height !important;
      width: $big-button-height !important;
      width: auto !important;
      padding: 0 !important;
      .v-btn__content {
        background-size: contain !important;
        height: 100% !important;
        width: 100% !important;
      }
    }
    #module-btn {
      .v-btn__content {
        background: url('~assets/icons/module-icon.png') center center no-repeat;
      }
    }
    #communication-kit-btn {
      .v-btn__content {
        background: url('~assets/icons/communication-kit-icon.png') center center no-repeat;
      }
    }
  }
</style>
