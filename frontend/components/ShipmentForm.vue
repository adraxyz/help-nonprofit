<template>

  <v-card class="form-container pa-0 ma-0">

    <v-card-title class="pt-4 pl-6 pr-0 ma-0">
      <h2>{{ getLabel('title') }}</h2>
    </v-card-title>

    <v-card-text class="pb-2 pt-4 pl-6 pr-0 ma-0">

      <form id="shop-shipment-form" class="shipment-form" @submit.prevent="submit" method="post">
        <v-row no-gutters class="shipment-form-row">
          <v-col cols="12" sm="6" class="pr-sm-4">
            <v-text-field
              v-model="first_name"
              :error-messages="first_nameErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="50"
              :label="getLabel('first_name')"
              title=""
              outlined
              @input="$v.first_name.$touch()"
              @blur="$v.first_name.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field
              v-model="last_name"
              :error-messages="last_nameErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="50"
              :label="getLabel('last_name')"
              title=""
              outlined
              @input="$v.last_name.$touch()"
              @blur="$v.last_name.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" class="pr-sm-4">
            <v-text-field
              v-model="email"
              :error-messages="emailErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :label="getLabel('email')"
              title=""
              outlined
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field
              v-model="phone"
              :error-messages="phoneErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="20"
              :label="getLabel('phone')"
              title=""
              outlined
              @input="$v.phone.$touch()"
              @blur="$v.phone.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4" class="pr-sm-4">
            <v-text-field
              v-model="country"
              :error-messages="countryErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="50"
              :label="getLabel('country')"
              title=""
              outlined
              @input="$v.country.$touch()"
              @blur="$v.country.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4" class="pr-sm-4">
            <v-text-field
              v-model="city"
              :error-messages="cityErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="50"
              :label="getLabel('city')"
              title=""
              outlined
              @input="$v.city.$touch()"
              @blur="$v.city.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4">
            <v-text-field
              v-model="province"
              :error-messages="provinceErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="2"
              :label="getLabel('province')"
              title=""
              outlined
              @input="$v.province.$touch()"
              @blur="$v.province.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4" class="pr-sm-4">
            <v-text-field
              v-model="address"
              :error-messages="addressErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="250"
              :label="getLabel('address')"
              title=""
              outlined
              @input="$v.address.$touch()"
              @blur="$v.address.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4" class="pr-sm-4">
            <v-text-field
              v-model="address_number"
              :error-messages="address_numberErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="10"
              :label="getLabel('address_number')"
              title=""
              outlined
              @input="$v.address_number.$touch()"
              @blur="$v.address_number.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4">
            <v-text-field
              v-model="cap"
              :error-messages="capErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
              :counter="5"
              :label="getLabel('cap')"
              title=""
              outlined
              @input="$v.cap.$touch()"
              @blur="$v.cap.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" class="ma-0 pa-0">
            <v-checkbox class="d-inline-block ma-0 pa-0"
              v-model="privacy_agreement"
              :error-messages="privacyAgreementErrors"
              :dense="$vuetify.breakpoint.mdAndDown"
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
          </v-col>
          <v-col cols="12" class="ma-0 pa-0">
            <v-checkbox class="d-inline-block ma-0 pa-0"
              v-model="news_agreement"
              :dense="$vuetify.breakpoint.mdAndDown"
              :hide-details="true"
              title=""
              outlined
              @change="$v.news_agreement.$touch()"
              @blur="$v.news_agreement.$touch()"
            />
            <span class="policy-text">
              {{getLabel('news_agreement')}}
            </span>
          </v-col>
        </v-row>

      </form>

    </v-card-text>

    <v-card-actions class="dialog-actions py-4 pl-6 pr-0 ma-0">

      <v-row no-gutters>

        <v-col cols="12" align="right">
          <v-row no-gutters>
            <v-col cols="12">
              <v-btn type="submit" tile class="button-shadow-secondary-right nav-button"
                     form="shop-shipment-form">
                {{getLabel('submit')}}
              </v-btn>
            </v-col>
          </v-row>
        </v-col>

      </v-row>

    </v-card-actions>

    <!-- Response messages dialog -->
    <v-dialog class="white" v-model="show_response_dialog" max-width="600">
      <v-card tile>

        <v-card-title class="pa-3 cart-summary">
          <v-row no-gutters>
            <v-col cols="12" v-if="response_dialog.email.message">
              <v-icon large :color="response_dialog.email.color" class="mr-3">
                {{ response_dialog.email.icon }}
              </v-icon>
              <span class="response-message">{{ response_dialog.email.message }}</span>
            </v-col>
            <v-col cols="12" v-if="response_dialog.news.message">
              <v-icon large :color="response_dialog.news.color" class="mr-3">
                {{ response_dialog.news.icon }}
              </v-icon>
              <span class="response-message">{{ response_dialog.news.message }}</span>
            </v-col>
          </v-row>
        </v-card-title>

        <v-card-text class="pa-4 d-inline-block cart-summary">
          <v-row no-gutters v-for="p in cart.products" :key="p.order">
            <v-col cols="12" class="d-block">
              <span class="donation-info">{{p.count}} x {{p.title}}</span>
            </v-col>
          </v-row>
          <v-divider class="my-2"></v-divider>
          <v-row no-gutters>
            <v-col cols="12" class="d-block">
              <span class="donation-info">{{getLabel('total_price')}}</span>
              <span class="float-right">{{cart.total}}€</span>
            </v-col>
            <v-col cols="12" class="d-block" v-show="paypal_free_shop.shipping_fees">
              <span class="donation-info">{{getLabel('shipping_fees')}}</span>
              <span class="float-right">{{paypal_free_shop.shipping_fees}}€</span>
            </v-col>
          </v-row>
          <v-divider class="mt-2 mb-4"></v-divider>
          <v-row no-gutters>
            <v-col cols="12" class="d-block">
              <span>{{getLabel('minimum_donation')}}</span>
              <span class="donation-value float-right">{{compute_total_cost()}}€</span>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions class="card-section-content-end">
          <v-btn tile @click="closeDialog"
                 class="button-shadow-secondary-right nav-button ma-2">
            {{getLabel('continue')}}
          </v-btn>
        </v-card-actions>

      </v-card>

    </v-dialog>

  </v-card>

</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
  import { mdiAlert, mdiCheckBold, mdiCloseThick } from "@mdi/js";
  import { mapState } from 'vuex';
  export default {
    name: "ShipmentForm",
    data: () => ({
      email: '',
      first_name: '',
      last_name: '',
      country: '',
      province: '',
      city: '',
      address: '',
      address_number: '',
      cap: '',
      phone: '',
      cart: {total: 0, products: []},
      news_agreement: true,
      privacy_agreement: false,
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
      }
    }),
    async fetch() {
      await this.$store.dispatch('loadShipmentFormLabels')
      await this.$store.dispatch('loadShipmentFormMessages')
      await this.$store.dispatch('loadPaypalFreeShop')
    },
    computed: {
      ...mapState(['locale', 'privacy_policy', 'terms_of_use', 'paypal_free_shop',
        'shopping_cart', 'shipment_form_labels', 'shipment_form_messages']),
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
        !this.$v.first_name.required && errors.push(this.getMessage('required'))
        return errors
      },
      last_nameErrors () {
        const errors = []
        if (!this.$v.last_name.$dirty) return errors
        !this.$v.last_name.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.last_name.required && errors.push(this.getMessage('required'))
        return errors
      },
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push(this.getMessage('email'))
        !this.$v.email.required && errors.push(this.getMessage('required'))
        return errors
      },
      countryErrors () {
        const errors = []
        if (!this.$v.country.$dirty) return errors
        !this.$v.country.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.country.required && errors.push(this.getMessage('required'))
        return errors
      },
      provinceErrors () {
        const errors = []
        if (!this.$v.province.$dirty) return errors
        !this.$v.province.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.province.required && errors.push(this.getMessage('required'))
        return errors
      },
      cityErrors () {
        const errors = []
        if (!this.$v.city.$dirty) return errors
        !this.$v.city.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.city.required && errors.push(this.getMessage('required'))
        return errors
      },
      addressErrors () {
        const errors = []
        if (!this.$v.address.$dirty) return errors
        !this.$v.address.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.address.required && errors.push(this.getMessage('required'))
        return errors
      },
      address_numberErrors () {
        const errors = []
        if (!this.$v.address_number.$dirty) return errors
        !this.$v.address_number.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.address_number.required && errors.push(this.getMessage('required'))
        return errors
      },
      capErrors () {
        const errors = []
        if (!this.$v.cap.$dirty) return errors
        !this.$v.cap.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.cap.required && errors.push(this.getMessage('required'))
        return errors
      },
      phoneErrors () {
        const errors = []
        if (!this.$v.phone.$dirty) return errors
        !this.$v.phone.maxLength && errors.push(this.getMessage('max_length'))
        !this.$v.phone.required && errors.push(this.getMessage('required'))
        return errors
      }
    },
    methods: {
      getLabel(item) {
        if (this.shipment_form_labels instanceof Array) {
          return this.shipment_form_labels.find(l => l.item === item).label
        }
        return ''
      },
      getMessage(text) {
        let msg = this.shipment_form_messages.find(m => m.text.toLowerCase() === text.toLowerCase())
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
              this.locale + '/api/shipment_form',
              {
                'email': this.email,
                'first_name': this.first_name,
                'last_name': this.last_name,
                'country': this.country,
                'province': this.province,
                'city': this.city,
                'address': this.address,
                'address_number': this.address_number,
                'cap': this.cap,
                'phone': this.phone,
                'cart': this.cart,
                'news_agreement': this.news_agreement,
                'privacy_agreement': this.privacy_agreement
              }
            )
            this.$nuxt.$loading.finish()
            this.showMessage(response.data)
            if (response.data.email.status_code === 200) {

            }
          } catch (e) {
            // console.log(e)
          }
        }
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
      compute_products() {
        this.shopping_cart.forEach(
          pc => pc.products.forEach(
            p =>
              (this.cart.total += p.price)
              &&
              (this.cart.products.find(product => (product.order === p.order) && (product.count += 1)))
              ||
              (this.cart.products.push(
                {order: p.order, title: p.title, price: p.price, count: 1}
              ))
          )
        )
      },
      compute_total_cost() {
        return this.paypal_free_shop.shipping_fees ?
          this.cart.total + this.paypal_free_shop.shipping_fees :
          this.cart.total
      },
      closeDialog() {
        this.$store.dispatch('setShipmentFormDialog', {show: false})
        this.$store.dispatch('resetShoppingCart')
        window.open(this.paypal_free_shop.payment_link,'_blank')
        this.clear()
        this.show_response_dialog = false
      },
      clear () {
        this.$v.$reset()
        this.email = ''
        this.first_name =  ''
        this.last_name = ''
        this.country = ''
        this.province = ''
        this.city = ''
        this.address = ''
        this.address_number = ''
        this.cap = ''
        this.phone = ''
        this.news_agreement = true
        this.privacy_agreement = false
        this.cart = {total: 0, products: []}
      },
    },
    mounted() {
      this.compute_products()
    },
    mixins: [validationMixin],
    validations: {
      first_name: {required, maxLength: maxLength(50)},
      last_name: {required, maxLength: maxLength(50)},
      country: {required, maxLength: maxLength(50)},
      province: {required, maxLength: maxLength(2)},
      city: {required, maxLength: maxLength(50)},
      address: {required, maxLength: maxLength(250)},
      address_number: {required, maxLength: maxLength(10)},
      cap: {required, maxLength: maxLength(5)},
      phone: {required, maxLength: maxLength(20)},
      email: {required, email},
      news_agreement: {},
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
  box-shadow: none !important;
  max-width: calc(100% - 30px) !important;
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
  .fieldset {
    border: 2px solid black !important;
  }
  .dialog-actions {
  }
}
.card-section-content-end {
  justify-content: end !important;
}
.donation-info {
  font-family: "Crossten Light" !important;
}
.donation-value {
  font-family: "Crossten Bold";
  font-size: $font-size-30;
}
.cart-summary {
  letter-spacing: 0.15rem !important;
}
@media #{map-get($display-breakpoints, 'xs-only')} {
  .shipment-form-row {
    max-width: 95% !important;
  }
}
</style>
