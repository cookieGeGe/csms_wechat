<template>
    <van-row class="progress" >
      <van-col span="4" class="t-center">
        <div class="year" v-for="(value,key) in yearData">
          <div class="tit" @click="openers(key,$event)">{{key}}</div>
          <div class="monthCont" style="display: none;">
            <div v-for="(month,monthkey) in value" :class="month.is_current?'act':''"
                 @click="progresser(month.id,month.is_input,$event)">
              <span :class="month.is_input?'circle':''"></span><span>{{monthkey + 1}}月</span>
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
            <div>{{prog.content}}</div>
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
          <!--<div>
            <div>询问人员:</div>
            <van-row>
              <van-col>姓名	</van-col>
              <van-col>电话	</van-col>
              <van-col>所在班组</van-col>
              <van-col>到场时间</van-col>
              <van-col>工资领取情况</van-col>
            </van-row>

            <van-row v-for="preson ">
              <van-col>姓名	</van-col>
              <van-col>电话	</van-col>
              <van-col>所在班组</van-col>
              <van-col>到场时间</van-col>
              <van-col>工资领取情况</van-col>
            </van-row>
            <div>进度照片:</div>
          </div>-->
      </van-col>
    </van-row>

</template>

<script>
  //import {projectTypeArr, projectBadArr}  from '@/utils/type'
  import {queryProgress}  from '@/api/api'

  export default {
    name: 'Progress',
    data () {
      return {
        prog: {},
        yearData: '',
        percentage:0
      }
    },
    props: ['progress', 'yearlist'],
    components: {},
    methods: {
      progresser(id, is_input, event){
        if (!is_input) return;
        var eAct = document.getElementsByClassName('act')[0];
        eAct.setAttribute("class", "");
        var el = event.currentTarget;
        el.setAttribute("class", "act");
      },
      openers(key,event){
        var el = event.currentTarget;
        var monthCont = el.nextElementSibling;
        console.log(monthCont);
        if (monthCont.style.display == 'none') {
          monthCont.style.display = 'block'
        } else {
          monthCont.style.display = 'none'
        }
      }
    },
    mounted(){
      this.yearData = this.yearlist;
      this.prog = this.progress;
      this.percentage=parseInt(this.prog.percent)>=100?100:parseInt(this.prog.percent)
    },
  }
</script>


<style scoped>
  .t-center {
    font-weight: bold;
    font-size: 1.2rem;
    padding: .5rem;
  }

  .monthCont {

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
  .bad{
    color: #d9aa60;
  }
  .info{
    font-weight: bold;
  }
  .import-text{
    font-size: 1.2rem;
    font-weight: bold;
  }
  .one-block{
    border-bottom: 1px solid #ececec;
    padding-bottom: .5rem;
    margin-bottom: .5rem;
  }
  .table{
    border-spacing: 0px;
    border-collapse: collapse;
    width: 100%;margin-top: 1px;
  }
  .table tr td{
    border: 1px solid #3c3c3c;
    padding-left: .5rem;
    font-weight: bold;
  }
  .table tr td span{
    font-weight: normal;
  }
</style>
