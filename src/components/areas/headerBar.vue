<template>
    <van-row class="header-bar" >
      <van-col @click="goHistory()" >
        <span style="vertical-align: middle"><van-icon name="arrow-left" class="back" size="1.6rem"/></span>
        <span>{{fatherName}}</span>
      </van-col>
      <van-col class="line"></van-col>
      <van-col class="header-new">{{currentNmae}}</van-col>
    </van-row>
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
  .header-bar span {
    color: #8eaccc;
  }
  .header-bar .line {
    height:1.1rem;
    width: 2px;
    background: #888;
    margin:.4rem .5rem 0 .5rem;
  }
  .header-bar .header-new{
    color: #888;
  }
</style>
