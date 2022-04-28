<template>
  <div style="margin-left: 40px">
    <h2>这里为索引</h2>
  </div>
</template>

<script>
export default {
  name: "queue",
  beforeCreate() {
    this.$store.commit("getindex",1)
  },
}
</script>

<style scoped>

</style>