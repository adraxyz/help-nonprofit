<template>
  <div class="white form-container">

    <form class="contact-form" @submit.prevent="submit" method="post">
      <v-text-field
        v-model="first_name"
        :error-messages="first_nameErrors"
        :dense="$vuetify.breakpoint.xsOnly"
        :counter="30"
        :label="getLabel('first_name')"
        title=""
        outlined
        @input="$v.first_name.$touch()"
        @blur="$v.first_name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="last_name"
        :error-messages="last_nameErrors"
        :dense="$vuetify.breakpoint.xsOnly"
        :counter="30"
        :label="getLabel('last_name')"
        title=""
        outlined
        @input="$v.last_name.$touch()"
        @blur="$v.last_name.$touch()"
      ></v-text-field>
  <!--    <v-text-field-->
  <!--      v-model="where_from"-->
  <!--      :error-messages="where_fromErrors"-->
  <!--      :counter="30"-->
  <!--      :label="getLabel('where_from')"-->
  <!--      title=""-->
  <!--      outlined-->
  <!--      @input="$v.where_from.$touch()"-->
  <!--      @blur="$v.where_from.$touch()"-->
  <!--    ></v-text-field>-->
      <v-text-field
        v-model="email"
        :error-messages="emailErrors"
        :dense="$vuetify.breakpoint.xsOnly"
        :label="getLabel('email')"
        title=""
        outlined
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
      ></v-text-field>
      <v-row no-gutters align="center">
        <v-checkbox class="mt-0 pt-0"
          v-model="privacy_agreement"
          :error-messages="privacyAgreementErrors"
          :dense="$vuetify.breakpoint.xsOnly"
          :hide-details="true"
          title=""
          outlined
          @change="$v.privacy_agreement.$touch()"
          @blur="$v.privacy_agreement.$touch()"
        />
        <span class="policy-text">
          {{getLabel('privacy_agreement')}}
          (<a :href="privacy_policy.file" target="_blank">Privacy Policy</a> &
          <a :href="terms_of_use.file" target="_blank">Terms of use</a>)
        </span>
      </v-row>
      <div class="mt-5">
        <v-btn type="submit" tile class="button-shadow-secondary-right section-button mr-4">
          {{getLabel('submit')}}
        </v-btn>
      </div>
    </form>

    <!-- Response messages -->
    <div v-if="show_response" class="response-container">
      <v-icon large :color="response.color" class="mr-3">{{ response.icon }}</v-icon>
      <span class="response-message">{{ response.message }}</span>
    </div>

  </div>

</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
  import {mdiAlert, mdiCheckBold, mdiCloseThick} from "@mdi/js";
  import { mapState } from 'vuex';
  export default {
    name: "ContactForm",
    data: () => ({
      first_name: '',
      last_name: '',
      where_from: '',
      email: '',
      privacy_dialog: false,
      privacy_agreement: false,
      close_icon: mdiCloseThick,
      show_response: false,
      response: {
        color: 'primary',
        message: 'Success!',
        icon: mdiCheckBold
      }
    }),
    async fetch() {
      await this.$store.dispatch('loadContactFormLabels')
      await this.$store.dispatch('loadContactFormMessages')
    },
    computed: {
      ...mapState(['locale', 'privacy_policy', 'terms_of_use', 'contact_form_labels', 'contact_form_messages']),
      privacyAgreementErrors () {
        const errors = []
        if (!this.$v.privacy_agreement.$dirty) return errors
        !this.$v.privacy_agreement.checked && errors.push(this.getMessage('agreement'))
        return errors
      },
      first_nameErrors () {
        const errors = []
        if (!this.$v.first_name.$dirty) return errors
        !this.$v.first_name.maxLength && errors.push(this.getMessage('max_length'))
        return errors
      },
      last_nameErrors () {
        const errors = []
        if (!this.$v.last_name.$dirty) return errors
        !this.$v.last_name.maxLength && errors.push(this.getMessage('max_length'))
        return errors
      },
      where_fromErrors () {
        const errors = []
        if (!this.$v.where_from.$dirty) return errors
        !this.$v.where_from.maxLength && errors.push(this.getMessage('max_length'))
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
      getLabel(item) {
        if (this.contact_form_labels instanceof Array) {
          return this.contact_form_labels.find(l => l.item === item).label
        }
        return ''
      },
      getMessage(text) {
        let msg = this.contact_form_messages.find(m => m.text.toLowerCase() === text.toLowerCase())
        if (msg) {
          return msg.text_to_users
        }
        return ''
      },
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
              this.locale + '/api/subscribe',
              {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
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
      showMessage(data) {
        let color = 'primary'
        let icon = mdiCheckBold
        if (data.status_code != 200) {
          color = 'error'
          icon = mdiAlert
        }
        this.response.color = color
        this.response.message = data.message
        this.response.icon = icon
        this.show_response = true
      }
    },
    mixins: [validationMixin],
    validations: {
      first_name: {maxLength: maxLength(30)},
      last_name: {maxLength: maxLength(30)},
      where_from: {maxLength: maxLength(50)},
      email: {required, email},
      privacy_agreement: {
        checked(val) {
          return val
        }
      }
    }
  }
</script>

<style lang="scss">
.form-container {
  margin-top: 4vh;
  margin-bottom: 4vh;
  margin-left: 2vw;
  margin-right: 2vw;
  .buttons {
    box-shadow: $box-shadow-side $box-shadow-bottom $secondary-color;
    background-color: white;
    border: 2px solid black !important;
    font-family: "Crossten Bold";
  }
  .response-container {
    margin-top: 2vh;
  }
  .v-text-field--outlined {
    border-radius: 0px !important;
  }
  .policy-text {
    max-width: calc(100% - 40px);
  }
  fieldset {
    border: 2px solid black !important;
  }
}
</style>
