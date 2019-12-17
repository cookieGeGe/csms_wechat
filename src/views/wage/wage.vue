<template>
  <div class="company">
    <van-tabs background="transparent"
              color="#fff"
              title-inactive-color="#fff"
              title-active-color="#fff"
              class="searach-tabs"
              @click="changeTabs"
    >
      <van-tab title="项 目" name="project"></van-tab>
      <van-tab title="企 业" name="company"></van-tab>
      <van-tab title="劳 工" name="labor"></van-tab>
    </van-tabs>
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
    <div class="guarantee">
      <div style="font-weight: bold;line-height: 3rem;padding-left: 10px;border-bottom: 1px solid #ececec;">
        查询结果( <span style="color: #8ec5cc; font-size: 1.5rem;">{{total}}</span> 条)
      </div>
      <van-list
        v-model="loading"
        :finished="finished"
        finished-text="没有更多了"
        @load="onLoad"
        :immediate-check="false"
      >
        <wageItem :isReload="isReload" :result="this.result"></wageItem>
      </van-list>
    </div>
    <!---->
  </div>
</template>

<script>
  import {querySalary} from '@/api/api';
  import Search from '@/components/areas/Search';
  import wageItem from '@/components/wage/wageItem';


  export default {
    name: 'Company',
    data() {
      return {
        show: false,
        allbank: [],
        currentDate: new Date(),
        minDate: new Date(1970, 1, 1),
        searchType: {
          name:'',
          type:'project',
          month: '',
          page: 1,
        },
        loading: false,
        isReload: true,
        finished: false,
        para: {},
        result: [],
        total: 0
      }
    },
    components: {
      Search,
      wageItem
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
        querySalary(this.searchType).then(res => {
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
      searchObj(params) {
        this.searchType = Object.assign(this.searchType, params);
        this.searching();
      },
      onLoad() {
        this.reload();
      },
      searching() {  //重置搜索状态
        this.isReload = true;
        this.searchType.page = 1;
        this.reload();
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
