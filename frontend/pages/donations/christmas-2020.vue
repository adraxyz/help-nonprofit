<template>

  <div v-if="page_content.name === 'donations--christmas-2020'">
    <Section_0 :data="section_data(0)"/>
    <Section_1 :data="section_data(1)"/>
    <Section_2 :data="section_data(2)"/>
  </div>

</template>

<script>
  import Section_0 from "../../components/sections/donations/christmas/Section_0";
  import Section_1 from "@/components/sections/donations/christmas/Section_1";
  import Section_2 from "@/components/sections/donations/christmas/Section_2";
  import { mapState } from 'vuex';
  export default {
    name: 'Christmas-2020',
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
      ...mapState(['page_content'])
    },
    methods: {
      section_data(index) {
        return this.page_content.sections.find(s => s.order === index)
      }
    },
    async fetch({ store }) {
      await store.dispatch('loadPageContent', {page: 'donations--christmas-2020'})
      store.dispatch('setLogo', {content_type: false})
    }
  }
</script>
