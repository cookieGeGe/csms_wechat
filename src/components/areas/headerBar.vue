<template>
  <div>
    <van-row class="header-bar" type="flex" align="left">
      <span @click="goHistory()" style="color: #8eaccc !important;display: flex;">
        <van-icon name="arrow-left" color="#8eaccc" size="2rem"/>{{fatherName}}
      </span>
      <span>{{currentNmae}}</span>
    </van-row>
  </div>
</template>

<script>
  export default {
    name: "headerBar",
    data() {
      return {}
    },
    props: ['fatherName', 'currentNmae'],
    methods: {
      goHistory() {
        window.history.go(-1)
      }
    }
  }
</script>

<style scoped>
  .header-bar {
    font-size: 1.5rem !important;
  }
  .header-bar span {
    padding-right: 1rem;
    text-align: center;
    color: #3c3c3c;
  }

  .header-bar > span:last-child {
    border-left: 2px solid #3c3c3c;
    padding-left: 1rem;
  }

</style>
