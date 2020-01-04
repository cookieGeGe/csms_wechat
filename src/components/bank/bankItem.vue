<template>
  <div class="gualistitem">
    <div v-for="item in results"
         @click="toView(item.id)"
         style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem  .5rem">
      <van-row class="tit">
        <van-col span="24" class="van-ellipsis">{{item.bank || '银行未填写'}} {{item.account || '账号未知'}}</van-col>
      </van-row>
      <van-row class="project">
        项目：{{item.name}}
      </van-row>
      <van-row type="flex" align="center">
        <van-col span="16">
          <div>总工期：{{item.totalmonth}}个月 &#12288;开始时间：{{item.starttime}}</div>
          <div>总造价：¥{{item.price}}</div>
          <div>农民工工资比例：{{item.wagepercent}}</div>
          <div>每月发放金额：¥{{(item.price / 100 * item.wagepercent).toFixed(2)}}</div>
        </van-col>
        <van-col span="8" align="center"  class="left-border">
          <div style="color: #d9aa60;font-weight: bold;">¥ {{item.totalpay || 0}}</div>
          <div>实发总额(元)</div>
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
          path: '/bankView',
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

