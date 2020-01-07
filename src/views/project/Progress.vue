<template>
    <van-row class="progress" >
      <van-col span="4" class="t-center">
        <div class="year" v-for="(value,key) in yearData">
          <div class="tit" @click="openers(key,$event)">{{key}}</div>
          <div class="monthCont" style="display: none;">
            <div v-for="(month,monthkey) in value" :class="month.is_current?'act':''"
                 @click="progresser(month.id,month.is_input,$event)">
              <span :class="month.is_input?'circle':''"></span><span>{{month.month}}月</span>
            </div>
          </div>
        </div>
      </van-col>
      <van-col span="20">
          <div class="one-block">
            <van-row type="flex"  align="center">
              <van-col style="margin-right: .5rem">工资:</van-col>
              <van-col span="15">
                <van-progress
                    :percentage="percentage"
                    :show-pivot="false"
                    color="#8eaccc"
                />
              </van-col>
              <van-col>{{prog.percent}}%</van-col>
            </van-row>
            <van-row type="flex" align="center">
              <van-col>
                <div >日期: <span class="info" >{{prog.year}}年-{{prog.month}}月</span></div>
              </van-col>
              <van-col span="4" style="text-align: right">
                <van-tag color="#8ec5cc" v-if="prog.status==0" >正常</van-tag>
                <van-tag color="#d9aa60" v-else >异常</van-tag>
              </van-col>
            </van-row>
          </div>
          <div class="one-block">
            <div class="import-text">工程巡查情况:</div>
            <div style="padding-right:.5rem">{{prog.content}}</div>
          </div>

          <van-row class="one-block">
            <van-col span="12">
              <div>
                监管类型:
                <span v-if="prog.rtype==0" >正常</span>
                <span v-else-if="prog.rtype==1">常态监管</span>
                <span v-else-if="prog.rtype==2" class="bad">重点监管</span>
                <span class="bad" v-else>严重监管</span>
              </div>
              <div>
                员工是否有签订合同:
                <span v-if="prog.contract==0" >有</span>
                <span class="bad" v-else >无</span>
              </div>
              <div>
                是否进行实名制管理:
                <span v-if="prog.realname==0" >有</span>
                <span class="bad" v-else >无</span>
              </div>
              <div>
                有无考勤记录:
                <span v-if="prog.attend==0" >有</span>
                <span class="bad" v-else >无</span>
              </div>
            </van-col>
            <van-col span="12">
              <div>
                农民工工资公示:
                <span v-if="prog.lwages==0" >有</span>
                <span class="bad" v-else >无</span>
              </div>
              <div>
                劳务专员任命书:
                <span v-if="prog.lab==0" >有</span>
                <span class="bad" v-else >无</span>
              </div>
              <div>
                项目经理任命书:
                <span v-if="prog.pab==0" >有</span>
                <span class="bad" v-else >无</span>
              </div>
              <div>
                农民工工资支付凭证:
                <span v-if="prog.lpaycert==0" >有</span>
                <span class="bad" v-else >无</span>
              </div>
            </van-col>
          </van-row>

          <div class="one-block">
            <div class="import-text">月度工资情况发放表:</div>
            <table class="table" >
              <tbody>
              <tr>
                <td style="width: 50%">用工人数：<span>{{prog.workers}}</span></td>
                <td style="width: 50%">支付款项：<span>{{prog.payment}}</span></td>
              </tr>
              <tr>
                <td>应发人数：<span>{{prog.shouldissues}}</span></td>
                <td>欠款：<span>{{prog.overdraft}}</span></td>
              </tr>
              <tr>
                <td>实际发放数：<span>{{prog.realissues}}</span></td>
                <td>差值：<span>{{parseFloat(prog.totalsalary)-parseFloat(prog.overdraft)}}</span></td>
              </tr>
              <tr>
                <td>打卡数：<span>{{prog.punches}}</span></td>
                <td>总工资：<span>{{prog.totalsalary}}</span></td>
              </tr>
              </tbody>
            </table>
          </div>
          <div class="one-block">
            <div class="import-text">询问人员:</div>
            <div style="width: 100%;overflow-x: scroll">
              <table class="table person" >
                <thead>
                <tr>
                  <th style="width: 20%">姓名</th>
                  <th style="width: 25%">电话</th>
                  <th >班组</th>
                  <th >时间</th>
                  <th style="width: 25%">工资领取情况</th>
                </tr>
                </thead>
                <tbody  >
                <tr v-for="person in prog.person">
                  <td >{{person.name}}</td>
                  <td >{{person.phone}}</td>
                  <td >{{person.class}}</td>
                  <td >{{person.time}}</td>
                  <td >{{person.wage}}</td>
                </tr>
                </tbody>
              </table>
            </div>

          </div>
        <div class="one-block">
          <div class="import-text">进度图片:</div>
          <ProgressImg :groupList="prog.pics"></ProgressImg>
        </div>
      </van-col>
    </van-row>

</template>

<script>
  import ProgressImg  from '@/components/GroupImg/ProgressImg'
  import {queryProgress}  from '@/api/api'

  export default {
    name: 'Progress',
    data () {
      return {
        prog: {},
        yearData: '',
        percentage:0,
      }
    },
    props: ['progress', 'yearlist'],
    components: {
      ProgressImg
    },
    methods: {
      progresser(id, is_input, event){
        if (!is_input) return;
        var eAct = document.getElementsByClassName('act')[0];
        eAct.setAttribute("class", "");
        var el = event.currentTarget;
        el.setAttribute("class", "act");
        queryProgress({"id": id}).then(res => {
          this.prog=res.progress;
        })
      },
      openers(key,event){
        var el = event.currentTarget;
        var monthCont = el.nextElementSibling;
        if (monthCont.style.display == 'none') {
          monthCont.style.display = 'block'
        } else {
          monthCont.style.display = 'none'
        }
      },
      init(){
        this.yearData = this.yearlist;
        this.prog = this.progress;
        this.percentage=parseInt(this.prog.percent)>=100?100:parseInt(this.prog.percent);
      }
    },
    mounted(){
      var arrs=localStorage.getItem('permission');
      var rootArr=arrs.split(',');
      if(rootArr.indexOf('progress_show')!=-1){
        this.init();
      } else{
        this.$toast('没有查看权限，请联系管理员');
      }
    },
  }
</script>


<style scoped>
  .progress{
    padding-right: .5rem;
  }
  .t-center {
    font-weight: bold;
    font-size: 1.2rem;
    padding: .5rem;
  }

  .monthCont div {
    margin: .5rem 0;
    color: #888888;
  }

  .monthCont .circle+span{
    color: #3c3c3c;
  }
  .circle {
    display: inline-block;
    height: .6rem;
    width: .6rem;
    vertical-align: middle;
    background: #8ec5cc;
    border-radius: 50%;
    margin-right: .5rem;
  }
  .act{
    background: #8eaccc;
  }
  .bad{
    color: #d9aa60;
  }
  .info{
    font-weight: bold;
  }
  .import-text{
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: .5rem;
  }
  .one-block{
    border-bottom: 1px solid #ececec;
    padding-bottom: .5rem;
    margin-bottom: .5rem;
  }
  .table{
    border-spacing: 0px;
    border-collapse: collapse;
    width: 95%;margin-top: 1px;
  }
  .person{
    width:150%;
  }
  .table tr td,table{
    border: 1px solid #3c3c3c;
    padding-left: .5rem;
    font-weight: bold;
  }
  .table tr td span{
    font-weight: normal;
  }

  .table.person tr th,.table.person tr td{
    border: 1px solid #ececec;
    padding-left: 0;
    font-weight: normal;
    text-align: center;
    font-size: 1rem;
  }
  .table.person tr th{
    font-weight: bold;
  }
</style>
