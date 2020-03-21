// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vant from 'vant';
import VueScroller from "vue-scroller"

import 'vant/lib/index.css';
import './assets/reset.css'
import service from "./utils/request";

var base = "http://120.78.163.106:5000";

service.defaults.baseURL = base;
Vue.use(VueScroller);
Vue.use(Vant);

Vue.config.productionTip = false;
Vue.prototype.myLocalHost= base;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
