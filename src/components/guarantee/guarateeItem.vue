<template>
  <div class="gualistitem">
    <div v-for="item in results"
         @click="toView(item.id)"
         style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem  .5rem">
      <van-row class="tit">
        <van-col span="12" class="van-ellipsis">保函编号：{{item.number}}</van-col>
        <van-col span="12" style="text-align: right">
          <van-tag color="#8eaccc">{{guarantype(item.category)}}</van-tag>
          <van-tag color="#8ec5cc" v-if="item.is_expiretime ==1">已过期</van-tag>
          <van-tag color="#d9aa60" v-else>未过期</van-tag>
        </van-col>
      </van-row>
      <van-row class="project">
        项目：{{item.projectid}}
      </van-row>
      <van-row type="flex" align="center">
        <van-col span="16">
          <div>项目区域：{{item.pname}}-{{item.cname}}-{{item.dname}}</div>
          <div>公司名称：{{item.companyid}}</div>
          <div>收益人名称：{{item.bene}}</div>
          <div>保函期限：{{item.signtime}} 至 {{item.expiretime}}</div>
        </van-col>
        <van-col span="8" align="center"  class="left-border">
          <div style="color: #d9aa60;font-weight: bold;">¥ {{item.amount}}</div>
          <div>担保金额(万元)</div>
        </van-col>
      </van-row>
    </div>
  </div>
</template>

<script>
  import {guarantype, companyBad} from '@/utils/type'

  export default {
    name: 'CompnayListItem',
    data() {
      return {
        guarantype,
        companyBad,
        results: [],
      }
    },
    props: ['result', 'isReload'],
    methods: {
      toView(id) {
        this.$router.push({
          path: '/GuaView',
          query: {
            id
          },
        });
      }
    },
    watch: {                        //监听value的变化，进行相应的操作即可
      result: function (a, b) {       //a是value的新值，b是旧值
        if (a != b) {
          this.results = this.results.concat(a);
        }
      },
      isReload: function (a, b) {
        if (a) {
          this.results = []
        }
      }
    }
  }
</script>
<style scoped>
  .gualistitem {
    color: #3c3c3c;
    padding: 0 .5rem;
  }

  .gualistitem .tit .van-col--20 {
    font-size: 1.6rem;
    line-height: 3rem;
    font-weight: bold;
    color: #3c3c3c;
  }

  .companylistitem /deep/ .legal {
    color: #8eaccc;
    font-size: 1.4rem;
  }

  .companylistitem .address {
    font-size: 1.4rem;
    margin-top: .5rem;
  }

  .left-border{
    border-left: 1px solid #ececec;
    padding: 1rem 0;
  }
  .project {
    font-weight: bold;
  }
</style>

