<template>
  <div class="view">
    <div class="title">
      <div class="cont">
        <van-row class="tit" type="flex" align="center" justify="space-between">
          <van-col>{{item.name}}</van-col>
          <van-col span="4" style="text-align: right">
            <van-tag color="#8ec5cc" v-if="item.hasbadrecord <=1">{{companyBad(item.hasbadrecord)}}</van-tag>
            <van-tag color="#d9aa60" v-else>{{companyBad(item.hasbadrecord)}}</van-tag>
          </van-col>
        </van-row>
        <van-row type="flex" align="center" justify="space-between">
          <van-col span="20" class="type">
            <div>企业类型: <van-tag color="#8eaccc">{{companyType(item.type)}}</van-tag></div>
            <div>所属地区: {{item.provinceid}}{{item.cityid}}{{item.districtid}}</div>
            <div >办公地址: {{item.address}}</div>
          </van-col>
          <van-col span="4" style="text-align: right">
            <van-tag color="#8eaccc" @click="file">导出</van-tag>
          </van-col>
        </van-row>
        <van-row class="contact" type="flex" align="center" justify="space-between">
          <van-col span="6" style="border-right: 1px solid #888888">
            企业负责人 <div>{{item.legal}}</div>
          </van-col>
          <van-col class="van-ellipsis">
            联系方式 <div v-html="contact(item.phone)"></div>
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
      <van-tab title="公司图片" >
        <GroupImg :groupList="groupList"></GroupImg>
      </van-tab>
      <van-tab title="相关项目">
        <van-list
          v-model="loading"
          :finished="finished"
          finished-text="没有更多了"
          :immediate-check="false"
        >
          <ProjectListItem  :result="this.result"></ProjectListItem>
        </van-list>
      </van-tab>
      <van-tab title="备注信息" class="description">
        <div>备注:</div>
        <p>{{item.description}}</p>
        <div>其他信息:</div>
        <p>{{item.otherinfo}}</p>
      </van-tab>
      <van-tab title="资质及文件" class="description" >
        <div>资质文件:</div>
        <p><img :src="myLocalHost+item.license" alt="" width="100%" @click="previewshow()"></p>
        <div>其他文件:</div>
        <p v-for="other in item.other_file_list"><a  :href="myLocalHost+other.filepath" :download="other.filename">{{other.filename}}</a></p>
      </van-tab>
    </van-tabs>


  </div>

</template>

<script>

  import {queryCompany,queryCompanyProject}  from '@/api/api'
  import {companyBad, companyType, contact}  from '@/utils/type'
  import GroupImg  from '@/components/GroupImg/GroupImg'
  import ProjectListItem  from '@/components/project/ProjectListItem'
  import Vue from 'vue';
  import { ImagePreview } from 'vant';
  Vue.use(ImagePreview);

  export default {
    name: 'CompanyView',
    data () {
      return {
        companyBad,
        companyType,
        contact,
        id: 0,
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
      }
    },
    components:{
      GroupImg,
      ProjectListItem
    },
    methods: {
      init(){
        if(!this.id) return;
        queryCompany({"id": this.id}).then(res => {
          this.item = res.company;
          this.groupList=res.pic_groups;
        })
      },
      changeCont(name,tit){
        if(tit==='相关项目'){
          this.loading = true;
          queryCompanyProject({page:this.page,id:this.id}).then(res => {
            var ret = res.data;
            if (ret.length < 10) {
              this.finished = true;  //是否全部加载完毕
            }
            this.loading = false;  //是否结束加载状态
            this.result = ret;
            this.page++;
          });
        }
      },
      previewshow(){
        ImagePreview([
          this.myLocalHost+this.item.license,
        ]);
      },
      file(){
        var href=this.myLocalHost+'/template/export?type=word&ft=company&id='+this.item.id;
        window.open(href,this.item.name);
      }
    },
    mounted(){
      this.id = this.$route.query.id;
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
    background: rgba(255, 255, 255, 0.77);
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
</style>
