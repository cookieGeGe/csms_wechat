<template>
  <div class="gualistitem">
    <div v-for="item in results"
         @click="toView(item.id, item.date, item.name)"
         style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem .5rem;">
      <van-row class="tit" type="flex" align="center">
        <van-col span="14">
          <div>{{item.name}}</div>
        </van-col>
        <van-col span="5">
          <div style="text-align: center">{{item.date}}</div>
          <div style="text-align: center">{{item.info}}</div>
        </van-col>
        <van-col span="5" class="t-center">
          <div style="font-weight: unset;">
            <span style="font-size: 1.3rem; font-weight: bold">{{item.punch}}</span> /
            <span style="font-size: 1rem;">{{item.total}}</span></div>
          <div class="yellow-c">{{item.unpunch}}未打卡</div>

        </van-col>
      </van-row>
    </div>
  </div>
</template>

<script>
  import {laborJob, laborSex} from '@/utils/type';

  export default {
    name: 'Attendlist',
    data() {
      return {
        laborJob,
        laborSex,
        results: [],
        type:''
      }
    },
    props: ['result', 'isReload', 'type'],
    methods: {
      toView(id, date, name) {
       // console.log(id,date,name,this.type)
        this.$router.push({
          path: '/AttendInfo',
          query: {
            id,
            date,
            name,
            type:this.type,
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
    font-size: 1.2rem;
  }

  .gualistitem .tit .van-col--20 {
    font-size: 1.6rem;
    line-height: 3rem;
    font-weight: bold;
    color: #3c3c3c;
  }

  .t-center div:first-child {
    font-weight: bold;
  }

  .mini-line-height {
    line-height: 1.3;
  }

</style>

