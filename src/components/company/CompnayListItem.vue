<template>
  <div class="companylistitem">
    <div v-for="item in results"
         @click="toView(item.id)"
         style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem  .5rem" >
      <van-row class="tit"  >
        <van-col span="20" class="van-ellipsis">{{item.name}}</van-col>
        <van-col span="4" style="text-align: right">
          <van-tag color="#8ec5cc" v-if="item.hasbadrecord <=1">{{companyBad(item.hasbadrecord)}}</van-tag>
          <van-tag color="#d9aa60" v-else>{{companyBad(item.hasbadrecord)}}</van-tag>
        </van-col>
      </van-row>
      <div>
        <van-tag color="#8eaccc">{{companyType(item.type)}}</van-tag>
        <span class="legal">{{item.legal}}</span>
        <span>(企业负责人)</span>
      </div>
      <div class="address van-ellipsis">{{item.address}}</div>
    </div>
  </div>
</template>

<script>
  import {companyType, companyBad}  from '@/utils/type'
  export default {
    name: 'CompnayListItem',
    data () {
      return {
        companyType,
        companyBad,
        results: [],
      }
    },
    props: ['result', 'isReload'],
    methods:{
        toView(id){
          this.$router.push({
            name:'CompanyView',
            params:{
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
  .companylistitem {
    color: #3c3c3c;
    padding: 0 .5rem;
  }

  .companylistitem .tit .van-col--20 {
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
</style>

