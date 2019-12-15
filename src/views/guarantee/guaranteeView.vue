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
        <GroupImg :groupList="groupList"></GroupImg>
      </div>
      <div class="info">
        <span>备注</span>
        <span>{{result.description || '无'}}</span>

      </div>

      <div class="info">
        <span>反担保</span>
        <van-row class="cguarantee" v-for="(item, index) in cguarantee" :key="index">
          <van-col span="12" class="box right-border">
            <img v-if="item.pimg.length>0" @click="showimg(myLocalHost+item.pimg)" :src="myLocalHost+item.pimg"
                 alt="">
            <img v-else src="../../assets/index/no_pic.jpg" alt="">
            <span class="text-center">房产证</span>
            <span>产权比例：{{item.proportion}}</span>
            <span>房屋面积(平米)：{{item.area}}</span>
            <span>房产价值：{{item.value}}</span>
          </van-col>
          <van-col span="12" class="box">
            <img v-if="item.idimg.length>0" @click="showimg(myLocalHost+item.idimg)" :src="myLocalHost+item.idimg"
                 alt="">
            <img v-else src="../../assets/index/no_pic.jpg" alt="">
            <span class="text-center">身份证</span>
            <span>反担保人姓名：{{item.name}}</span>
            <span>反担保人电话：{{item.phone}}</span>
            <span>反担保人住址：{{item.address}}</span>
          </van-col>
        </van-row>
      </div>

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
  import guaranteeItem from '@/components/guarantee/guarateeItem';
  import {queryGuarantee} from '@/api/api';
  import GroupImg from '@/components/GroupImg/GroupImg'

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
        groupList: [],
        cguarantee: []
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
          this.groupList = res.pic_groups;
          this.cguarantee = res.cguarantee;
        });
      },
      showimg(img) {
        this.images = [img]
        this.show = true
      }

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
</style>
