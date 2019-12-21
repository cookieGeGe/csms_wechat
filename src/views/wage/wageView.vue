<template>
  <div class="van-content">
    <Calendar ref="Calendar" v-on:choseDay="clickDay"
              v-on:changeMonth="changeDate"></Calendar>
    <div class="card">
      <salaryItem :isReload="isReload" :result="result" :total="total"></salaryItem>
    </div>
    <div class="card info">
      <van-row>
        <van-col span="12">合同类型</van-col>
        <van-col span="12" class="float-right">
          <van-tag color="#8eaccc">{{formatter_type(info.isfeestand)}}</van-tag>
        </van-col>
        <van-col span="12" class="show-inline">
          <div class="float-left">计酬方式</div>
          <div class="float-right">
            <van-tag color="#8eaccc">{{info.type||''}}</van-tag>
          </div>
        </van-col>
        <van-col span="12" class="show-inline">
          <div class="float-left">计酬（日薪）</div>
          <div class="float-right">¥ {{info.unit||'0'}}</div>
        </van-col>
        <van-col span="12" class="show-inline">
          <div class="float-left">考勤天数</div>
          <div class="float-right">{{info.swipe||'0'}}</div>
        </van-col>
        <van-col span="12" class="show-inline">
          <div class="float-left">手工合计</div>
          <div class="float-right">{{info.manual||'0'}}</div>
        </van-col>
        <van-col span="12">基本工资</van-col>
        <van-col span="12" class="float-right">¥ {{info.basicwage||'0'}}</van-col>
        <van-col span="12">加班工资</van-col>
        <van-col span="12" class="float-right">¥ {{info.overtime||'0'}}</van-col>
        <van-col span="12">小计</van-col>
        <van-col span="12" class="float-right yellow-c">¥ {{info.subtotal||'0'}}</van-col>
        <van-col span="12">奖金</van-col>
        <van-col span="12" class="float-right">¥ {{info.raward||'0'}}</van-col>
        <van-col span="12">扣款</van-col>
        <van-col span="12" class="float-right">¥ {{info.deduction||'0'}}</van-col>
        <van-col span="12">实发工资</van-col>
        <van-col span="12" class="float-right weight-font yellow-c">¥ {{info.total||'0'}}</van-col>
      </van-row>
    </div>
    <van-image-preview
      v-model="show"
      :images="images"
    >
      <!--<template v-slot:index>第{{ index }}页</template>-->
    </van-image-preview>

  </div>
</template>

<script>
  import salaryItem from '@/components/wage/wageItem';
  import Calendar from 'vue-calendar-component';
  import {querySalary, querySalaryNext} from '@/api/api';

  export default {
    name: "guaranteeView",
    data() {
      return {
        show: false,
        images: [],
        searchType: {
          id: -1,
        },
        total:'',
        isReload: true,
        result: [],
        info: {},
      }
    },
    components: {
      salaryItem,
      Calendar
    },
    methods: {
      clickDay(data) {
        console.log(data); //选中某天
      },
      changeDate(data) {
        // console.log(data); //左右点击切换月份
        if (JSON.stringify(this.info) != '{}') {
          var params = {
            id: this.info.laborid,
            month: data.replace(/\//g, '-')
          }
          querySalaryNext(params).then((res) => {
            var ret = res.data;
            if (ret.length==0){
              this.$toast('没有找到工资信息！');
              this.total = 0
              this.info.unit = 0
              this.info.swipe = 0
              this.info.manual = 0
              this.info.basicwage = 0
              this.info.overtime = 0
              this.info.subtotal = 0
              this.info.raward = 0
              this.info.deduction = 0
              this.info.total = 0
            } else {
              console.log(res);
              this.total = ret[0].total;
              this.info = ret[0];
            }

          })
        }

      },
      formatter_type(type) {
        if (parseInt(type) == 1) {
          return '合同工'
        }
        return '临时工'
      },
      reload() {
        querySalary(this.searchType).then((res) => {
          var ret = res.data;
          console.log(res);
          this.isReload = false; //是否重新赋值
          this.result = ret;
          this.info = ret[0];
          this.$refs.Calendar.ChoseMonth(this.info.year + '-' + this.info.month + '-1');
          // if (this.month_bank.receipt == '') {
          //   this.month_bank.rectime = ''
          // }
        });
      },
      showimg(img) {
        this.images = [img];
        this.show = true;
      },

    },
    mounted() {
      this.searchType.id = this.$route.query.id;
      this.reload();
    }
  }
</script>

<style scoped>
  /deep/ .wh_content {
    display: none !important;
  }

  /deep/ .wh_content_all {
    background-color: rgba(255, 255, 255, 0) !important;
  }

  .card {
    padding: 0.5rem 0.5rem;
    font-size: 1.1rem !important;
  }

  .show-inline {
    display: inline-block;
  }

  /deep/ .info .van-col {
    padding: 1rem;
    line-height: 2rem;
    font-size: 1.3rem;

  }

  .float-left {
    display: inline-block;
    float: left;
    text-align: left;
  }

  .float-right {
    display: inline-block;
    float: right;
    text-align: right;
  }

  .weight-font {
    font-size: 1.8rem !important;
  }
</style>
