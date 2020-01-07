<template>
  <div>
    <headerBar fatherName="首页" currentNmae="帮助中心"></headerBar>
    <div class="pdf" v-show="fileType === 'pdf'">
      <p class="arrow">
        <span @click="changePdfPage(0)" class="turn" :class="{grey: currentPage==1}">上一页</span>
        {{currentPage}} / {{pageCount}}
        <span @click="changePdfPage(1)" class="turn" :class="{grey: currentPage==pageCount}">下一页</span>
      </p>
      <pdf style="width: 100%"
           :src="src"
           :page="currentPage"
           @num-pages="pageCount=$event"
           @page-loaded="currentPage=$event"
           @loaded="loadPdfHandler"
      >
      </pdf>
    </div>
  </div>

</template>

<script>
  import headerBar from '@/components/areas/headerBar';
  import pdf from 'vue-pdf'


  export default {
    name:'viewPdf',
    components: {
      pdf,
      headerBar
    },
    data() {
      return {
        currentPage: 0, // pdf文件页码
        pageCount: 0, // pdf文件总页数
        fileType: 'pdf', // 文件类型
        src: './static/use.pdf', // pdf文件地址
      }
    },
    created() {
      // 有时PDF文件地址会出现跨域的情况,这里最好处理一下
      this.src = pdf.createLoadingTask(this.src)
    },
    methods: {
      // 改变PDF页码,val传过来区分上一页下一页的值,0上一页,1下一页
      changePdfPage(val) {
        // console.log(val)
        if (val === 0 && this.currentPage > 1) {
          this.currentPage--
          // console.log(this.currentPage)
        }
        if (val === 1 && this.currentPage < this.pageCount) {
          this.currentPage++
          // console.log(this.currentPage)
        }
      },

      // pdf加载时
      loadPdfHandler(e) {
        this.currentPage = 1 // 加载的时候先加载第一页
      }

    }
  }

</script>

<style scoped>
  .pdf {
    margin: 0 auto;
  }

  .main {
    position: relative;
    margin: 0 auto;
    width: 50%;
    height: 800px;
    overflow: scroll;
  }
  .arrow{
    background: #fff;
    margin: 0;
    text-align: center;
    line-height: 2;
    font-size: 1.6rem;
  }
  .turn{
    color: #8eaccc;
  }
</style>
