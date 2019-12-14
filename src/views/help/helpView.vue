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
      <!--</div>-->
    </div>


    <div class="card">
      <div style="padding: 0.5rem 0;font-size: 2rem;line-height: 2em;">
        问题详情
      </div>
      <div class="question-answer">
        Q: {{answer.name}}
      </div>
      <div class="answer" v-html="answer.answer">

      </div>
    </div>

    <div class="card question">
      <div class="blue-color">
        推荐的问题({{total}})
      </div>
      <!--<div>-->
      <div v-for="item in result" :value="item.id" @click="goto(item.id)">{{item.name}}</div>
    </div>

  </div>
</template>

<script>
  import {queryQuestion} from '@/api/api';
  import {Toast} from 'vant'

  export default {
    name: "helpView",
    data() {
      return {
        params: {
          id: 0,
          name: ''
        },
        query_params: {
          id: 0,
          name: ''
        },
        answer: {
          name: '',
          answer: 'A:',
        },
        value: '',
        total: 0,
        result: []
      }
    },
    methods: {
      query() {
        queryQuestion(this.params).then((res) => {
          // console.log(res)
          this.answer = res.question;
        }).catch((res) => {
          this.answer = {
            name: '',
            answer: '',
          };
          Toast({
            message: '请求失败！',
          });
        })
      },
      goto(id) {
        // console.log(id)
        this.params.id = id;
        this.query();
      },
      onSearch() {
        this.query_params.name = this.value;
        queryQuestion(this.query_params).then((res) => {
          // console.log(res)
          this.total = res.data.length;
          this.result = res.data;
        })
      }
    },
    created() {
      this.params.id = this.$route.params.id
    },
    mounted() {
      this.query()
      this.onSearch()
    }
  }
</script>

<style scoped>
  .question-answer {
    line-height: 3rem;
    font-size: 2.5rem;
    color: #a8a9aa;
  }

  /deep/ .answer img {
    margin: 10px 0;
    width: 100% !important;
    /*max-height: 5rem;*/
  }

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
    padding: 0.5rem 1rem;
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
