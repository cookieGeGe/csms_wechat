<template>
  <div class="view">
    <div class="title">
      <div class="cont">
          <LaborListItem  :result="this.item" ></LaborListItem>
          <van-row  class="guanlyuan" type="flex" justify="space-around">
          <van-col>
            <van-tag color="#8eaccc" v-if="item.ispm==1">项目管理员</van-tag>
            <van-tag color="#888" v-else>非项目管理员</van-tag>
            <van-tag color="#8eaccc" v-if="item.isleader==1">班组长</van-tag>
            <van-tag color="#888" v-else>非班组长</van-tag>
            <van-tag color="#8eaccc" >所属班组:{{item.classname}}</van-tag>
          </van-col>
          <van-col>
            安全帽号: <van-tag color="#8ec5cc" >{{item.hardhatnum||'00000'}}</van-tag>
          </van-col>
        </van-row>
      </div>
      <div class="list">
        <div class="ablock">
          <van-row type="flex" justify="space-between" align="center">
            <van-col>
              手机号:<b>{{item.phone}}</b> <van-icon name="phone-o" color="#8ec5cc" size="1rem"/>
            </van-col>
            <van-col>
              紧急联系号:<b>{{item.emercon}}</b> <van-icon name="phone-o" color="#8ec5cc" size="1rem"/>
            </van-col>
          </van-row>
          <div>
            家庭地址:{{item.address}}
          </div>
          <van-row>
            <van-col span="8">
              文化程度:<span>{{laborEdu(item.education)}}</span>
            </van-col>
            <van-col>
              工资标准:<span>{{item.isfeestand?'临时工':'合同工'}} {{item.feestand}}</span>
            </van-col>
          </van-row>
          <van-row>
            <van-col span="8">
               是否不良: <van-tag color="#8eaccc" v-if="item.isbadrecord==0">否</van-tag>
               <van-tag color="#d9aa60" v-else="item.isbadrecord==1">不良</van-tag>
               <van-tag color="#d9aa60" v-if="item.isbadrecord==2">黑名单</van-tag>
            </van-col>
            <van-col>
              是否培训:<span>{{item.train?'是':'否'}}</span>
            </van-col>
          </van-row>
        </div>
        <div class="ablock">
          <div>
            身份证号:{{item.idcard}}
          </div>
          <div>
            发证机关:{{item.ssueAauth}}
          </div>
          <div class="imgBox">
            <div style="width: 64rem" >
              <div  @click="previewshow(item.closeupphoto)" style="width: 15rem;float: left;margin-right: 1rem">
                <img v-if="item.idp!=''" :src="myLocalHost+item.idp" />
                <img v-else src="../../assets/index/no_pic.jpg" alt="">
                <div class="van-multi-ellipsis--l2 t-center">身份证正面</div>
              </div>
              <div  @click="previewshow(item.closeupphoto)" style="width: 15rem;float: left;margin-right: 1rem">
                <img v-if="item.idb!=''" :src="myLocalHost+item.idb" />
                <img v-else src="../../assets/index/no_pic.jpg" alt="">
                <div class="van-multi-ellipsis--l2 t-center">身份证背面</div>
              </div>
              <div  @click="previewshow(item.closeupphoto)" style="width: 15rem;float: left;margin-right: 1rem">
                <img v-if="item.closeupphoto!=''" :src="myLocalHost+item.closeupphoto" />
                <img v-else src="../../assets/index/no_pic.jpg" alt="">
                <div class="van-multi-ellipsis--l2 t-center">近身照片</div>
              </div>
              <div  @click="previewshow(item.trainpic)" style="width: 15rem;float: left;margin-right: 1rem">
                <img v-if="item.trainpic&&item.trainpic!=''" :src="myLocalHost+item.trainpic" />
                <img v-else src="../../assets/index/no_pic.jpg" alt="">
                <div class="van-multi-ellipsis--l2 t-center">培训图片</div>
              </div>
            </div>
          </div>
        </div>
        <div class="ablock">
          <van-tabs v-model="active"
                    color="#8eaccc"
                    background="transparent"
                    title-inactive-color="#5e5e5e"
                    title-active-color="#5e5e5e"
                    class="details"
                    @click="changeCont"
          >
            <van-tab title="分组图片" >
              <GroupImg :groupList="groupList"></GroupImg>
            </van-tab>
            <van-tab title="备注信息">
              <p>{{item.remark}}</p>
            </van-tab>
            <van-tab title="不良信息">
              <p>{{item.badrecord}}</p>
            </van-tab>
          </van-tabs>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import {queryLabor}  from '@/api/api'
  import {laborEdu}  from '@/utils/type'
  import LaborListItem  from '@/components/labor/LaborListItem'
  import GroupImg  from '@/components/GroupImg/GroupImg'
  import Vue from 'vue';
  import { ImagePreview } from 'vant';
  Vue.use(ImagePreview);

  export default {
    name: 'LaborView',
    data () {
      return {
        laborEdu,
        id: 0,
        item: {

        },
        active:0,
        groupList:[]
      }
    },
    components:{
      GroupImg,
      LaborListItem
    },
    methods: {
      init(){
        if(!this.id) return;
        //this.id=55;
        queryLabor({"id": this.id}).then(res => {
          this.item = res.labor;
          this.groupList=res.pic_groups;
        })
      },

      previewshow(src){
          if(src!=''){
            ImagePreview([
              this.myLocalHost+src,
            ]);
          }
      },
      /*file(){
        var href=this.myLocalHost+'/template/export?type=word&ft=company&id='+this.item.id;
        window.open(href,this.item.name);
      }*/
    },
    mounted(){
      this.id = this.$route.params.id;
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
    background: rgba(255, 255, 255, 0.77);
    border-radius: 4px;
    font-size: 1.2rem;
  }
  .list{
    background: #fff;
    margin-top: 1rem;
    border-radius: 4px;
    color: #888;
  }
  .ablock{
    padding: 1rem .5rem;
    line-height: 2rem;
    border-bottom: 1px solid #ececec;
  }
  .guanlyuan{
    border-top:1px solid #ccc;
    padding: .5rem 0;
  }

  .imgBox{
    width: 100%;overflow-x:scroll;
    margin: 1rem 0;
  }
  .imgBox img{
    max-height: 18rem;
  }
  .imgBox img,
  .imgBox .van-multi-ellipsis--l2{
    width: inherit;
  }
</style>
