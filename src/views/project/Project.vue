<template>
  <div class="company">
    <Search @searchObj="searchObj"></Search>
    <van-row type="flex" align="center" justify="space-between" style="margin: 10px;margin-top: 0;">
      <van-col span="9">
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.type" :options="projectTypeArr" @change="typeChange"/>
        </van-dropdown-menu>
      </van-col>
      <van-col span="9">
        <van-dropdown-menu active-color="#8eaccc" class="dropdown">
          <van-dropdown-item v-model="searchType.status" :options="projectBadArr" @change="statusChange"/>
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
      <ProjectListItem :isReload="isReload" :result="this.result"></ProjectListItem>
    </van-list>
    <!---->
  </div>
</template>

<script>
  import {projectTypeArr, projectBadArr}  from '@/utils/type'
  import {queryProject}  from '@/api/api'
  import Search  from '@/components/areas/Search'
  import SearchResult  from '@/components/areas/SearchResult'
  import ProjectListItem  from '@/components/project/ProjectListItem'


  export default {
    name: 'Project',
    data () {
      return {
        show: false,
        projectTypeArr,
        projectBadArr,
        currentDate: new Date(),
        minDate: new Date(1970, 1, 1),
        searchType: {
          time: '',
          type: 4,
          status: 4,
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
      ProjectListItem
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
        queryProject(this.searchType).then(res => {
          var ret = res.project;
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
          currentRate:0,};
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
  }

  /deep/
  .van-dropdown-menu__title {
    font-size: 1rem;
  }

  .company /deep/ .van-dropdown-item__option {
    line-height: 1rem;
    font-size: 1rem;
  }
</style>
