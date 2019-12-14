// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vant from 'vant';
import VueScroller from "vue-scroller"

import 'vant/lib/index.css';
import './assets/reset.css'



Vue.use(VueScroller);
Vue.use(Vant);

Vue.config.productionTip = false;
Vue.prototype.myLocalHost="http://47.92.138.195:5000";
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
