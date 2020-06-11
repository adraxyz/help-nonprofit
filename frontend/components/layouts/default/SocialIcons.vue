<template>
  <div id="social-icons-container" :class="[{
      'vertical-align-icons': vertical,
      'horizontal-align-icons': !vertical
    }]">

    <v-btn v-for="social in socials" :key="social.order"
      :class="[{'social-btn white': true,'icon-shadow': shadow}, icon_custom_class]"
      target="_blank"
      :href="social.link">
      <i :id="`${social.platform}-icon`" class="social-icon"/>
    </v-btn>

  </div>
</template>

<script>
  import { mapState } from 'vuex';
  export default {
    name: "SocialIcons",
    props: {
      vertical: Boolean,
      shadow: Boolean,
      icon_custom_class: String
    },
    async fetch() {
      await this.$store.dispatch('loadSocials')
    },
    computed: {
      ...mapState(['socials'])
    }
  }
</script>

<style lang="scss">
  #social-icons-container {
    position: relative;
    /*z-index: 1 !important; TODO z-index */
    align-self: end;
    margin-right: $big-button-height/2 - $circle-icon-size/2;
    height: 145px;
    flex-direction: column;
    justify-content: space-between;
    .white {
      border: 2px solid black !important;
      background-color: white !important;
    }
    .icon-shadow {
      box-shadow: -$box-shadow-side $box-shadow-bottom #E99F33 !important;
    }
  }
  .vertical-align-icons {
    display: flex;
  }
  .horizontal-align-icons {
    height: unset !important;
  }
  .social-btn {
    min-width: unset !important;
    width: $circle-icon-size !important;
    height: $circle-icon-size !important;
    border-radius: 50% !important;
  }
  .social-icon {
    border-radius: 50%;
    height: $circle-icon-size * 0.7;
    width: $circle-icon-size * 0.7;
    background-size: 60% !important;
  }
  #facebook-icon {
    /*height: $circle-icon-size * 0.5;
    width: $circle-icon-size * 0.5;
    background-size: 50% !important;*/
    background: white url('~assets/icons/facebook-icon.png') center center no-repeat;
  }
  #instagram-icon {
    /*height: $circle-icon-size * 0.5;
    width: $circle-icon-size * 0.5;
    background-size: 50% !important;*/
    background: white url('~assets/icons/instagram-icon.png') center center no-repeat;
  }
  #linkedin-icon {
    /*height: $circle-icon-size * 0.5;
    width: $circle-icon-size * 0.5;
    background-size: 50% !important;*/
    background: white url('~assets/icons/linkedin-icon.png') center center no-repeat;
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #social-icons-container {
      margin-right: 0px;
    }
  }
</style>
