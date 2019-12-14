<template>
  <div class="van-content">
    <div class="card question">
      <div>
        输入要查询的问题：
      </div>
      <van-search
        v-model="value"
        placeholder="请输入搜索关键词"
        show-action
        background="#fff"
        shape="round"
        @search="onSearch"
      >
        <!--<div slot="action" @click="onSearch">搜索</div>-->
      </van-search>
      <div class="blue-color">
        推荐的问题({{total}})
      </div>
      <!--<div>-->
      <div v-for="item in result" :value="item.id" @click="goto(item.id)">{{item.name}}</div>
      <!--</div>-->
    </div>
    <div class="card phone">
      <div style="line-height: 4rem;font-size: 1.5rem">
        电话咨询
      </div>
      <div class="connect">
        <div class="icon-border">
          <van-icon style="margin: 0.5rem;" color="#fff" size="5rem" name="phone-o"/>
        </div>
        <div>
          <span>13400000000</span>
          <span>09:00-18:00(工作日)</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {queryQuestion} from '@/api/api';

  export default {
    name: "Help",
    data() {
      return {
        total: 0,
        value: '',
        result: [1, 2, 3, 4],
        params: {
          id: 0,
          name: ''
        }
      }
    },
    methods: {
      goto(id) {
        this.$router.push({
          name: 'helpView',
          params: {
            id
          },
        });
      },
      onSearch() {
        this.params.name = this.value
        queryQuestion(this.params).then((res) => {
          // console.log(res)
          this.total = res.data.length;
          this.result = res.data;
        })
      }
    },
    mounted() {
      this.onSearch();
    }
  }
</script>

<style scoped>
  /deep/ .van-search {
    background: none !important;
    padding-left: 0;
    padding: 0 0;
  }

  /deep/ .van-search .van-search__content {
    border: 1px solid #efefef;
    background: #fff;
    opacity: 1;
  }

  /deep/ .van-search .van-search__action {
    display: none;
  }

  .blue-color {
    color: #8eaccc;
  }

  .question, .question > div {
    padding: 1rem 1rem;
  }

  .phone {
    margin-top: 10px;
  }

  .icon-border {
    border: #adadad 1px solid;
    display: inline-block;
    border-radius: 50%;
    width: 6rem;
    height: 6rem;
    background: #adadad;
  }

  .connect {
    display: inline-block;
    padding-bottom: 1rem;
  }

  .connect > div:last-child {
    display: inline-block;
    vertical-align: bottom;
    height: 6rem;
    margin-left: 1rem;
  }

  .connect div span {
    display: block;
  }

  .connect div span:first-child {
    font-size: 2rem;
    line-height: 3.5rem;
  }

  .connect div span:last-child {
    font-size: 1.5rem;
  }
</style>
