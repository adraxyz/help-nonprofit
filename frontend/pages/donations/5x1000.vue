<template>
  <div v-if="page_content.name === 'donations--5x1000'">
    <Section_0 :data="section_data(0)"/>
    <Section_1 :data="section_data(1)"/>
    <Section_2 :data="section_data(2)"/>
    <Section_3 :data="section_data(3)"/>
    <Section_4 :data="section_data(4)"/>
    <Section_5 :data="section_data(5)"/>
  </div>
</template>

<script>
  import Section_0 from "../../components/sections/donations/5x1000/Section_0";
  import Section_1 from "../../components/sections/donations/5x1000/Section_1";
  import Section_2 from "../../components/sections/donations/5x1000/Section_2";
  import Section_3 from "../../components/sections/donations/5x1000/Section_3";
  import Section_4 from "../../components/sections/donations/5x1000/Section_4";
  import Section_5 from "../../components/sections/donations/5x1000/Section_5";
  import { mapState } from 'vuex';
  export default {
    name: 'CinquePerMille',
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
      ...mapState(['page_content'])
    },
    methods: {
      section_data(index) {
        return this.page_content.sections.find(s => s.order === index)
      }
    },
    async fetch({ store }) {
      await store.dispatch('loadPageContent', {page: 'donations--5x1000'})
      store.dispatch('setLogo', {content_type: false})
    }
  }
</script>
