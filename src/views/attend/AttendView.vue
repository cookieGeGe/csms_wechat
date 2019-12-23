<template>
  <div class="van-content">
    <headerBar fatherName="考勤查询" currentNmae="考勤详情"></headerBar>
    <Calendar ref="Calendar"
              @choseDay="clickDay"
              @changeMonth="changeDate"
              :markDateMore="nolist"
    >
    </Calendar>
    <div class="card">
      <AttendItem :isReload="isReload" :isone="true" :result="labor"></AttendItem>
    </div>

    <div class="attend">
      <h3 style="font-size: 1.4rem">
        {{dayData.year}}-{{dayData.month}}-{{dayData.day}} 考勤明细

      </h3>
      <van-row type="flex" align="center">
        <van-col span="3" class="t-center">
          <div>上</div>
          午
        </van-col>
        <van-col>
          <div class="time">上班:
            <span v-if="dayData.amin&&dayData.amin.length>0">{{dayData.amin}}</span>
            <span v-else style="color: #d9aa60">未打卡</span>
          </div>
          <div>打卡地址:{{dayData.aminpos}}</div>
          <div class="time">下班:
            <span v-if="dayData.amout&&dayData.amout.length>0">{{dayData.amout}}</span>
            <span v-else style="color: #d9aa60">未打卡</span></div>
          <div>打卡地址:{{dayData.amoutpos}}</div>
        </van-col>
      </van-row>
      <van-row type="flex" align="center">
        <van-col span="3" class="t-center">
          <div>下</div>
          午
        </van-col>
        <van-col>
          <div class="time">上班:
            <span v-if="dayData.pmin&&dayData.pmin.length>0">{{dayData.pmin}}</span>
            <span v-else style="color: #d9aa60">未打卡</span>

          </div>
          <div>打卡地址:{{dayData.pmoutpos}}</div>
          <div class="time">下班:
            <span v-if="dayData.pmout&&dayData.pmout.length>0">{{dayData.pmout}}</span>
            <span v-else style="color: #d9aa60">未打卡</span>
          </div>
          <div>打卡地址:{{dayData.pmoutpos}}</div>
        </van-col>
      </van-row>
    </div>

  </div>
</template>

<script>
  import Calendar from 'vue-calendar-component';
  import AttendItem from '@/components/attend/AttendItem';
  import headerBar from '@/components/areas/headerBar';
  import {queryAttendInfo} from '@/api/api';

  export default {
    name: "AttendView",
    data() {
      return {
        searchType: {},
        isReload: true,
        result: [],
        nolist: [],
        dayData: {},
        labor: []
      }
    },
    components: {
      Calendar,
      AttendItem,
      headerBar
    },
    methods: {
      clickDay(data) {
        var day = data.split('/')[2];
        this.result.forEach((val, index, arr) => {
          if (parseInt(val.day) == day) {
            this.dayData = val;
          }
        });
      },
      changeDate(data) {
        if (!this.changeDates) {
          return
        }
        var arrDate = data.split('/');
        this.searchType.year = arrDate[0];
        this.searchType.month = arrDate[1];
        this.reload();
      },
      reload() {
        this.changeDates = false;
        this.$refs.Calendar.ChoseMonth(this.searchType.year + '-' + this.searchType.month, false);
        setTimeout(() => {
          this.changeDates = true
        }, 500);
        queryAttendInfo(this.searchType).then((res) => {
          var ret = res.data;
          this.isReload = true; //是否重新赋值
          if (JSON.stringify(res.labor) !== '[]') {
            this.labor = res.labor
          } else {
            this.labor = []
          }
          if (JSON.stringify(ret) === '[]') {
            this.$toast('当月没有数据请及时填写');
            this.dayData = {};
          } else {
            this.result = ret;
            this.clickDay(ret[0].year + '/' + ret[0].month + '/' + ret[0].day);
            ret.forEach((val, index, arr) => {
              if (val.miss === '缺考') {
                this.nolist.push({date: val.year + '/' + val.month + '/' + val.day, className: "mark1"})
              } else {
                this.nolist.push({date: val.year + '/' + val.month + '/' + val.day, className: "mark2"})
              }
            });
          }
        });
      },

    },
    mounted() {
      this.searchType = this.$route.query;
      this.reload();
    }
  }
</script>

<style scoped>
  .card {
    padding: 0.5rem 0.5rem;
    font-size: 1.1rem !important;
  }

  .attend /deep/ .van-row {
    border-bottom: 1px solid #ececec;
    padding-bottom: 1rem;
  }

  .attend .t-center {
    text-align: center;
    margin-right: 10px;
    font-size: 1.4rem;
  }

  .time {
    font-size: 1.2rem;
    font-weight: bold;
    margin: .5rem 0;
  }

  .van-content /deep/ .wh_content_all {
    background-color: rgba(255, 255, 255, 0.77);
    font-size: 1.2rem;
  }

  .van-content /deep/ .wh_content_li {
    color: #8eaccc;
  }

  .van-content /deep/ .wh_jiantou1 {
    border-top: 2px solid #8eaccc;
    border-left: 2px solid #8eaccc;
  }

  .van-content /deep/ .wh_jiantou2 {
    border-top: 2px solid #8eaccc;
    border-right: 2px solid #8eaccc;
  }

  .van-content /deep/ .wh_top_tag {
    color: #000;
    font-weight: bold;
  }

  .van-content /deep/ .wh_item_date {
    color: #3c3c3c;
  }

  .van-content /deep/ .wh_item_date.wh_other_dayhide {
    color: #bfbfbf;
  }

  .van-content /deep/ .wh_item_date.wh_isToday {
    background: #8eaccc;
  }

  .van-content /deep/ .wh_item_date.wh_chose_day {
    background: #8eaccc !important;
  }

  .van-content /deep/ .wh_item_date.mark1 {
    background: #d9aa60;
    border-radius: 100px;
  }

  .van-content /deep/ .wh_item_date.mark2 {
    background: #8ec5cc;
    border-radius: 100px;
  }

</style>
