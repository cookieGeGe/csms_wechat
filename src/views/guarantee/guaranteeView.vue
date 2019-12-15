<template>
  <div class="van-content">
    <div class="card">
      <guaranteeItem :isReload="isReload" :result="this.result"></guaranteeItem>
    </div>
    <div class="card">
      <div class="info">
        <span>所在地详情</span>
        <span>{{result.address || '无'}}</span>
      </div>
      <div class="info">
        <span>担保公司信息</span>
        <span>担保公司：{{result.guacompany}}</span>
        <span>注册资本(万元)：{{result.capital}}</span>
        <span>企业性质：{{result.nature}}</span>
      </div>
      <div class="info">
        <span>费用信息</span>
        <span>实际收费(万元)：{{result.realac}}</span>
        <span>保证金比例：{{result.marginratio || 0}}%</span>
        <span>保证金：{{result.margin}}%</span>
        <span>总费率：{{result.totalrate || 0}}%</span>
        <span>总收费金额(万元)：{{result.total}}</span>
      </div>
      <div class="info">
        <span>备注</span>
        <!--<span>{{result.description || '无'}}</span>-->
        <GroupImg :groupList="groupList"></GroupImg>
      </div>
      <div class="info">
        <span>保函照片</span>
        <span></span>
      </div>

    </div>
    <div class="card">
      <div>反担保</div>
      <div></div>
    </div>
  </div>
</template>

<script>
  import guaranteeItem from '@/components/guarantee/guarateeItem';
  import {queryGuarantee} from '@/api/api';
  import GroupImg  from '@/components/GroupImg/GroupImg'

  export default {
    name: "guaranteeView",
    data() {
      return {
        searchType: {
          id: -1,
        },
        isReload: true,
        result: [],

      }
    },
    components: {
      guaranteeItem,
      GroupImg
    },
    methods: {
      reload() {
        queryGuarantee(this.searchType).then(res => {
          var ret = res.guarantee;
          console.log(res);
          this.isReload = false; //是否重新赋值
          this.result = ret;
        });
      },

    },
    mounted() {
      this.searchType.id = this.$route.params.id;
      this.reload()
    }
  }
</script>

<style scoped>
  .card {
    padding: 0.5rem 0.5rem;
    font-size: 1.2rem !important;
  }

  .info span {
    display: block;
    font-size: 1.2rem;
    line-height: 2.5rem;
  }

  .info span:first-child {
    font-size: 1.3rem;
    font-weight: bold;
  }

</style>
