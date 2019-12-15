<template>
  <div class="company">
    <Search @searchObj="searchObj"></Search>
    <van-row type="flex" align="center" justify="space-between" style="margin: 10px;margin-top: 0;">
      <van-col span="">
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.sex" :options="laborSexArr" @change="sexChange"/>
        </van-dropdown-menu>
      <!--</van-col>-->
      <!--<van-col span="5">-->
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.age" :options="laborAgeArr" @change="ageChange"/>
        </van-dropdown-menu>
      <!--</van-col>-->
      <!--<van-col span="6">-->
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.education" :options="laborEduArr" @change="eduChange"/>
        </van-dropdown-menu>
      <!--</van-col>-->
      <!--<van-col span="6">-->
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.jobtype" :options="laborJobArr" @change="jobChange"/>
        </van-dropdown-menu>
      </van-col>
    </van-row>

    <SearchResult :totals="totals"></SearchResult>
    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
      @load="onLoad"
      :immediate-check="false"
    >
      <LaborListItem :isReload="isReload" :result="this.result"></LaborListItem>
    </van-list>
    <!---->
  </div>
</template>

<script>
  import {laborSexArr, laborJobArr,laborAgeArr,laborEduArr}  from '@/utils/type'
  import {queryLabor}  from '@/api/api'
  import Search  from '@/components/areas/Search'
  import SearchResult  from '@/components/areas/SearchResult'
  import LaborListItem  from '@/components/labor/LaborListItem'


  export default {
    name: 'Labor',
    data () {
      return {
        show: false,
        laborSexArr, laborJobArr,laborAgeArr,laborEduArr,
        currentDate: new Date(),
        minDate: new Date(1970, 1, 1),
        searchType: {
          time: '',
          sex: 2,
          age: 6,
          education: 7,
          jobtype: 5,
          page: 1,
        },
        loading: false,
        isReload: true,
        finished: false,
        para: {},
        result: {},
        totals:{}
      }
    },
    components: {
      Search,
      SearchResult,
      LaborListItem
    },
    methods: {
      sexChange(value){
        this.searchType.sex = value;
        this.searching()
      },
      ageChange(value){
        this.searchType.age = value;
        this.searching()
      },
      eduChange(value){
        this.searchType.education = value;
        this.searching()
      },
      jobChange(value){
        this.searchType.jobtype = value;
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
        queryLabor(this.searchType).then(res => {
          var ret = res.labor;
          if (ret.length < 10) {
            this.finished = true;
          }
          this.isReload = false;
          this.loading = false;
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
      searching(){
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
