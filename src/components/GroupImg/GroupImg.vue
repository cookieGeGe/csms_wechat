<template>
  <div class="imggroup" >
    <div v-for="(item,j) in groupLists">
      <van-row type="flex" justify="space-between">
        <van-col class="tits">
          {{item.name}}
        </van-col>
        <van-col>
          <van-dropdown-menu active-color="#8eaccc" >
            <van-dropdown-item v-model="valuesLists[j]" :options="item.list" @change="getPic"/>
          </van-dropdown-menu>
        </van-col>
      </van-row>
      <div class="imgBox">
        <div :style="styless[j]" >
          <div v-for="(img,index) in imgLists[j]"  @click="showImages(imgLists[j])" style="width: 15rem;float: left;margin-right: 1rem">
            <img :src="myLocalHost+img.url" /><!-- onerror="this.style.display = 'none' "-->
            <div class="van-multi-ellipsis--l2 t-center">{{img.name}}</div>
          </div>
        </div>
      </div>

      <van-image-preview
        v-model="show"
        :images="images"
        @change="onChange"
      >  <template v-slot:index>{{ imgName }}</template>
      </van-image-preview>
    </div>
  </div>
</template>
<script>
  import {queryGroupPics}  from '@/api/api'

  export default {
    name: 'GroupImg',
    data () {
      return {
        groupLists: [],
        valuesLists: [],
        imgLists: [],
        imgListsstr: '',
        styless: [],
        show:false,
        index: 0,
        images:[],
        imgList:'',
        imgName:'',
      }
    },
    props: ['groupList'],
    methods: {
      getPic(value){
        var index = this.valuesLists.indexOf(value);
        this.query(value, index)
      },
      query(value, index){
        queryGroupPics({id: value}).then(res => {
          res.group_pics.forEach((val,index,arr)=>{
              var arrs=val.purl.split('.');
              val.url=arrs[0]+'_min.'+arrs[1];
          });
          this.imgLists[index] = res.group_pics;


          this.imgListsstr = JSON.stringify(this.imgLists);
          this.styless[index] ={width:this.imgLists[index].length*16 +'rem'};
        })
      },
      push_to_values(val, index, arr) {
        if (val.list.length > 0) {
          this.valuesLists.push(val.list[0].value);
          this.query(val.list[0].value, index);
        } else {
          this.valuesLists.push(0);
        }
        this.imgLists.push([]);
         this.styless.push({width:'100%'}) ;
      },
      onChange(index) {
        this.imgName=JSON.parse(this.imgList)[index].name
      },
      showImages(imgLists){

        this.images=[];
        this.imgName=imgLists[0].name;
        this.imgList=JSON.stringify(imgLists);
        imgLists.forEach((val,index,arr)=>{
          this.images.push(this.myLocalHost+val.purl)
        });
        this.show=true;
      }
    },

    mounted(){


    },
    watch: {
      groupList: function (a, b) {
        if (a != b) {
          a.forEach(this.push_to_values);
          this.groupLists = a;
        }
      },
      imgListsstr: function (a, b) {
        this.imgLists = JSON.parse(a);
      }
    }
  }
</script>
<style scoped>
  .tits{
    font-size: 1.3rem;
    line-height: 2;
    height: 2rem;
  }
  .imggroup{
    padding:0rem 1.5rem;
  }
  .imgBox{
    width: 100%;overflow-x:scroll;
    margin: 1rem 0;
  }
  .imgBox img,
  .imgBox .van-multi-ellipsis--l2{
    width: inherit;
  }
  /deep/ .van-dropdown-menu{
    height: 2rem;
    background: transparent;
    font-size: 1.3rem;
   }
  /deep/ .van-dropdown-menu__title{
    font-size: 1.3rem;
  }
</style>

