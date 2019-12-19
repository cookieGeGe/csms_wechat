<template>
  <div class="gualistitem">
    <div v-for="item in results"
         @click="toView(item.id,item.year,item.month)"
         style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem .5rem;">
      <van-row class="tit" type="flex" align="center">
        <van-col span="9">
          <div>{{item.name}} [{{item.phone}}]</div>
          <div>{{item.idcard}}</div>
          <div>
            <van-tag color="#8eaccc">{{laborJob(item.jobtype)}}</van-tag>
            <van-tag color="#8ec5cc">{{laborSex(item.sex)}}</van-tag>
            <van-tag color="#8ec5cc">{{item.nationality}}</van-tag>
            <van-tag color="#8eaccc">{{item.age}}</van-tag>
          </div>
        </van-col>
        <van-col span="10">
            <div class="van-multi-ellipsis--l2 mini-line-height">{{item.projectname}}</div>
            <div class="van-multi-ellipsis--l2 mini-line-height">{{item.companyname}}</div>
            <div>{{item.classname}}(班组)</div>
        </van-col>
        <van-col span="5" class="t-center">
          <div style="font-size: 1.3rem;">{{item.punch||0}}天</div>
          <div class="yellow-c">{{item.unpunch-item.punch||0}}未打卡</div>
        </van-col>
      </van-row>
    </div>
  </div>
</template>

<script>
  import {laborJob, laborSex} from '@/utils/type';

  export default {
    name: 'AttendItem',
    data() {
      return {
        laborJob,
        laborSex,
        results: [],
      }
    },
    props: ['result', 'isReload','isone'],
    methods: {
      toView(id,year,month) {
        this.$router.push({
          path: '/AttendView',
          query: {
            id,
            year,
            month,
          },
        });
      }
    },
    watch: {                        //监听value的变化，进行相应的操作即可
      result: function (a, b) {       //a是value的新值，b是旧值
        if (a != b) {
            if(this.isone){
              this.results=a;
            }else{
              this.results = this.results.concat(a); //数组
            }
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
  .t-center div:first-child{
    font-weight: bold;
  }

  .mini-line-height {
    line-height: 1.3;
  }

</style>

