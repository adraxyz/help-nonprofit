<template>

  <div id="shopping-cart" class="mt-5 text-right">

    <div v-show="products_count>0 && $vuetify.breakpoint.mdAndUp"
         class="text-right cart-container px-4 pt-2 pb-1">

      <div class="cart-title text-center mb-2">
        <span>{{getLabel('title')}}</span>
      </div>

      <div v-for="pc in shopping_cart" :key="pc.order"
           v-show="pc.internal && pc.products.length>0">
        <span class="product-quantity float-left">{{pc.products.length}}</span>
        <span class="float-left ml-1 mr-3">x</span>
        <span>{{pc.title}}</span>
      </div>

      <div class="text-center mt-2">
        <v-btn @click="setShipmentFormDialog(true)" tile
               class="cart-button button-shadow-primary-left my-2">
          <span>{{getLabel('purchase_order')}}</span>
        </v-btn>
        <a class="cart-button-text d-block" @click="clearCart">
          <span>{{getLabel('reset_cart')}}</span>
          <!--<v-icon>{{delete_icon}}</v-icon>-->
        </a>
      </div>

    </div>

    <div v-show="products_count>0 && $vuetify.breakpoint.smAndDown"
         class="text-right pt-4">
      <span class="product-count">{{products_count}}</span>
      <v-btn @click="setShipmentFormDialog(true)" text fab width="37" height="37"
             class="cart-button-icon mb-2">
        <v-icon class="cart-icon" small>{{cart_icon}}</v-icon>
      </v-btn>
      <br>
    </div>

    <!-- Shopping Cart dialog -->
    <v-dialog :value="shipment_form_dialog"
              class="white shipment-dialog ma-0"
              max-width="1000px"
              scrollable persistent>

      <ShipmentForm :key="shipment_form_dialog"/>

      <v-icon class="dialog-close-icon pa-0 ma-0 pt-2" @click="setShipmentFormDialog(false)">
        {{ close_icon }}
      </v-icon>

    </v-dialog>

  </div>
</template>

<script>
import {mapState} from "vuex";
import {mdiCloseThick, mdiCartOutline} from "@mdi/js";
import ShipmentForm from "@/components/ShipmentForm";

export default {
  name: "ShoppingCart",
  components: {
    ShipmentForm
  },
  data: () => ({
    close_icon: mdiCloseThick,
    cart_icon: mdiCartOutline
  }),
  computed: {
    ...mapState(['shopping_cart', 'shipment_form_dialog', 'shopping_cart_labels']),
    products_count() {
      let count = 0
      let internal_products_categories = this.shopping_cart.filter(pc => pc.internal)
      internal_products_categories.forEach(ipc => count += ipc.products.length)
      return count
    }
  },
  async fetch() {
    await this.$store.dispatch('loadShoppingCart')
    await this.$store.dispatch('loadShoppingCartLabels')
  },
  methods: {
    setShipmentFormDialog(show) {
      this.$store.dispatch('setShipmentFormDialog', {show: show})
    },
    clearCart() {
      this.$store.dispatch('resetShoppingCart')
    },
    getLabel(item) {
      if (this.shopping_cart_labels instanceof Array) {
        return this.shopping_cart_labels.find(l => l.item === item).label
      }
      return ''
    }
  }

}
</script>

<style lang="scss">
.shipment-dialog {
  z-index: 1001;
}
#shopping-cart {
  font-family: "Crossten Light";
  letter-spacing: 0.15rem !important;
}
.cart-container {
  border: 2px solid black !important;
  background-color: white;
}
.dialog-close-icon {
  max-width: 24px !important;
  max-height: 24px !important;
}
.cart-button {
  border: 2px solid black !important;
  font-family: "Crossten Bold";
  letter-spacing: 0.15rem !important;
}
.cart-button-text {
  font-family: "Crossten Bold";
  color: $error-color !important;
}
.cart-button-icon {
  border: 2px solid black !important;
  font-family: "Crossten Bold";
  box-shadow: 0 0 0 0 $error-color;
	transform: scale(1);
	animation: pulse 3s infinite;
}
.product-quantity {
  font-family: "Crossten Bold";
}
.product-count {
  color: $error-color;
  font-family: "Crossten Bold";
  position: absolute;
  bottom: 42px;
}
.cart-title {
  font-family: "Crossten Bold";
}
@keyframes pulse {
	0% {
		transform: scale(1);
		box-shadow: 0 0 0 0 $error-color;
	}

	70% {
		transform: scale(1);
		box-shadow: 0 0 0 2px $error-color;
	}

	100% {
		transform: scale(1);
		box-shadow: 0 0 0 0 $error-color;
	}
}
</style>
