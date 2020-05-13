<template>
  <div v-if="page_content.name === 'projects--' + this.$route.params.slug">
    <Section_0 :data="section_data_0" :project="project"/>
    <Section_1 :data="section_data_1" :project="project"/>
    <Section_2 :data="section_data_2" :project="project"/>
    <Section_3 :data="section_data_3" :project="project"/>
    <Section_4 :data="section_data_4" :project="project"/>
    <Section_5 :data="section_data_5"/>
  </div>
</template>

<script>
  import Section_0 from "../../../components/sections/projects/_slug/Section_0";
  import Section_1 from "../../../components/sections/projects/_slug/Section_1";
  import Section_2 from "../../../components/sections/projects/_slug/Section_2";
  import Section_3 from "../../../components/sections/projects/_slug/Section_3";
  import Section_4 from "../../../components/sections/projects/_slug/Section_4";
  import Section_5 from "../../../components/sections/projects/_slug/Section_5";
  import { mapState } from 'vuex';
  export default {
    name: "project_details_page",
    head() {
      return {
        title: '| ' + this.project.title
      }
    },
    components: {
      Section_0,
      Section_1,
      Section_2,
      Section_3,
      Section_4,
      Section_5
    },
    computed: {
      ...mapState(['page_content', 'project']),
      section_data_0() {
        return this.page_content.sections.find(s => s.order === 0)
      },
      section_data_1() {
        return this.page_content.sections.find(s => s.order === 1)
      },
      section_data_2() {
        return this.page_content.sections.find(s => s.order === 2)
      },
      section_data_3() {
        return this.page_content.sections.find(s => s.order === 3)
      },
      section_data_4() {
        return this.page_content.sections.find(s => s.order === 4)
      },
      section_data_5() {
        return this.page_content.sections.find(s => s.order === 5)
      }
    },
    // methods: {
    //   section_data(index) {
    //     return this.page_content.sections.find(s => s.order === index)
    //   }
    // },
    async fetch({ store, params }) {
      await store.dispatch('loadPageContent', {page: 'projects--' + params.slug})
      await store.dispatch('loadProject', {slug: params.slug})
      store.dispatch('setLogo', {content_type: false})
    }
  }
</script>
