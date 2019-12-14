<template>
  <div class="areastyle">
    <div class="van-search van-search--show-action" style="padding-right: 10px;">
      <div class="van-search__content van-search__content--round">
        <div class="van-search__label" @click="selectArea()">
          {{adressName}}
          <i class="van-icon van-icon-arrow-down" style="vertical-align: text-top;"><!----></i></div>

        <div class="van-cell van-cell--borderless van-field"
             style="border-left: 1px solid #ececec;padding-left: .5rem;">
          <div class="van-field__left-icon" @click="bindSearch()"><i class="van-icon van-icon-search"><!----></i></div>
          <div class="van-cell__value van-cell__value--alone">
            <div class="van-field__body"><input type="search" v-model="para.name" @search="bindSearch()" placeholder="请输入搜索关键词"
                                                class="van-field__control"></div>
          </div>
        </div>
      </div>
    </div>

    <van-popup v-model="show" position="bottom">
      <van-area :area-list="areaList" :value="value"
                @change="onChange"
                @confirm="show = false"
                @cancel="show = false"/>
    </van-popup>
  </div>


</template>

<script>
  import AreaList from '@/components/areas/myarea';
  import {queryProject, queryCompany, queryLabor}  from '@/api/api'

  export default {
    name: 'Search',
    data () {
      return {
        show: false,
        value: '230105',
        adressName: '成都',
        areaList: AreaList,
        para: {
          name: '',
          area: [],
        },
      }
    },
    methods: {
      onChange (picker, value, index) {
        this.para.area = value;
        this.value = value[value.length - 1].code;
        this.adressName = value[value.length - 1].name;
      },
      selectArea(){
        this.show = true
      },
      bindSearch(){
        this.$emit('searchObj',this.para);
      },
      init(){
        var searchParams = JSON.parse(localStorage.getItem('searchParams'));
        if(JSON.stringify(searchParams)==='{}')
            return;
        if (searchParams.name) {
          this.para.name = searchParams.name;
        }
        if (searchParams.area.length) {
          this.value = searchParams.area[searchParams.area.length - 1].code;
          this.adressName = searchParams.area[searchParams.area.length - 1].name;
          this.para.area = searchParams.area;
        }
      },
    },
    mounted(){
      this.init();
    },
  }
</script>
<style scoped>

</style>

