<template>
  <div class="view">
    <headerBar :fatherName="sources" currentNmae="项目详情"></headerBar>
    <div class="title">
        <ProjectListItem :daochu="true" :result="this.item" class="cont"></ProjectListItem>

      <div class="preson" >
        <van-row type="flex" justify="space-between">
          <van-col  span="12" style="border-right: 1px solid #ccc;">
            <div class="build">建设方</div>
            <div class="company" @click="toCompany(item.build)">{{item.buildname}}</div>
            <div>业主负责人:</div>
            <p v-html="item.ownermanager"></p>
          </van-col>
          <van-col span="12">
            <div class="build">施工方</div>
            <div  class="company" @click="toCompany(item.cons)">{{item.consname}}</div>
            <div>施工负责人:</div>
            <p v-html="item.consmanager"></p>
          </van-col>
        </van-row>
      </div>

    </div>
    <van-tabs v-model="active"
              color="#8eaccc"
              background="transparent"
              title-inactive-color="#5e5e5e"
              title-active-color="#5e5e5e"
              class="details"
              @click="changeCont"
    >
      <van-tab title="项目图片" >
        <GroupImg :groupList="groupList"></GroupImg>
      </van-tab>
      <van-tab title="项目进度">
        <Progress :progress="progress" :yearlist="year_month_info" ></Progress>
      </van-tab>
      <van-tab title="分包企业">
        <div  v-for="(subcompany,i) in item.subcompany" class="preson" style=" padding: .5rem 2rem" >
              <div class="build">分包企业{{i+1}}</div>
              <div class="company" @click="toCompany(subcompany.id)">{{subcompany.companyname}}</div>
              <div>分包负责人:</div>
              <p v-html="subcompany.person"></p>
        </div>
      </van-tab>
      <van-tab title="备注" class="description" >
        <div>备注:</div>
        <p>{{item.description}}</p>
      </van-tab>
    </van-tabs>

  </div>

</template>

<script>

  import {queryProject}  from '@/api/api'
  import GroupImg  from '@/components/GroupImg/GroupImg'
  import headerBar  from '@/components/areas/headerBar'
  import ProjectListItem  from '@/components/project/ProjectListItem'
  import Progress  from '@/views/project/Progress'
  import Vue from 'vue';
  import { ImagePreview } from 'vant';
  Vue.use(ImagePreview);

  export default {
    name: 'CompanyView',
    data () {
      return {
        id: 0,
        sources:'',
        item: {
            phone:[]
        },
        active:0,
        groupList:[],

        result:[],
        loading: false,
        finished: false,
        page:1,

        show:false,
        images:[],
        onChange:false,
        progress:{},
        year_month_info:{},
        rootArr:[]
      }
    },
    components:{
      GroupImg,
      ProjectListItem,
      Progress,
      headerBar
    },
    methods: {
      init(){
        if(!this.id) return;
        //this.id=3;
        queryProject({"id": this.id}).then(res => {
          this.item = res.project;
          this.item.ownermanager= this.item.ownermanager.replace(/,/,"<br/>");
          this.item.consmanager= this.item.consmanager.replace(/,/,"<br/>");

          this.item.subcompany.forEach((val,index)=>{
            val.person=val.person.replace(/,/,"<br/>")
          });
          this.groupList=res.pic_groups;
          this.progress=res.progress;
          this.year_month_info=res.year_month_info;
        })
      },
      changeCont(tit,name){

      },
      toCompany(id){
        this.$router.push({
          path:'/CompanyView',
          query:{
            id,
            sources:'项目详情'
          },
        });
      }
    },
    mounted(){

      this.id = this.$route.query.id;
      this.sources = this.$route.query.sources;
      this.init();
    }
  }
</script>


<style scoped>

  .title{
    padding: 1rem 1rem 0 1rem;
  }
  .cont {
    border-bottom: 1px solid #ececec;
    padding: .5rem  1rem .5rem;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 4px;
    font-size: 1.2rem;
  }

  .view .tit:first-child {
    font-size: 1.6rem;
    line-height: 1.4;
    font-weight: bold;
    color: #3c3c3c;
  }

  .contact {
    text-align: center;
    margin-top: 1rem;
    font-size: 1rem;
  }

  .contact div div {
    margin-top: .3rem;
    color: #8eaccc;
  }
  .type div{
    margin: .5rem 0;
    margin-bottom: 0;
  }
  .details{
    background: transparent;
  }
  .description{
    padding:0rem 1.5rem;
  }
  .description div{
    font-size: 1.3rem;
    line-height: 2;
    height: 2rem;
    font-weight: bold;
  }
  .description a{
    color:#8eaccc
  }

  .preson .van-col{
    padding:0 1rem;
    margin: 1rem 0;
  }
  .preson .company{
    color: #8eaccc;
    font-size: 1.4rem;
    margin-bottom: .5rem;
  }
  .preson p{
    margin: 0;
  }
  .preson .build{
    font-weight:bold;
  }
</style>
