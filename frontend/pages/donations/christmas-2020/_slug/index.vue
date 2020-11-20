<template>
  <div class="text-right">
    <Section_0 :data="section_data(0)" :product="product"/>
  </div>
</template>

<script>
  import { mapState } from 'vuex';
  import Section_0 from "@/components/sections/donations/christmas/_slug/Section_0";

  export default {
    name: "product_details_page",
    head() {
      return {
        title: '| ' + this.product.title,
        meta: this.page_content.meta_tags
      }
    },
    components: {
      Section_0
    },
    computed: {
      ...mapState(['page_content', 'product'])
    },
    methods: {
      section_data(index) {
        return this.page_content.sections.find(s => s.order === index)
      }
    },
    async fetch({ store, params }) {
      let locale_slug = store.state.product["slug_" + store.state.locale]
      if (!locale_slug) {
        locale_slug = params.slug
      }
      await store.dispatch('loadPageContent', {page: 'christmas-2020--' + locale_slug})
      await store.dispatch('loadProduct', {slug: locale_slug})
      store.dispatch('setLogo', {content_type: false})
    }
  }
</script>
