<template>
  <div class="">
    <headerBar fatherName="银行查询" currentNmae="银行详情"></headerBar>
    <div class="card">
      <bankItem :isReload="isReload" :result="result"></bankItem>
    </div>
    <div class="card">
      <van-row class="progress">
        <van-col span="4" class="t-center">
          <div class="year" v-for="(value,key) in yearData">
            <div class="tit" @click="openers(key,$event)">{{key}}</div>
            <div class="monthCont" style="display: none;">
              <div v-for="(month,monthkey) in value" :class="month.is_current?'act':''"
                   @click="progresser(month.id,month.is_input,$event)">
                <span :class="month.is_input?'circle':''"></span><span>{{monthkey + 1}}月</span>
              </div>
            </div>
          </div>
        </van-col>
        <van-col span="20" class="bankinfo">
          <div class="title">{{month_bank.year}}年 {{month_bank.month}}月 银行账户信息</div>
          <div v-if="month_bank.status==0">支付状态:
            <van-tag color="#8ec5cc">全额到</van-tag>
          </div>
          <div v-else-if="month_bank.status==1">支付状态:
            <van-tag color="#d9aa60">部分到</van-tag>
          </div>
          <div v-else>支付状态:
            <van-tag color="#d96c60">未到账</van-tag>
          </div>
          <div>每月余额: {{month_bank.rpay - month_bank.actualpay||'0'}}</div>
          <div>开卡数：{{month_bank.workers || '0'}}</div>
          <div>当月账户收到金额：{{month_bank.rpay||'0'}}</div>
          <div>总支出金额：{{month_bank.actualpay || '0'}}</div>
          <div class="title">银行回单</div>
          <div>
            <p v-if="month_bank.receipt && month_bank.receipt != ''">已上传银行回单，暂不显示xls，详情请移步PC端</p>
            <p style="color: rgb(217, 108, 96)" v-else>还没有添加回单哟~</p>
<!--            <img v-if="month_bank.receipt && month_bank.receipt != ''" @click="showimg(myLocalHost+month_bank.receipt)"-->
<!--                 :src="myLocalHost+month_bank.receipt"-->
<!--                 alt="">-->
<!--            <img v-else src="../../assets/index/no_pic.jpg" alt="">-->
          </div>
          <div v-if="month_bank.receipt && month_bank.receipt != ''">上传时间 {{month_bank.rectime}}</div>
        </van-col>
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
  import bankItem from '@/components/bank/bankItem';
  import headerBar from '@/components/areas/headerBar';
  import {queryBank, queryBankInfo} from '@/api/api';

  export default {
    name: "guaranteeView",
    data() {
      return {
        show: false,
        images: [],
        searchType: {
          id: -1,
        },
        isReload: true,
        result: [],
        yearData: {},
        month_bank: {},
      }
    },
    components: {
      bankItem,
      headerBar
    },
    methods: {
      reload() {
        queryBank(this.searchType).then((res) => {
          var ret = res.project;
          //console.log(res);
          this.isReload = false; //是否重新赋值
          this.result = [ret,];
          this.yearData = res.allmonth;
          this.month_bank = res.bankinfo;
          //console.log(this.month_bank)
          // if (this.month_bank.receipt == '') {
          //   this.month_bank.rectime = ''
          // }
        });
      },
      showimg(img) {
        this.images = [img];
        this.show = true;
      },
      progresser(id, is_input, event) {
        if (!is_input) return;
        var eAct = document.getElementsByClassName('act')[0];
        eAct.setAttribute("class", "");
        var el = event.currentTarget;
        el.setAttribute("class", "act");
        this.load_month_bank(id)
      },
      openers(key, event) {
        var el = event.currentTarget;
        var monthCont = el.nextElementSibling;
       // console.log(monthCont);
        if (monthCont.style.display == 'none') {
          monthCont.style.display = 'block'
        } else {
          monthCont.style.display = 'none'
        }
      },
      load_month_bank(id) {
        queryBankInfo({id,}).then((res) => {
          this.month_bank = res.bankinfo;
          // if (this.month_bank.receipt == '') {
          //   this.month_bank.rectime = ''
          // }
        })
      }

    },
    mounted() {
      this.searchType.id = this.$route.query.id;
      this.reload();
    }
  }
</script>

<style scoped>
  .card {
    padding: 0.5rem 0.5rem;
    margin-right: 5px;
    margin-left: 5px;
    font-size: 1.1rem !important;
  }

  .bankinfo div {
    display: block;
    font-size: 1.2rem;
    line-height: 2.5rem;
  }

  .bankinfo .title {
    font-size: 1.3rem;
    font-weight: bold;
  }

  .bankinfo img {
    width: 85%;
    max-height: 18rem;
  }

  .imggroup {
    padding: 0rem 0rem !important;
  }

  /deep/ .imggroup .tits {
    font-weight: bold;
  }

  /deep/ .imggroup .van-dropdown-menu__item {
    padding-right: 0.5rem;
  }

  .cguarantee {
    margin: 1rem 0;
    /*border-bottom: 1px solid #ececec;*/
    background: #fff;
    padding: 1rem 0;
  }

  .cguarantee div {
    display: inline-block;
  }

  .cguarantee span {
    font-size: 1.1rem;
  }

  .text-center {
    text-align: center;
  }

  .box {
    padding: 0 1rem;
  }

  .box img {
    width: 100%;
    height: 15rem;
  }

  .right-border {
    border-right: 0.8px solid #ececec;
  }

  .t-center {
    font-weight: bold;
    font-size: 1.2rem;
    padding: .5rem;
  }

  .monthCont {

  }

  .monthCont div {
    margin: .5rem 0;
    color: #888888;
  }

  .monthCont .circle + span {
    color: #3c3c3c;
  }

  .circle {
    display: inline-block;
    height: .6rem;
    width: .6rem;
    vertical-align: middle;
    background: #8ec5cc;
    border-radius: 50%;
    margin-right: .5rem;
  }

  .act {
    background: #8eaccc;
  }
</style>
