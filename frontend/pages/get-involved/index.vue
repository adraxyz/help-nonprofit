<template>
  <div v-if="page_content.name === 'get-involved'">
    <Section_0 :data="section_data_0"/>
    <Section_1 :data="section_data_1"/>
    <Section_2 :data="section_data_2"/>
  </div>
</template>

<script>
  import Section_0 from "../../components/sections/get-involved/Section_0";
  import Section_1 from "../../components/sections/get-involved/Section_1";
  import Section_2 from "../../components/sections/get-involved/Section_2";
  import { mapState } from 'vuex';
  export default {
    name: 'get_involved_page',
    components: {
      Section_0,
      Section_1,
      Section_2
    },
    head() {
      return {
        title: '| ' + this.page_content.title
      }
    },
    computed: {
      ...mapState(['page_content']),
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
      // section_data(index) {
      //   return this.page_content.sections.find(s => s.order === index)
      // }
    // },
    async fetch({ store }) {
      await store.dispatch('loadPageContent', {page: 'get-involved'})
      store.dispatch('setLogo', {content_type: false})
    }
  }
</script>
