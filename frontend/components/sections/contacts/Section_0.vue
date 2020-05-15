<template>
  <section id="contacts-section-0" class="padding-level-3" v-resize="onResize">
    <v-row class="section-row" no-gutters align="center" align-content="center" justify="center">
      <v-col cols="12" md="7" class="">
        <v-form class="section-form text-content" @submit.prevent="submit" method="post">

          <v-text-field
            v-model="firstname"
            :error-messages="firstnameErrors"
            :counter="30"
            :label="firstnameTextField.title"
            :dense="$vuetify.breakpoint.smAndDown"
            title=""
            outlined
            @input="$v.firstname.$touch()"
            @blur="$v.firstname.$touch()"
          ></v-text-field>
          <v-text-field
            v-model="lastname"
            :error-messages="lastnameErrors"
            :counter="30"
            :label="lastnameTextField.title"
            :dense="$vuetify.breakpoint.smAndDown"
            title=""
            outlined
            @input="$v.lastname.$touch()"
            @blur="$v.lastname.$touch()"
          ></v-text-field>
          <v-text-field
            v-model="email"
            :error-messages="emailErrors"
            :label="emailTextField.title"
            :dense="$vuetify.breakpoint.smAndDown"
            title=""
            outlined
            @input="$v.email.$touch()"
            @blur="$v.email.$touch()"
          ></v-text-field>
          <v-select
            v-model="object"
            :items="getItems(objectSelectField)"
            :error-messages="objectErrors"
            :label="objectSelectField.title"
            :dense="$vuetify.breakpoint.smAndDown"
            title=""
            outlined
            @change="$v.object.$touch()"
            @blur="$v.object.$touch()"
          ></v-select>
          <v-textarea
            v-model="message"
            :error-messages="messageErrors"
            :label="messageTextAreaField.title"
            :dense="$vuetify.breakpoint.smAndDown"
            outlined
            title=""
            @input="$v.message.$touch()"
            @blur="$v.message.$touch()"
          ></v-textarea>
          <v-checkbox class="mt-0 pt-0"
            v-model="news_agreement"
            :error-messages="newsAgreementErrors"
            :label="newsAgreementCheckBoxField.title"
            :dense="$vuetify.breakpoint.smAndDown"
            title=""
            outlined
            @change="$v.news_agreement.$touch()"
            @blur="$v.news_agreement.$touch()"
          ></v-checkbox>
          <v-checkbox class="mt-0 pt-0"
            v-model="privacy_agreement"
            :error-messages="privacyAgreementErrors"
            :dense="$vuetify.breakpoint.smAndDown"
            title=""
            outlined
            @change="$v.privacy_agreement.$touch()"
            @blur="$v.privacy_agreement.$touch()"
          >
            <template v-slot:label>
              <v-row no-gutters>
                <v-col cols="12">
                  <span>{{privacyAgreementCheckBoxField.title}}</span>
                  <span>(<a @click="privacy_dialog=true">Privacy Policy</a>)</span>
                </v-col>
<!--                <v-col cols="12" sm="4"><span>( <a @click="privacy_dialog=true">Privacy Policy</a> )</span></v-col>-->
              </v-row>
            </template>
          </v-checkbox>

          <!-- Buttons -->
          <div class="mt-1 mt-md-5">
            <v-btn type="submit" tile class="button-shadow-primary-right section-button mr-4">
              {{submitButton.text_0}}
            </v-btn>
            <v-btn tile class="button-shadow-secondary-right section-button clear-button" @click="clear">
              {{clearButton.text_0}}
            </v-btn>
          </div>

        </v-form>
      </v-col>

      <v-col cols="12" md="5" class="text-center image-col">
        <v-img :src="sectionImage.content" class="section-image" contain/>
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

    <!-- Response messages dialog -->
    <v-dialog class="white" v-model="show_response_dialog" persistent max-width="600">
      <v-card tile>
        <v-card-title>
          <v-icon class="close-icon ma-2" @click="show_response_dialog=false">
            {{ close_icon }}
          </v-icon>
        </v-card-title>
        <v-card-text class="pa-3 pt-0">
          <v-icon large :color="response_dialog.email.color" class="mr-3">{{ response_dialog.email.icon }}</v-icon>
          <span class="response-message">{{ response_dialog.email.message }}</span>
        </v-card-text>
        <v-card-text class="pa-3" v-if="response_dialog.news.message">
          <v-icon large :color="response_dialog.news.color" class="mr-3">{{ response_dialog.news.icon }}</v-icon>
          <span class="response-message">{{ response_dialog.news.message }}</span>
        </v-card-text>
      </v-card>
    </v-dialog>

  </section>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
  import {mdiAlert, mdiCheckBold, mdiCloseThick} from '@mdi/js'
  import { mapState } from 'vuex';

  export default {
    name: "Section_0",
    props: {
      data: Object
    },
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    data: () => ({
      firstname: '',
      lastname: '',
      email: '',
      base_object: null,
      object: null,
      message: '',
      news_agreement: true,
      privacy_agreement: false,
      privacy_dialog: false,
      close_icon: mdiCloseThick,
      show_response_dialog: false,
      response_dialog: {
        email: {
          color: 'primary',
          message: 'Success!',
          icon: mdiCheckBold
        },
        news: {
          color: '',
          message: '',
          icon: null
        }
      },
    }),
    mixins: [validationMixin],
    validations: {
      firstname: {required, maxLength: maxLength(30)},
      lastname: {maxLength: maxLength(30)},
      email: {required, email},
      object: {required},
      message: {required},
      news_agreement: {},
      privacy_agreement: {
        checked(val) {
          return val
        }
      }
    },
    computed: {
      ...mapState(['locale', 'contact_form_messages', 'privacy_text']),
      submitButton() {
        return this.data.buttons.find(b => b.order === 0)
      },
      clearButton() {
        return this.data.buttons.find(b => b.order === 1)
      },
      sectionImage() {
        return this.data.images.find(i => i.order === 0)
      },
      firstnameTextField() {
        return this.data.texts.find(t => t.order === 0)
      },
      lastnameTextField() {
        return this.data.texts.find(t => t.order === 1)
      },
      emailTextField() {
        return this.data.texts.find(t => t.order === 2)
      },
      objectSelectField() {
        let obj = this.data.texts.find(t => t.order === 3)
        this.base_object = this.getItems(obj)[0]
        this.object = this.getItems(obj)[0]
        return obj
      },
      messageTextAreaField() {
        return this.data.texts.find(t => t.order === 4)
      },
      newsAgreementCheckBoxField() {
        return this.data.texts.find(t => t.order === 5)
      },
      privacyAgreementCheckBoxField() {
        return this.data.texts.find(t => t.order === 6)
      },
      newsAgreementErrors () {
        const errors = []
        if (!this.$v.privacy_agreement.$dirty) return errors
        return errors
      },
      privacyAgreementErrors () {
        const errors = []
        if (!this.$v.privacy_agreement.$dirty) return errors
        !this.$v.privacy_agreement.checked && errors.push(this.getMessage('agreement'))
        return errors
      },
      objectErrors () {
        const errors = []
        if (!this.$v.object.$dirty) return errors
        !this.$v.object.required && errors.push(this.getMessage('required'))
        return errors
      },
      messageErrors () {
        const errors = []
        if (!this.$v.message.$dirty) return errors
        !this.$v.message.required && errors.push(this.getMessage('required'))
        return errors
      },
      firstnameErrors () {
        const errors = []
        if (!this.$v.firstname.$dirty) return errors
        !this.$v.firstname.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.firstname.required && errors.push(this.getMessage('required'))
        return errors
      },
      lastnameErrors () {
        const errors = []
        if (!this.$v.lastname.$dirty) return errors
        !this.$v.lastname.maxLength && errors.push(this.getMessage('max_length'))
        return errors
      },
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push(this.getMessage('email'))
        !this.$v.email.required && errors.push(this.getMessage('required'))
        return errors
      }
    },
    methods: {
      async submit () {
        this.$v.$touch()
        if (!this.$v.$invalid) {
          try {
            this.$nuxt.$loading.start()
            this.$axios.defaults.xsrfCookieName = 'csrftoken';
            this.$axios.defaults.xsrfHeaderName = 'X-CSRFToken';
            const csrftoken = this.$cookies.get('csrftoken')
            this.$axios.setHeader('X-CSRFToken', csrftoken)
            let response = await this.$axios.post(
              this.locale + '/api/contact_form',
              {
                'firstname': this.firstname,
                'lastname': this.lastname,
                'email': this.email,
                'object': this.object,
                'message': this.message,
                'news_agreement': this.news_agreement,
                'privacy_agreement': this.privacy_agreement
              }
            )
            this.$nuxt.$loading.finish()
            this.showMessage(response.data)
          } catch (e) {
            // console.log(e)
          }
        }
      },
      clear () {
        this.$v.$reset()
        this.firstname = ''
        this.lastname = ''
        this.email = ''
        this.object = this.base_object
        this.message = ''
        this.news_agreement = true
        this.privacy_agreement = false
      },
      getMessage(text) {
        let msg = this.contact_form_messages.find(m => m.text.toLowerCase() === text.toLowerCase())
        if (msg) {
          return msg.text_to_users
        }
        return ''
      },
      getItems(obj) {
        return obj.content.split(',')
      },
      showMessage(data) {
        let email_color = 'primary'
        let email_icon = mdiCheckBold
        let news_color = ''
        let news_icon = null
        if (data.email.status_code != 200) {
          email_color = 'error'
          email_icon = mdiAlert
        }
        this.response_dialog.email.color = email_color
        this.response_dialog.email.message = data.email.message
        this.response_dialog.email.icon = email_icon
        if (data.news.status_code) {
          if (data.news.status_code != 200) {
            news_color = 'error'
            news_icon = mdiAlert
          } else {
            news_color = 'primary'
            news_icon = mdiCheckBold
          }
        }
        this.response_dialog.news.color = news_color
        this.response_dialog.news.message = data.news.message
        this.response_dialog.news.icon = news_icon
        this.show_response_dialog = true
      },
      onResize () {
        document.documentElement.style.setProperty('--100vh', `${window.innerHeight}px`);
      }
    }
  }
</script>

<style lang="scss">
  #contacts-section-0 {
    padding-top: $logo-size + $logo-margin;
    margin-bottom: 5vh;
    min-height: var(--100vh);
    .section-form {
      .v-text-field--outlined {
        border-radius: 0px !important;
      }
      fieldset {
        border: 2px solid black !important;
      }
    }
    .section-row {
      min-height: calc(var(--100vh) - #{$logo-size} - #{$logo-margin})
    }
    .section-image {
      /*max-width: calc(100vw - #{$md-up-top-bar-height}*2 - #{$logo-margin}*2);*/
      padding-left: 5vw;
    }
    .buttons {
      box-shadow: $box-shadow-side $box-shadow-bottom $primary-color;
      background-color: white;
      border: 2px solid black !important;
      font-family: "Crossten Bold";
    }
    .clear-button {
      box-shadow: $box-shadow-side $box-shadow-bottom $secondary-color;
    }
    .response-message {
      word-break: break-word;
    }
    .close-icon {
      right: 0 !important;
      position: absolute !important;
    }
  }
  .v-menu__content {
    box-shadow: none !important;
    border: 2px solid black !important;;
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #contacts-section-0 {
      padding-top: $md-logo-size;
      .section-row {
        min-height: calc(var(--100vh) - #{$md-logo-size} - #{$md-logo-margin})
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #contacts-section-0 {
      padding-top: calc(#{$md-logo-size} + 2vh);
      .section-image {
        padding-left: 0px;
        padding-top: 5vh;
        padding-bottom: 5vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #contacts-section-0 {
    }
    @media (max-width: 400px) {
      #contacts-section-0 {
        .section-image {
        }
      }
    }
  }
</style>
