<template>
  <div class="page-content-container" v-if="page_content.name === 'projects'">
    <Section_0 :data="section_data_0" :projects="projects"/>
    <Section_1 :data="section_data_1" :categories="projects_categories"/>
    <Section_2 :data="section_data_2" />
  </div>
</template>

<script>
  import Section_0 from "../../components/sections/projects/Section_0";
  import Section_1 from "../../components/sections/projects/Section_1";
  import Section_2 from "../../components/sections/projects/Section_2";
  import { mapState } from 'vuex';
  export default {
    name: 'projects_page',
    components: {
      Section_0,
      Section_1,
      Section_2
    },
    head() {
      return {
        title: '| ' + this.page_content.title,
        meta: this.page_content.meta_tags
      }
    },
    computed: {
      ...mapState(['page_content', 'projects', 'projects_categories']),
      section_data_0() {
        return this.page_content.sections.find(s => s.order === 0)
      },
      section_data_1() {
        return this.page_content.sections.find(s => s.order === 1)
      },
      section_data_2() {
        return this.page_content.sections.find(s => s.order === 2)
      }
    },
    // methods: {
    //   section_data(index) {
    //     return this.page_content.sections.find(s => s.order === index)
    //   }
    // },
    async fetch({ store }) {
      await store.dispatch('loadPageContent', {page: 'projects'})
      store.dispatch('setLogo', {content_type: false})
      await store.dispatch('loadProjects')
      await store.dispatch('loadProjectsCategories')
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
