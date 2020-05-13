<template>
  <section id="donations-section-2" class="padding-level-2">

    <div class="section-title-center text-center">
      <span class="section-title">{{ data.title }}</span>
    </div>

    <v-row no-gutters class="donation-section-row">

      <v-col cols="12" md="4"
             class="donation-section-col">
        <DonateCard
          :intro="'1'"
          :title="card(0).texts.title"
          :subtitle="card(0).texts.subtitle"
          :content="card(0).texts.content"
          :button="card(0).button"
          :paypal="true"/>
      </v-col>

      <v-col cols="12" md="8"
             class="donation-section-col">
        <DonateCard
          :intro="'2'"
          :title="card(1).texts.title"
          :subtitle="card(1).texts.subtitle"
          :content="card(1).texts.content"
          :button="card(1).button"/>
      </v-col>

      <v-col cols="12" class="donation-section-col">
        <v-row no-gutters class="donation-section-nested-row">
          <v-col cols="12" md="8" class="donation-image-col">
            <v-img :src="backg_img" contain class="section-image"/>
          </v-col>
          <v-col cols="12" md="4">
            <v-row no-gutters class="donation-section-nested-row">
              <v-col cols="12">
                <DonateCard
                  :intro="'3'"
                  :title="card(2).texts.title"
                  :subtitle="card(2).texts.subtitle"
                  :content="card(2).texts.content"
                  :button="card(2).button"/>
              </v-col>
              <v-col cols="12" class="donation-section-nested-col">
                <DonateCard
                  :intro="'4'"
                  :title="card(3).texts.title"
                  :subtitle="card(3).texts.subtitle"
                  :content="card(3).texts.content"
                  :button="card(3).button"/>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="12" md="4"
             class="donation-section-col">
        <DonateCard
          :intro="'5'"
          :title="card(4).texts.title"
          :subtitle="card(4).texts.subtitle"
          :content="card(4).texts.content"
          :button="card(4).button"/>
      </v-col>
      <v-col cols="12" md="4"
             class="donation-section-col">
        <DonateCard
          :intro="'6'"
          :title="card(5).texts.title"
          :subtitle="card(5).texts.subtitle"
          :content="card(5).texts.content"
          :button="card(5).button"/>
      </v-col>
      <v-col cols="12" md="4"
             class="donation-section-col">
        <DonateCard
          :intro="'7'"
          :title="card(6).texts.title"
          :subtitle="card(6).texts.subtitle"
          :content="card(6).texts.content"
          :button="card(6).button"/>
      </v-col>
    </v-row>
  </section>
</template>

<script>
  import DonateCard from "../../DonateCard";
  export default {
    name: "Section_2",
    props: {
      data: Object
    },
    components: {
      DonateCard
    },
    computed: {
      backg_img() {
        let img = this.data.images.find(i => i.order === 0)
        if (img) {
          return img.content
        }
        return ''
      }
    },
    methods: {
      card(index) {
        return {
          texts: this.data.texts.find(t => t.order === index),
          button: this.data.buttons.find(t => t.order === index)
        }
      }
    }
  }
</script>

<style lang="scss">
  #donations-section-2 {
    .donation-section-row {
      margin-bottom: 5vh;
      background-size: 150% !important;
      padding-left: 5%;
      padding-right: 5%;
    }
    .donation-section-nested-row {
      height: 100%;
      padding-left: 30px;
    }
    .donation-section-col {
      padding: 30px;
      z-index: 1;
      line-height: 100%;
    }
    .donation-section-nested-col {
      padding-top: 60px;
    }
    .iban-first-col {
      width: 60%;
    }
    .iban-second-col {
      width: 40%;
      text-align: right;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #donations-section-2 {
      .donation-section-row {
        /*padding-left: 0px;*/
        /*padding-right: 0px;*/
      }
      .donation-section-col {
        padding-left: 20px;
        padding-right: 20px;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #donations-section-2 {
      .donation-section-nested-row {
        padding-left: 0px;
      }
      .donation-section-col {
        padding-left: 0px;
        padding-right: 0px;
      }
      .donation-image-col {
        padding-bottom: 60px;
      }
      .iban-first-col {
        padding-right: 3px;
        width: 50%;
      }
      .iban-second-col {
        padding-left: 3px;
        width: 50%;
      }
      .section-image {
        max-height: 70vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #donations-section-2 {
      .donation-section-row {
        padding-left: 0px;
        padding-right: 0px;
      }
    }
  }
</style>
