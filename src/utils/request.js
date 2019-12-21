/**
 * Created by 16288 on 2019/11/20.
 */
import axios from 'axios'
import {Toast,Dialog} from 'vant'

// 创建axios实例
const service = axios.create({
   baseURL: 'http://47.92.138.195:5000/', // api的base_url
 // baseURL: 'http://127.0.0.1:5000/', // api的base_url
  timeout: 5000 // 请求超时时间
});

// request拦截器
service.interceptors.request.use(config => {
    config.headers['token'] = localStorage.getItem('token')||''; // 让每个请求携带自定义token 请根据实际情况自行修改
  return config
}, error => {
  // Do something with request error
  Toast({message: error}); // for debug
  Promise.reject(error)
});

// respone拦截器
service.interceptors.response.use(
  response => {
    /**
     * code为非20000是抛错 可结合自己业务进行修改
     */
    const res = response.data;
    if (res.code !== 0) {
      Toast({
        message: res.msg,
      });

      // 非法的token;
      if (res.code ===  50031 || res.code === 50032 || res.code === 50033) {
        Dialog.confirm({
          title: '确定登出',
          message: '你已被登出，可以取消继续留在该页面，或者重新登录'
        }).then(() => {
          location.reload()
        })
      }
      return Promise.reject('error')
    } else {
      return response.data;
    }
  },
  error => {
    Toast({
      message: error,
    });
    return Promise.reject(error)
  }
);

export default service
