<template>
  <section id="donations-section-0" class="padding-level-3" v-resize="onResize">

    <div class="section-text text-center">
      <h2 class="text-title" v-html="sectionText.title"/>
      <br>
      <h1 class="title-number">
        {{ variableContent }}
      </h1>
    </div>

  </section>
</template>

<script>
  export default {
    name: "Section_0",
    props: {
      data: Object
    },
    data: () => ({
      content_index: 0
    }),
    head() {
      return {
        meta: this.data.meta_tags
      }
    },
    computed: {
      contents() {
        return this.data.texts[0].content.split(',')
      },
      sectionText() {
        return this.data.texts[0]
      },
      variableContent() {
        if (this.content_index === this.contents.length) {
          this.content_index = 0
        }
        return this.contents[this.content_index]
      }
    },
    methods: {
      setIndex() {
        setInterval(
          () => {
            this.content_index += 1
          },
          2000
        )
      },
      onResize() {
        document.documentElement.style.setProperty('--100vh', `${window.innerHeight}px`);
      }
    },
    mounted() {
      this.setIndex()
    }
  }
</script>

<style lang="scss">
  /* TRANSITIONS */
  .fade-enter-active, .fade-leave-active {
    transition: opacity 1s;
  }
  .fade-enter, .fade-leave {
    opacity: 0.1;
  }
  /* BASE STYLE */
  #donations-section-0 {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    margin-top: $logo-size + $logo-margin;
    .title-number {
      color: $secondary-color;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #donations-section-0 {
      margin-top: $md-logo-size + $md-logo-margin;
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #donations-section-0 {
      .title-number {
        font-size: $font-size-40;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #donations-section-0 {
      .title-number {
        font-size: $font-size-30;
        line-height: 120%;
        margin-top: 1vh;
      }
    }
  }
</style>
