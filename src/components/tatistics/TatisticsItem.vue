<template>
  <van-row class="TatisticsItem"  >
    <van-col span="8" style="border-right: 1px solid #888">
      <div >{{total}}</div>
      <div>{{name}}总数</div>
    </van-col>
    <van-col span="8">
      <div>{{month}}</div>
      <div>本月新增</div>
    </van-col>
    <van-col span="8">
      <div class="danger">{{alarm}}</div>
      <div>风险{{name}}</div>
    </van-col>
  </van-row>
</template>
<script>
  export default {
    name: 'TatisticsItem',
    data () {
      return {
        total: 0,
        alarm: 0,
        month: 0,
        name: ''
      }
    },
    props: ['datas', 'type'],
    methods: {
      formatter(){
        if (!this.datas) {
          return
        }
        this.total = this.datas[this.type].total;
        this.alarm = this.datas[this.type].alarm;
        this.month = this.datas[this.type].month;
        if (this.type == 'project') {
          this.name = '项目'
        } else if (this.type == 'company') {
          this.name = '企业'
        } else if (this.type == 'labor') {
          this.name = '劳工'
        }
      }
    },
    mounted() {
      this.formatter();
    },
    watch: {                       //监听value的变化，进行相应的操作即可
      datas: function (a, b) {     //a是value的新值，b是旧值
        if (a != b) {
          this.datas = a;
          this.formatter()
        }
      }
    }
  }
</script>
<style scoped>
  .TatisticsItem{
    background: #F2F7F7;
    text-align: center;
    padding: 1.5rem 0;
  }
  .TatisticsItem .van-col div:first-child {
    font-size: 3rem;
    margin-bottom: .5rem;
  }
  .TatisticsItem .van-col div:last-child {
    font-size: 1.5rem;
    color: #888;
  }
   .TatisticsItem .van-col .danger{
    color: red;
  }
</style>

