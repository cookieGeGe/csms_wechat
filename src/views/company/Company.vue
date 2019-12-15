<template>
  <div class="company">
    <Search @searchObj="searchObj"></Search>
    <van-row type="flex" align="center" justify="space-between" style="margin: 10px;margin-top: 0;">
      <van-col span="">
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.type" :options="companyTypeArr" @change="typeChange"/>
        </van-dropdown-menu>
      <!--</van-col>-->
      <!--<van-col span="">-->
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.status" :options="companyBadArr" @change="statusChange"/>
        </van-dropdown-menu>
      </van-col>
      <van-col @click="show=true">
        <van-tag round type="primary" color="#8eaccc" style="padding: 3px 1rem">更新时间</van-tag>
      </van-col>
    </van-row>
    <van-popup v-model="show" position="bottom">
      <van-datetime-picker
        v-model="currentDate"
        type="date"
        :min-date="minDate"
        @confirm="confirms"
        @cancel="show = false"
      />
    </van-popup>
    <SearchResult :totals="totals"></SearchResult>
    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
      @load="onLoad"
      :immediate-check="false"
    >
      <CompnayListItem :isReload="isReload" :result="this.result"></CompnayListItem>
    </van-list>
    <!---->
  </div>
</template>

<script>
  import {companyTypeArr, companyBadArr}  from '@/utils/type'
  import {queryCompany}  from '@/api/api'
  import Search  from '@/components/areas/Search'
  import SearchResult  from '@/components/areas/SearchResult'
  import CompnayListItem  from '@/components/company/CompnayListItem'


  export default {
    name: 'Company',
    data () {
      return {
        show: false,
        companyTypeArr,
        companyBadArr,
        currentDate: new Date(),
        minDate: new Date(1970, 1, 1),
        searchType: {
          time: '',
          type: 8,
          status: 0,
          page: 1,
        },
        loading: false,
        isReload: true,
        finished: false,
        para: {},
        result: {},
        totals: {},
      }
    },
    components: {
      Search,
      SearchResult,
      CompnayListItem
    },
    methods: {
      typeChange(value){
        this.searchType.type = value;
        this.searching()
      },
      statusChange(value){
        this.searchType.status = value;
        this.searching()
      },
      confirms(){
        this.searchType.time = this.currentDate;
        this.show = false;
        this.searching()
      },
      reload(){
        this.finished = false;
        this.loading = true;
        queryCompany(this.searchType).then(res => {
          var ret = res.company;
          if (ret.length < 10) {
            this.finished = true;  //是否全部加载完毕
          }
          this.isReload = false; //是否重新赋值
          this.loading = false;  //是否结束加载状态
          this.result = ret;
          this.searchType.page++;
          this.totals=res.totals;
        });
      },
      searchObj(params){
        this.searchType = Object.assign(this.searchType, params);
        this.searching();
      },
      onLoad(){
        this.reload();
      },
      searching(){  //重置搜索状态
        this.totals={total:0,
          normal:0,
          abnormal:0,
          currentrate:0,};
        this.isReload = true;
        this.searchType.page = 1;
        this.reload();
      }
    },
    created(){
      localStorage.setItem('searchParams', JSON.stringify(this.$route.params));
    },
    mounted(){
      this.searchObj(this.$route.params)
    }
  }
</script>


<style scoped>
  .company .dropdown {
    border-radius: 50rem;
    height: 2rem;
    display: inline-block;
  }

  /deep/
  .van-dropdown-menu__title {
    font-size: 1rem;
  }

  /deep/ .van-dropdown-menu__item {
    padding-right: 10px;
  }

  .company /deep/ .van-dropdown-item__option {
    line-height: 1rem;
    font-size: 1rem;
  }
</style>
