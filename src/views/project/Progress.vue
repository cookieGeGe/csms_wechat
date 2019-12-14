<template>
  <div class="progress">
    是否异常：否 日期：2019-09-12
    进度（%）：
    25%
    工程巡查情况：据项目相关负责人说明，由于7月工资表到近日才交齐，因此7月工资将于9月5日左右发放，同时8月工资将于15日左右进行发放。
    监管类型：正常员工是否有签订合同：无
    此项目是否进行实名制管理：无是否有考勤记录：无
    农民工工资公示牌：无劳务专员任命书：无
    项目经理任命书：无农民工工资支付凭证：有
    月度工资发放情况表
    用工人数：0	支付款项：0
    应发人数：0	欠款：0
    实际发放数：0	差值：0
    打卡数：0	总工资：0
    询问人员
    照片	姓名	电话	所在班组	到场时间	工资领取情况
    <van-row>
      <van-col  span="3">
        <div class="year" v-for="(value,key) in yearData">
          <div class="tit">{{key}}</div>
          <div class="monthCont">
            <div class="month"  v-for="(month,monthkey) in value">
              <span></span>{{monthkey+1}}
            </div>
          </div>
        </div>
      </van-col>
    </van-row>

  </div>
</template>

<script>
  //import {projectTypeArr, projectBadArr}  from '@/utils/type'
  import {queryProgress}  from '@/api/api'

  export default {
    name: 'Progress',
    data () {
      return {
        progressData:{},
        yearData:'',
      }
    },
    props: ['progress', 'yearlist'],
    components: {

    },
    methods: {

    },
    mounted(){
      this.yearData = this.yearlist;
      this.progressData = this.progress;
    },
  }
</script>


<style scoped>
  .company .dropdown {
    border-radius: 50rem;
    height: 2rem;
  }

  /deep/
  .van-dropdown-menu__title {
    font-size: 1rem;
  }

  .company /deep/ .van-dropdown-item__option {
    line-height: 1rem;
    font-size: 1rem;
  }
</style>
