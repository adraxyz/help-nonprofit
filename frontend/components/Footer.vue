<template>
  <div id="footer-container" class="secondary">
    <v-row class="footer-row" no-gutters>

      <v-col class="text-center footer-col" cols="12" md="4" order-md="0" order="1">
        <h1 class="footer-title">{{ data.footer_1_col_title }}</h1>
        <div class="text-content">
          <span v-html="data.footer_1_col_text"></span>
        </div>
      </v-col>

      <v-col cols="12" md="8" order-md="1" order="0" class="text-center">

        <v-row no-gutters>
          <v-col cols="12" md="6" class="footer-col">
            <h1 class="footer-title">{{ data.footer_2_col_title }}</h1>
            <div class="text-content">
              <span v-html="data.footer_2_col_text"></span>
            </div>
            <v-btn class="d-inline-block button-shadow-primary-right nav-button"
                   tile @click="subscribe_dialog=true">{{ data.subscribe_btn_text }}</v-btn>
          </v-col>
          <v-col cols="12" md="6" class="footer-col">
            <h1 class="footer-title">{{ data.footer_3_col_title }}</h1>
            <div class="text-content">
              <span v-html="data.footer_3_col_text"></span>
            </div>
            <div class="social-container">
              <SocialIcons :vertical="false" :shadow="false" icon_custom_class="mx-2"/>
            </div>
          </v-col>
        </v-row>

        <v-row no-gutters class="nested-row">
          <v-col cols="12" md="6" order="1" order-md="0" class="footer-col">
            <h1 class="footer-title">{{data.transparency_title}}</h1>
            <a v-if="data.document_0" target="_blank" :href="data.document_0.file"
               class="text-content doc-link">
              <b>{{ data.document_0.title }}</b>
            </a>
            <br>
            <a v-if="data.document_1" target="_blank" :href="data.document_1.file"
               class="text-content doc-link">
              <b>{{ data.document_1.title }}</b>
            </a>
          </v-col>
          <v-col cols="12" md="6" order="0" order-md="1" class="footer-col">
            <h1 class="footer-title">{{ data.donation_title }}</h1>
            <div>
              <v-btn :to="localePath(donation_button.to)" class="rounded-btn white"
                     fab dark outlined nuxt active-class="no-active">
                <v-icon id="small-icon" color="error">mdi-heart</v-icon>
              </v-btn>
            </div>
          </v-col>
        </v-row>

      </v-col>

    </v-row>

    <!-- Bottom line -->
    <v-row no-gutters>
      <v-col cols="12" class="last-footer-cols pb-0">
        <span>@{{ new Date().getFullYear() }} <b>{{ data.corporate_short_name }}</b></span>
      </v-col>
      <v-col cols="12" class="last-footer-cols pt-1 pb-4">
        <v-row no-gutters>
          <v-col cols="auto">
          <a @click="privacy_dialog=true">Privacy Policy</a> |
          <span>{{ data.email }}</span> |
          <nuxt-link :to="localePath(contact_button.to)">{{ contact_button.text_1 }}</nuxt-link> |
          <span>CF: {{ data.fiscal_code }}</span> |
          <span>{{ data.registered_office }}</span>
          </v-col>
          <v-spacer/>
          <v-col cols="auto" class="mt-3 mt-sm-0">
            <span>
              [
                <nuxt-link v-for="lang in locales" :key="lang.code"
                           :to="switchLocalePath(lang.code)" >
                  <span>{{ lang.code }} </span>
                </nuxt-link>
              ]
            </span>
          </v-col>
        </v-row>
      </v-col>

    </v-row>

    <!-- Privacy Policy dialog -->
    <v-dialog v-model="privacy_dialog" class="white" scrollable persistent max-width="90vw">
      <v-card tile>
        <v-card-title>
          <v-icon class="close-icon ma-2" @click="privacy_dialog=false">
            {{ close_icon }}
          </v-icon>
        </v-card-title>
        <v-card-text class="pa-3">
          <span v-html="privacy_text"/>
        </v-card-text>
      </v-card>
    </v-dialog>

    <!-- Subscribe dialog -->
    <v-dialog v-model="subscribe_dialog" class="white" scrollable persistent max-width="800px">
      <div class="white dialog-container">
        <v-icon class="float-right ma-2" @click="subscribe_dialog=false">
          {{ close_icon }}
        </v-icon>
        <div class="dialog-form-container">
          <!-- key used to reset the form -->
          <ContactForm :key="subscribe_dialog"/>
        </div>
      </div>
    </v-dialog>

  </div>
</template>

<script>
  import SocialIcons from "./layouts/default/SocialIcons";
  import ContactForm from "./ContactForm";
  import { mdiCloseThick } from '@mdi/js'
  import { mapState } from 'vuex';
  export default {
    name: "Footer",
    props: {
      data: Object,
      donation_button: Object,
      contact_button: Object,
      privacy_text: String
    },
    components: {
      ContactForm,
      SocialIcons
    },
    data: () => ({
      subscriber_email: '',
      privacy_dialog: false,
      subscribe_dialog: false,
      close_icon: mdiCloseThick
    }),
    computed: {
      ...mapState(['locale', 'locales'])
    },
  }
</script>

<style lang="scss">
  #footer-container {
    /*z-index: 2; TODO z-index */
    position: relative;
    color: white;
    .contact-icon {
      height: $circle-icon-size * 0.45;
      width: $circle-icon-size * 0.45;
    }
    a {
      text-decoration: none !important;
      color: white !important;
      font-weight: bold;
    }
    .v-card__text {
      font-size: large !important;
    }
    .nav-button {
      margin-top: 2vh;
    }
    .social-container {
      margin-top: 2vh;
    }
    .text-content {
      font-size: $font-size-15 !important;
      font-family: "Crossten Book";
    }
    .nested-row {
      margin-top: 2vh;
    }
    .footer-col {
      padding-top: 2vh !important;
      padding-left: 4vw !important;
      padding-right: 4vw !important;
    }
    #social-icons-container {
      margin-right: 0px !important;
    }
    .doc-link {
      font-family: "Crossten Bold";
    }
  }
  #emailField {
    height: $nav-button-height;
    width: $nav-button-width * 1.5;
    color: black;
  }
  .dialog-form-container {
    margin-top: 50px;
  }
  .dialog-container {
    height: 100%;
  }
  .footer-title {
    margin-bottom: 10px;
    letter-spacing: 0.15rem;
  }
  .trasparenza {
    margin-top: 2vh;
    margin-bottom: 10px;
  }
  .last-footer-cols {
    font-family: "Crossten Book";
    font-size: $font-size-15;
    /*padding: 2vw !important;*/
    padding-top: 2vh !important;
    padding-left: 2vw !important;
    padding-right: 2vw !important;
  }
  #newsletter-message {
    word-break: break-word;
  }
  .close-icon {
    right: 0 !important;
    position: absolute !important;
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #footer-container {
      .footer-col {
        margin-bottom: 4vh;
      }
    }
  }
</style>
