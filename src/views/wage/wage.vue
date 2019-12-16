<template>
  <div class="van-content">
    <!--  tab切换和搜索  -->
    <van-tabs background="transparent"
              color="#fff"
              title-inactive-color="#fff"
              title-active-color="#fff"
              class="searach-tabs"
              @click="changeTabs"
    >
      <van-tab title="项 目" name="Project"></van-tab>
      <van-tab title="企 业" name="Company"></van-tab>
      <van-tab title="劳 工" name="Labor"></van-tab>
    </van-tabs>
    <Search @searchObj="searchObj"></Search>

  </div>
</template>

<script>
  import Search from '@/components/areas/Search';

  export default {
    name: "wage",
    data() {
      return {
        searchType: 'Project',
      }
    },
    methods: {
      changeTabs(name, title) {
        this.searchType = name;
      },

      searchObj(params) {
        this.$router.push({
          name: this.searchType,
          params,
        });
      },
    },
    mounted() {

    },
    created() {

    }
  }
</script>

<style scoped>

</style>
