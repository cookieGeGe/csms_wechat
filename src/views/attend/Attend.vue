<template>
  <div class="company">

    <Search @searchObj="searchObj"></Search>
    <van-row type="flex" align="center" justify="space-between" style="margin: 10px;margin-top: 0;">
      <van-col @click="show=true">
        <van-tag round type="primary" color="#8eaccc" style="padding: 3px 1rem">更新时间</van-tag>
      </van-col>
    </van-row>

    <van-popup v-model="show" position="bottom">
      <van-datetime-picker
        v-model="currentDate"
        type="year-month"
        :min-date="minDate"
        @confirm="confirms"
        @cancel="show = false"
      />
    </van-popup>
    <van-tabs background="transparent"
              color="#fff"
              title-inactive-color="#fff"
              title-active-color="#fff"
              class="searach-tabs"
              @click="changeTabs"
    >
      <van-tab title="项 目" name="project">
        <div class="guarantee">
          <div style="font-weight: bold;line-height: 3rem;padding-left: 10px;border-bottom: 1px solid #ececec;">
            查询结果( <span style="color: #8ec5cc; font-size: 1.5rem;">{{pro_total}}</span> 条)
          </div>
          <div class="header">
            <van-row align="center">
              <van-col span="14">项目名称</van-col>
              <van-col span="5">时间</van-col>
              <van-col span="5">考勤统计</van-col>
            </van-row>
          </div>
          <van-list
            v-model="pro_loading"
            :finished="pro_finished"
            finished-text="没有更多了"
            @load="onLoad"
            :immediate-check="false"
          >
            <Attendlist :isReload="pro_isReload" :result="pro_result"></Attendlist>
          </van-list>
        </div>

      </van-tab>
      <van-tab title="企 业" name="company">
        <div class="guarantee">
          <div style="font-weight: bold;line-height: 3rem;padding-left: 10px;border-bottom: 1px solid #ececec;">
            查询结果( <span style="color: #8ec5cc; font-size: 1.5rem;">{{com_total}}</span> 条)
          </div>
          <div class="header">
            <van-row align="center">
              <van-col span="14">企业名称</van-col>
              <van-col span="5">时间</van-col>
              <van-col span="5">考勤统计</van-col>
            </van-row>
          </div>
          <van-list
            v-model="com_loading"
            :finished="com_finished"
            finished-text="没有更多了"
            @load="onLoad"
            :immediate-check="false"
          >
            <Attendlist :isReload="com_isReload" :result="com_result"></Attendlist>
          </van-list>
        </div>
      </van-tab>
      <van-tab title="劳 工" name="labor">
        <div class="guarantee">
          <div style="font-weight: bold;line-height: 3rem;padding-left: 10px;border-bottom: 1px solid #ececec;">
            查询结果( <span style="color: #8ec5cc; font-size: 1.5rem;">{{total}}</span> 条)
          </div>
          <div class="header">
            <van-row align="center">
              <van-col span="9">劳工信息</van-col>
              <van-col span="10">项目/企业/班组</van-col>
              <van-col span="5">考勤统计</van-col>
            </van-row>
          </div>
          <van-list
            v-model="loading"
            :finished="finished"
            finished-text="没有更多了"
            @load="onLoad"
            :immediate-check="false"
          >
            <AttendItem :isReload="isReload" :result="this.result"></AttendItem>
          </van-list>
        </div>
      </van-tab>
    </van-tabs>


    <!---->
  </div>
</template>

<script>
  import {queryAttend} from '@/api/api';
  import Search from '@/components/areas/Search';
  import AttendItem from '@/components/attend/AttendItem';
  import Attendlist from '@/components/attend/Attendlist';


  export default {
    name: 'Company',
    data() {
      return {
        show: false,
        allbank: [],
        currentDate: new Date(),
        minDate: new Date(1970, 1, 1),
        searchType: {
          name: '',
          type: 'project',
          month: '',
          page: 1,
        },
        loading: false,
        isReload: true,
        finished: false,
        para: {},
        result: [],
        total: 0,

        pro_loading: false,
        pro_isReload: true,
        pro_finished: false,
        pro_result: [],
        pro_total: 0,

        com_loading: false,
        com_isReload: true,
        com_finished: false,
        com_result: [],
        com_result: 0,
      }
    },
    components: {
      Search,
      AttendItem,
      Attendlist
    },
    methods: {
      changeTabs(name, title) {
        this.searchType.type = name;
        this.searching();
      },
      confirms() {
        this.searchType.time = this.currentDate;
        this.show = false;
        this.searching();
      },
      reload() {
        this.finished = false;
        this.loading = true;
        queryAttend(this.searchType).then(res => {
          var ret = res.data;
          if (ret.length < 10) {
            this.finished = true;  //是否全部加载完毕
          }
          // this.total += ret.length;
          this.isReload = false; //是否重新赋值
          this.loading = false;  //是否结束加载状态
          this.result = ret;
          this.searchType.page++;
          this.total = res.total;
        });
      },
      com_reload() {
        this.com_finished = false;
        this.com_loading = true;
        queryAttend(this.searchType).then(res => {
          var ret = res.date;
          if (ret.length < 10) {
            this.com_finished = true;  //是否全部加载完毕
          }
          // this.total += ret.length;
          this.com_isReload = false; //是否重新赋值
          this.com_loading = false;  //是否结束加载状态
          this.com_result = ret;
          this.searchType.page++;
          this.com_total = res.total;
        });
      },
      pro_reload() {
        this.pro_finished = false;
        this.pro_loading = true;
        queryAttend(this.searchType).then(res => {
          var ret = res.date;
          if (ret.length < 10) {
            this.pro_finished = true;  //是否全部加载完毕
          }
          // this.total += ret.length;
          this.pro_isReload = false; //是否重新赋值
          this.pro_loading = false;  //是否结束加载状态
          this.pro_result = ret;
          this.searchType.page++;
          this.pro_total = res.total;
        });
      },
      searchObj(params) {
        this.searchType = Object.assign(this.searchType, params);
        this.searching();
      },
      onLoad() {
        if (this.searchType.type == 'project') {
          this.pro_reload();
        } else if (this.searchType.type == 'company') {
          this.com_reload();
        } else {
          this.reload();
        }
      },
      searching() {  //重置搜索状态

        this.searchType.page = 1;
        if (this.searchType.type == 'project') {
          this.pro_isReload = true
          this.pro_reload();
        } else if (this.searchType.type == 'company') {
          this.com_isReload = true;
          this.com_reload();
        } else {
          this.isReload = true;
          this.reload();
        }
      }
    },
    created() {
      // localStorage.setItem('searchParams', JSON.stringify(this.$route.params));
    },
    mounted() {
      this.searching();
      // this.searchObj(this.$route.params)
    }
  }
</script>


<style scoped>
  /deep/ .header .van-row {
    text-align: center;
    font-size: 1.2rem;
    font-weight: bold;
    margin-top: 0.5rem;
  }

  .header {
    padding: 0.5rem;
  }

  .company .dropdown {
    border-radius: 50rem;
    height: 1.8rem;
  }

  /deep/
  .van-dropdown-menu__title {
    font-size: 1rem;
  }

  /deep/ .van-dropdown-menu__item {
    padding-right: 10px;
  }

  /deep/ .van-dropdown-menu__title {
    line-height: 1.8rem;
  }

  /deep/ .van-dropdown-menu__title div {
    margin-top: 1px;
  }

  .company /deep/ .van-dropdown-item__option {
    line-height: 1rem;
    font-size: 1rem;
  }

  .guarantee {
    position: relative;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    color: #323233;
    opacity: 0.9;
    border-radius: 4px;
    line-height: 1.7rem;
    background-color: #f8fbfc;
    margin: 1rem 0;
  }

  .guarantee div {
    line-height: 2rem;
  }
</style>
