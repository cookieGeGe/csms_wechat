<template>
  <div class="imggroup" >
    <div v-for="(item,j) in groupLists">
      <van-row type="flex" justify="space-between">
        <van-col class="tits">
          {{item.name}}
        </van-col>
      </van-row>
      <div class="imgBox">
        <div :style="styless[j]"  @click="showImages(item.list)">
          <div v-for="(img,index) in item.list"  style="width: 15rem;float: left;margin-right: 1rem">
            <img :src="minSrc(img.purl)" />
            <div class="van-multi-ellipsis--l2 t-center">{{img.text}}</div>
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
  export default {
    name: 'ProgressImg',
    data () {
      return {
        groupLists:[],
        styless:[],
        show:false,
        index: 0,
        images:[],
        imgList:'',
        imgName:'',
      }
    },
    props: ['groupList'],
    methods: {

      push_to_values(val, index, arr) {
        if(JSON.stringify(val.list)!=='[]'){
          this.groupLists.push(val);
          this.styless.push({width:val.list.length*16 +'rem'});
        }
      },
      minSrc(src){
        var arrs=src.split('.');
        return this.myLocalHost+arrs[0]+'_min.'+arrs[1];
      },
      onChange(index) {
        this.imgName=JSON.parse(this.imgList)[index].text
      },
      showImages(imgLists){
        this.images=[];
        this.imgName=imgLists[0].text;
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
            this.groupLists=[];
            this.styless=[];
          a.forEach(this.push_to_values);
        }
      },
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
    padding-right:.5rem;
  }
  .imgBox{
    width: 100%;overflow-x:scroll;
    margin: 1rem 0;
  }
  .imgBox img,
  .imgBox .van-multi-ellipsis--l2{
    width: inherit;
  }
  .imgBox img{
    max-height: 18rem;
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

