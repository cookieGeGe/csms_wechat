<template>
  <div class="laborlistitem">
    <div v-for="item in results"
         @click="toView(item.id)"
         style="border-bottom: 1px solid #ececec;padding:.5rem .5rem 1rem  .5rem">
      <van-row type="flex" align="center" justify="space-between">
        <van-col span="5" style="overflow: hidden;">
          <div style="border-radius: 100%;
                width: 6rem;
                overflow: hidden;
                height: 6rem;
                border: 2px solid #dde6f0;
">
            <img v-if="item.avatar.length>0" :src="myLocalHost+getMinImage(item.avatar)" style="width: 100%">
            <img v-else src="../../assets/index/labor.png" style="width: 100%">
          </div>

        </van-col>
        <van-col offset="1" span="18">
          <div>
            <span class="name">{{item.name}} </span>
            <van-tag color="#8eaccc">{{laborJob(item.jobtype)}} </van-tag>
            <van-tag :color="item.sex?'#8ec5cc':'#d9aa60'">{{laborSex(item.sex)}} </van-tag>
            <van-tag color="#8ec5cc">{{item.nationality}} </van-tag>
            <van-tag color="#8ec5cc">{{item.age}} </van-tag>
            <van-tag v-if="item.isbadrecord>0" color="#d9aa60">{{laborIsbadrecord(item.isbadrecord)}} </van-tag>
          </div>
          <div>{{item.pname}}-{{item.dname}}-{{item.cname}}</div>
          <div class="van-ellipsis">项目名称:<span class="mianColor">{{item.projectname}}</span></div>
          <div class="van-ellipsis">所属企业:<span class="mianColor">{{item.companyname}}</span></div>
        </van-col>
      </van-row>
    </div>
  </div>

</template>

<script>
  import {laborSex, laborJob, laborIsbadrecord, getMinImage}  from '@/utils/type'
  export default {
    name: 'LaborListItem',
    data () {
      return {
        laborSex,
        laborJob,
        laborIsbadrecord,
        getMinImage,
        results: []
      }
    },
    methods:{
      toView(id){
        this.$router.push({
          path:'/LaborView',
          query:{
            id
          },
        });
      }
    },
    props: ['result', 'isReload'],
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
  .laborlistitem {
    color: #888888;
    font-sizes: 1.2rem;
    /*padding: 0 .5rem;*/
  }

  .laborlistitem .name {
    font-size: 1.4rem;
    font-weight: bold;
    color: #333;
  }

  .laborlistitem .mianColor {
    color: #333;
    font-weight: bold;
  }

  .laborlistitem .van-col--18 div {
    margin: .5rem;
  }
</style>

