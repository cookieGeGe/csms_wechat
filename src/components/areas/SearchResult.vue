<template>
    <van-row class="searchreuslt" type="flex" align="center" >
      <van-col span="8" style="">
        <div class="tit">当前搜索结果</div>
      </van-col>
      <van-col span="4" style="border-right: 1px solid #ececee;border-left: 1px solid #ececee">
        <div>总数</div>
        <div class="num">{{totals.total}}</div>
      </van-col>
      <van-col span="7"  style="text-align: left;padding-left: 1rem">
        <div>正常 <span class="num" style="color:#8ec5cc">{{totals.normal}}</span></div>
        <div>风险 <span class="num" style="color:#d9aa60">{{totals.abnormal}}</span></div>
      </van-col>
      <van-col span="4" offset="1">
        <van-circle
          v-model="totals.currentrate"
          :rate="totals.currentrate"
          :speed="100"
          :text="text"
          color="#d9aa60"
          layer-color="#8ec5cc"
          :stroke-width="80"
          size="5rem"
        />
      </van-col>
    </van-row>
</template>

<script>
  import AreaList from '@/components/areas/myarea';
  import {queryProject,queryCompany,queryLabor}  from '@/api/api'

  export default {
    name: 'SearchResult',
    data () {
      return {
      }
    },
    props: ['totals',],
    methods: {

    },
    watch: {                        //监听value的变化，进行相应的操作即可
      totals: function (a, b) {       //a是value的新值，b是旧值
        if (a != b) {
          this.totals = a;
        }
      }
    },
    computed: {
      text() {
        return this.totals.currentrate + '%'
      }
    },
  }
</script>
<style scoped>
  .searchreuslt{
     text-align: center;
     background: white;
     color: #888888;
     margin: 10px;
    padding: 1rem;
    border-radius: 5px;
   }
  .searchreuslt .tit{
   font-size: 1.4rem;
    color: #3c3c3c;
    font-weight: bold;
  }
  .searchreuslt .num{
    font-size: 2rem;
    color: #3c3c3c;
  }
</style>

