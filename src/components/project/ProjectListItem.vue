<template>
  <div class="projectlistitem">
    <div v-for="item in results" :key="item.id"
         @click="toView(item.id)"
         style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem .5rem">
      <van-row type="flex" align="center">
        <van-col span="20">
          <div  class="van-ellipsis tit"> {{item.name}}  </div>
          <div  class="van-ellipsis info">项目地址:{{item.address}}</div>
        </van-col>
        <van-col span="4" style="text-align: right">
          <van-tag color="#8ec5cc"  v-if="item.status <=1">{{projectBad(item.status)}} </van-tag>
          <van-tag color="#d9aa60" v-else>{{projectBad(item.status)}} </van-tag>
          <van-tag color="#8eaccc" style="margin-top: .5rem" v-if="daochu" @click.stop="file(item.name,item.id)">导出</van-tag>
          <van-tag color="#8eaccc" style="margin-top: .5rem" v-if="daochu" @click.stop="kaoqin(item.name,item.id)">考勤</van-tag>
        </van-col>
      </van-row>
      <van-row  type="flex" justify="space-between" >
        <van-col >项目类型: <van-tag color="#8eaccc">{{projectType(item.type)}}</van-tag> </van-col>
        <van-col >工期: {{item.starttime}} ~ {{item.endtime}}</van-col>
      </van-row>
      <van-row  type="flex" justify="space-between">
        <van-col >担保类型: {{guarantype(item.type)}}</van-col>
        <van-col >担保金额: ￥{{item.gamount}}元</van-col>
      </van-row>
      <van-row  type="flex" justify="space-between" align="center">
        <van-col >工资发放:</van-col>
        <van-col span="16">
          <van-progress
                        :percentage="parseInt(item.wagepercent)>=100?100:parseInt(item.wagepercent)"
                        :show-pivot="false"
                        color="#8eaccc"

          />
        </van-col>
        <van-col >{{item.wagepercent}}%</van-col>
      </van-row>
      <van-row  type="flex">
        <van-col>代发银行: {{item.bank}}</van-col>
      </van-row>
    </div>
  </div>

</template>

<script>
  import {projectType, projectBad,guarantype}  from '@/utils/type'
  export default {
    name: 'ProjectListItem',
    data () {
      return {
        projectType,
        projectBad,
        guarantype,
        results:[]
      }
    },
    props: ['result', 'isReload','daochu','source'],
    methods:{
      toView(id){
        this.$router.push({
          path:'/ProjectView',
          query:{
            id,
            sources:this.source||'项目查询'
          },
        });
      },
      file(name,id){
          var href=this.myLocalHost+'/template/export?type=word&ft=project&id='+id;
          window.open(href,name);
      },
      kaoqin(name, id){
        this.$router.push({
          path:'/Attend',
          query:{
            name,
            sources:'项目详情'
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
  .projectlistitem{
    font-size: 1.2rem;
    padding: 0 .5rem;
  }
  .projectlistitem .tit  {
    font-size: 1.6rem;
    font-weight: bold;
    color: #3c3c3c;
  }
  .projectlistitem .info  {
    font-size: 1rem;
    color: #888888;
  }
  /deep/ .van-row--flex{
    margin-bottom: .5rem;
  }
</style>

