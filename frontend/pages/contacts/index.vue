<template>
  <div class="page-content-container" v-if="page_content.name === 'contacts'">
    <Section_0 :data="section_data(0)"/>
  </div>
</template>

<script>
  import Section_0 from "../../components/sections/contacts/Section_0";
  import { mapState } from 'vuex';
  export default {
    name: 'contacts_page',
    components: {
      Section_0
    },
    head() {
      return {
        title: '| ' + this.page_content.title,
        meta: this.page_content.meta_tags
      }
    },
    computed: {
      ...mapState(['page_content', 'default_layout', 'contact_form_messages'])
    },
    methods: {
      section_data(index) {
        return this.page_content.sections.find(s => s.order === index)
      }
    },
    async fetch({ store }) {
      await store.dispatch('loadPageContent', {page: 'contacts'})
      await store.dispatch('loadContactFormMessages')
      store.dispatch('setLogo', {content_type: false})
    }
  }
</script>

<style lang="scss">
  .page-content-container {
    max-width: $max-width;
    .section-button {
      white-space: normal;
    }
  }
</style>
