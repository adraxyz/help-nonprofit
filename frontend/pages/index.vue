<template>
  <div v-if="page_content.name === 'home'">
<!--    <div class="page-content-container error" v-if="page_content.name === 'home'">-->
<!--    <Section_0 :data="section_data(0)"/>-->
<!--    <Section_1 :data="section_data(1)"/>-->
<!--    <Section_2 :data="section_data(2)"/>-->
<!--    <Section_3 :data="section_data(3)"/>-->
<!--    <Section_4 :data="section_data(4)"/>-->
    <Section_0 :data="section_data_0"/>
    <Section_1 :data="section_data_1"/>
    <Section_2 :data="section_data_2"/>
    <Section_3 :data="section_data_3"/>
    <Section_4 :data="section_data_4"/>
  </div>
</template>

<script>
  import Section_0 from "../components/sections/home/Section_0";
  import Section_1 from "../components/sections/home/Section_1";
  import Section_2 from "../components/sections/home/Section_2";
  import Section_3 from "../components/sections/home/Section_3";
  import Section_4 from "../components/sections/home/Section_4";
  import { mapState } from 'vuex';
  export default {
    name: 'home_page',
    components: {
      Section_0,
      Section_1,
      Section_2,
      Section_3,
      Section_4
    },
    head() {
      return {
        title: ''
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
      }
    },
    // methods: {
      // section_data(index) {
      //   return this.page_content.sections.find(s => s.order === index)
      // }
    // },
    async fetch({ store }) {
      await store.dispatch('loadPageContent', {page: 'home'})
      store.dispatch('setLogo', {content_type: 'alt'})
    }
  }
</script>
