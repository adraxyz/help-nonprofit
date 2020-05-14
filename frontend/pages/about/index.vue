<template>
  <div v-if="page_content.name === 'about'">
    <Section_0 :data="section_data_0"/>
    <Section_1 :data="section_data_1"/>
    <Section_2 :data="section_data_2"/>
    <Section_3 :data="section_data_3"/>
    <Section_4 :data="section_data_4"/>
    <Section_5 :data="section_data_5"/>
  </div>
</template>

<script>
  import Section_0 from "../../components/sections/about/Section_0";
  import Section_1 from "../../components/sections/about/Section_1";
  import Section_2 from "../../components/sections/about/Section_2";
  import Section_3 from "../../components/sections/about/Section_3";
  import Section_4 from "../../components/sections/about/Section_4";
  import Section_5 from "../../components/sections/about/Section_5";
  import { mapState } from 'vuex';
  export default {
    name: 'about_page',
    components: {
      Section_0,
      Section_1,
      Section_2,
      Section_3,
      Section_4,
      Section_5
    },
    head() {
      return {
        title: '| ' + this.page_content.title,
        meta: this.page_content.meta_tags
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
    async fetch({ store }) {
      await store.dispatch('loadPageContent', {page: 'about'})
      store.dispatch('setLogo', {content_type: false})
    }
  }
</script>
