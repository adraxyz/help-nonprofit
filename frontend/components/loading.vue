<template>
  <div class="loading-page" v-if="loading">
    <v-progress-circular
      :size="80"
      :width="7"
      indeterminate
    ></v-progress-circular>
  </div>
</template>

<script>
export default {
  data: () => ({
    loading: false
  }),
  methods: {
    start () {
      this.loading = true
    },
    finish () {
      this.loading = false
    }
  }
}
</script>

<style lang="scss">
.loading-page {
  position: fixed;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  z-index: 300;
  .v-progress-circular {
    color: $error-color !important;
    align-self: center;
  }
}
</style>
