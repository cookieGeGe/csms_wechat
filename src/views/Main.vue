<template>
  <div class="main" >
    <!--标题-->
    <van-row type="flex" justify="space-between" class="header-box">
      <van-col span="14" class="header-tit">建筑工地管理系统</van-col>
      <van-col span="10">
        <van-row type="flex" justify="space-between" align="center">
          <van-col span="12" class="t-right"><img src="../assets/index/user.png" style="width: 2rem"></van-col>
          <van-col span="12" class="header-text" style="padding-left: 1rem">
            <div class="LoginName">{{LoginName}}</div>
            <div class="admintype">{{admintype}}</div>
          </van-col>
        </van-row>
      </van-col>
    </van-row>

    <!--  tab切换和搜索  -->
    <van-tabs background="transparent"
              color="#fff"
              title-inactive-color="#fff"
              title-active-color="#fff"
              class="searach-tabs"
              @click="changeTabs"
    >
      <van-tab title="项 目" name="Project"></van-tab>
      <van-tab title="企 业" name="Company"></van-tab>
      <van-tab title="劳 工" name="Labor"></van-tab>
    </van-tabs>
    <Search   @searchObj="searchObj"></Search>

    <!--菜单  -->
    <div class="menus-box">
      <div class="menus-tit">所有功能</div>
      <van-tabbar v-model="menus"
                  :fixed="false"
                  inactive-color="#3c3c3c"
                  style="background: transparent;height: 6rem;font-size: 1.6rem"
      >
        <van-tabbar-item name="company" to="/Company">
          <span>企业查询</span>
          <img slot="icon" src="../assets/index/index_icon1.png">
        </van-tabbar-item>
        <van-tabbar-item name="project" to="/Project">
          <span>项目查询</span>
          <img slot="icon" src="../assets/index/index_icon2.png">
        </van-tabbar-item>
        <van-tabbar-item name="labor" to="/Labor">
          <span>劳工查询</span>
          <img slot="icon" src="../assets/index/index_icon3.png">
        </van-tabbar-item>
        <van-tabbar-item name="attend" to="/Attend">
          <span>考勤查询</span>
          <img slot="icon" src="../assets/index/index_icon4.png">
        </van-tabbar-item>
      </van-tabbar>
      <van-tabbar v-model="menus"
                  :fixed="false"
                  inactive-color="#3c3c3c"
                  style="background: transparent;height: 6rem"
      >
        <van-tabbar-item name="salary" to="/Salary">
          <span>工资查询</span>
          <img slot="icon" src="../assets/index/index_icon5.png">
        </van-tabbar-item>
        <van-tabbar-item name="bank" to="/Bank">
          <span>银行查询</span>
          <img slot="icon" src="../assets/index/index_icon6.png">
        </van-tabbar-item>
        <van-tabbar-item name="guarantee" to="/Guarantee">
          <span>保函查询</span>
          <img slot="icon" src="../assets/index/index_icon7.png">
        </van-tabbar-item>
        <van-tabbar-item name="help" to="/Help">
          <span>帮助中心</span>
          <img slot="icon" src="../assets/index/index_icon8.png">
        </van-tabbar-item>
      </van-tabbar>
    </div>

    <!--统计  -->
    <van-tabs color="#8eaccc"
              title-inactive-color="#5e5e5e"
              title-active-color="#5e5e5e"
              class="statistics"
    >
      <van-tab title="项目统计">
        <TatisticsItem :datas="statisticsData" type="project"></TatisticsItem>
      </van-tab>
      <van-tab title="企业统计">
        <TatisticsItem :datas="statisticsData" type="company"></TatisticsItem>
      </van-tab>
      <van-tab title="劳工统计">
        <TatisticsItem :datas="statisticsData" type="labor"></TatisticsItem>
      </van-tab>
    </van-tabs>

    <!--风险  -->

     <van-tabs v-model="activeName"
                color="#8eaccc"
                title-inactive-color="#5e5e5e"
                title-active-color="#5e5e5e"
                class="risk"
                @click="changeStatus"
      >
        <van-tab title="项目风险" name="project">
          <van-list
            v-model="tabsing.project.loading"
            :finished="tabsing.project.finished"
            finished-text="没有更多了"
            @load="onLoad"
          >
            <ProjectListItem :result="tabsing.project.result"></ProjectListItem>
          </van-list>
        </van-tab>
        <van-tab title="企业风险" name="company">
          <van-list
            v-model="tabsing.company.loading"
            :finished="tabsing.company.finished"
            finished-text="没有更多了"
            @load="onLoad"
          >
            <CompnayListItem :result="tabsing.company.result"></CompnayListItem>
          </van-list>
        </van-tab>
        <van-tab title="劳工风险" name="labor">
          <van-list
            v-model="tabsing.labor.loading"
            :finished="tabsing.labor.finished"
            finished-text="没有更多了"
            @load="onLoad"
          >
          <LaborListItem :result="tabsing.labor.result"></LaborListItem>
          </van-list>
        </van-tab>
      </van-tabs>

  </div>
</template>

<script>
  import {indexCount, queryProject, queryCompany, queryLabor}  from '@/api/api';
  import {getAdmintype}  from '@/utils/type'

  import Search from '@/components/areas/Search'
  import TatisticsItem from '@/components/tatistics/TatisticsItem'
  import ProjectListItem from '@/components/project/ProjectListItem'
  import CompnayListItem from '@/components/company/CompnayListItem'
  import LaborListItem from '@/components/labor/LaborListItem'


  export default {
    name: 'Main',
    data () {
      return {
        LoginName: localStorage.getItem('LoginName'),
        admintype: getAdmintype(localStorage.getItem('admintype')),
        searchType: 'Project',
        menus: 0,
        statisticsData: '',

        activeName: 'company',
        tabsing:{
            'project':{
              result:[],
              page:1,
              loading:false,
              finished:false,
            },
            'company':{
              result:[],
              page:1,
              loading:false,
              finished:false,
            },
            'labor':{
              result:[],
              page:1,
              loading:false,
              finished:false,
            }
        },
      }
    },
    components: {
      'Search': Search,
      'TatisticsItem': TatisticsItem,
      'ProjectListItem': ProjectListItem,
      'CompnayListItem': CompnayListItem,
      'LaborListItem': LaborListItem,
    },
    methods: {
      changeTabs(name, title) {
        this.searchType = name;
      },
      changeStatus(name, title) {
        this.activeName = name;
      },
      init(){
        indexCount().then(res => {
          this.statisticsData = res;
        });
      },

      searchObj(params){
        this.$router.push({
          name:this.searchType,
          params,
        });
      },

      onLoad() {
        setTimeout(() => {
          var oneName=this.activeName;
          var oneTab=this.tabsing[oneName];
          var para = {status: false,page:oneTab.page};

          if(oneName=='project'){
            queryProject(para).then(res => {
              if(res[oneName].length<10) {
                oneTab.finished = true;
              }
              oneTab.loading=false;
              oneTab.result=res[oneName];
              oneTab.page++;
            });
          }else if(oneName=='company'){
            queryCompany(para).then(res => {
              if(res[oneName].length<10) {
                oneTab.finished = true;
              }
                oneTab.loading=false;
                oneTab.result=res[oneName];
                oneTab.page++;
            });
          }else if(oneName=='labor'){
            queryLabor(para).then(res => {
              if(res[oneName].length<10) {
                oneTab.finished = true;
              }
                oneTab.loading=false;
                oneTab.result=res[oneName];
                oneTab.page++;
            });
          }

        }, 500);
      }
    },
    mounted() {
      this.init();
      this.onLoad();

    },
  }
</script>

<style scoped>
  .header-box {
    padding: 1rem;
    color: #fff;
  }

  .header-tit {
    font-size: 2rem;
    font-weight: bold;
    text-align: left;
    padding-top: .5rem;
  }

  .van-tab--active {
    font-weight: bold;
  }

  .menus-box {
    border-bottom: 1px solid #ececee;
  }

  .menus-tit {
    font-size: 1.7rem;
    font-weight: bold;
    color: #5E5E5E;
    padding: 1rem;
    border-bottom: 1px solid #5e5e5e1a;
  }

  .van-tabbar-item__icon img {
    height: 3rem;
  }

  /deep/
  .statistics .van-tabs__wrap {
    margin-bottom: .5rem;
  }
</style>


