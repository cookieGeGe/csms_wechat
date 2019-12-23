<template>
  <div style="padding-top: 1rem;">
    <van-row class="searchreuslt" type="flex" align="center">
      <van-col span="8" style="">
        <div class="tit">{{name}}</div>
        <div class="tit">{{date}}</div>
      </van-col>
      <van-col span="4" style="border-right: 1px solid #ececee;border-left: 1px solid #ececee">
        <div>总数</div>
        <div class="num">{{total}}</div>
      </van-col>
      <van-col span="7" style="text-align: left;padding-left: 1rem">
        <div>未考勤 <span class="num" style="color:#8ec5cc">{{normal}}</span></div>
        <div>已考勤 <span class="num" style="color:#d9aa60">{{abnormal}}</span></div>
      </van-col>
      <van-col span="4" offset="1">
        <van-circle
          v-model="currentrate"
          :rate="currentrate"
          :speed="100"
          :text="text"
          color="#d9aa60"
          layer-color="#8ec5cc"
          :stroke-width="80"
          size="5rem"
        />
      </van-col>
    </van-row>

    <div class="card">
      <div class="gualistitem">
        <div v-for="item in results"
             style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem .5rem;">
          <van-row class="tit" type="flex" align="center" justify="space-around">
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
            <van-col span="12">
              <div class="van-multi-ellipsis--l2 mini-line-height">{{item.projectname}}</div>
              <div class="van-multi-ellipsis--l2 mini-line-height">{{item.companyname}}</div>
              <div>{{item.classname}}(班组)</div>
            </van-col>
            <van-col span="3" class="t-center">
              <van-tag color="#8ec5cc" v-if="item.attend">已考勤</van-tag>
              <van-tag color="#d96c60" v-else>未考勤</van-tag>

            </van-col>
          </van-row>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import {laborJob, laborSex} from '@/utils/type';
  import {queryAttendProCom} from '@/api/api';

  export default {
    name: "AttendInfo",
    data() {
      return {
        laborJob,
        laborSex,
        total: 0,
        normal: 0,
        abnormal: 0,
        currentrate: 0,
        results: [],
        name: '',
        date: '',
        params: {}
      }
    },
    methods: {
      reload() {
        var params = {
          id: this.params.id,
          type: this.params.type,
          date: this.params.date
        }
        queryAttendProCom(params).then(res => {
        //  console.log(res)
          this.total = res.total;
          this.normal = res.normal;
          this.abnormal = res.abnormal;
          this.currentrate = res.currentrate;
          this.results = res.info;
        })
      }
    },
    mounted() {
      this.params = this.$route.query;
      this.name = this.params.name;
      this.date = this.params.date;
      this.reload();
    },
    computed: {
      text() {
        return this.currentrate + '%'
      }
    },
  }
</script>

<style scoped>
  .card {
    font-size: 1.1rem;
    padding: 1rem 1rem;
  }

  .searchreuslt {
    text-align: center;
    background: white;
    color: #888888;
    margin: 10px;
    padding: 1rem;
    border-radius: 5px;
  }

  .searchreuslt .tit {
    /*font-size: 1.4rem;*/
    color: #3c3c3c;
    font-weight: bold;
  }

  .searchreuslt .num {
    font-size: 2rem;
    color: #3c3c3c;
  }

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

  .t-center div:first-child {
    font-weight: bold;
  }

  .mini-line-height {
    line-height: 1.3;
  }

</style>
