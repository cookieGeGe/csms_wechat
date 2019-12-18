<template>
  <div class="van-content">
    <Calendar
      @choseDay="clickDay"
      @changeMonth="changeDate"
      >
     <!-- // v-on:isToday="clickToday"
      // :markDate=arr // arr=['2018/4/1','2018/4/3'] 标记4月1日和4月3日 简单标记
      //:markDateMore=arr // 多种不同的标记
      // 第一个标记和第二个标记不能同时使用
      // :agoDayHide='1514937600' //某个日期以前的不允许点击  时间戳10位
      // :futureDayHide='1525104000' //某个日期以后的不允许点击  时间戳10位
      // :sundayStart="true" //默认是周一开始 当是true的时候 是周日开始-->
    </Calendar>

    <div class="card">
      <AttendItem :isReload="isReload" :result="result[0]"></AttendItem>
    </div>
  </div>
</template>

<script>
  import Calendar from 'vue-calendar-component';
  import AttendItem from '@/components/attend/AttendItem';
  import {queryAttendInfo} from '@/api/api';

  export default {
    name: "AttendView",
    data() {
      return {
        searchType: {
          id: -1,
        },
        isReload: true,
        result: [],
      }
    },
    components: {
      Calendar,
      AttendItem,

    },
    methods: {
      clickDay(data) {
        console.log(data); //选中某天
      },
      changeDate(data) {
        console.log(data); //左右点击切换月份
      },
      clickToday(data) {
        console.log(data); //跳到了本月
      },
      reload() {

        queryAttendInfo({id:55,year:2019,month:7,}).then((res) => {
          var ret = res.data;
          console.log(res);
          this.isReload = false; //是否重新赋值
          this.result = ret;
        });
      },
      showimg(img) {
        this.images = [img];
        this.show = true;
      },

    },
    mounted() {
      this.searchType.id = this.$route.params.id;
      this.reload();
    }
  }
</script>

<style scoped>
  .card {
    padding: 0.5rem 0.5rem;
    font-size: 1.1rem !important;
  }
  .van-content /deep/ .wh_content_all{
    background-color: rgba(255, 255, 255, 0.77);
    font-size: 1.2rem;
  }
  .van-content /deep/ .wh_content_li{
    color: #8eaccc;
  }
  .van-content /deep/ .wh_jiantou1{
    border-top: 2px solid #8eaccc;
    border-left: 2px solid #8eaccc;
  }
  .van-content /deep/ .wh_jiantou2{
    border-top: 2px solid #8eaccc;
    border-right: 2px solid #8eaccc;
  }
  .van-content /deep/ .wh_top_tag{
    color: #000;
    font-weight: bold;
  }

  .van-content /deep/ .wh_item_date{
    color: #3c3c3c;
  }
  .van-content /deep/ .wh_item_date.wh_other_dayhide{
    color: #bfbfbf;
  }
</style>
