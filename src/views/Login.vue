<template>
  <div class="login">
    <div class="header-bar">{{msg}}</div>
    <div class="tit-big">建筑工地管理系统 <span class="vresion">v1.0</span></div>
    <div class="login-box">
      <div class="login-cont">
        <div class="login-tit">用户登录</div>
        <van-cell-group>
          <van-field
            v-model="LoginName"
            label="用户名:"
            placeholder="请输入用户名"
          />

          <van-field
            v-model="Password"
            type="password"
            label="密 码:"
            placeholder="请输入密码"
          />
          <van-button  size="large"  round  @click="bandLogin">登 录</van-button>
        </van-cell-group>
      </div>
    </div>
  </div>
</template>

<script>
  import {login}  from '@/api/api'
  import {Toast,Button,Field}  from 'vant'

  export default {
    name: 'Login',
    data () {
      return {
        msg: '用户登录',
        LoginName: 'admin',
        Password: '123456',
      }
    },
    methods: {

      bandLogin() {
        if(this.LoginName.length==0){
          Toast('请输入用户名!');
           return
        }
        if(this.Password.length==0){
          Toast('请输入密码!');
          return
        }

        const para = {
            LoginName: this.LoginName,
            Password: this.Password,
            logintype:'wechat'
          };

          login(para).then(res => {
             localStorage.setItem('LoginName',this.LoginName);
             localStorage.setItem('admintype',res.admintype);
             localStorage.setItem('token',res.token);
             localStorage.setItem('permission',res.permission);
             if(this.$route.query.help){
               this.$router.push({
                 path: '/Help',
               })
             }else{
               this.$router.push({
                 path: '/Main',
               });
             }
          })
        },

      },
  }
</script>


<style scoped>

  .login-box{
    margin:  0 .5rem;
    background: #fff;
    padding: 0 1rem 2rem 1rem;
    border-bottom: 1px solid #ececee;
    border-radius: .5rem;
  }
  .login-tit{
    font-size: 1.6rem;
    padding: 1.5rem 0;
  }

  .van-cell{
    padding: 8px 16px;
    border: 1px solid #ececec;
    border-radius: 3rem;
    margin-bottom: 2rem;
  }
  .van-cell::after{
    border:0;
    -webkit-transform: scale(.5);
    transform: scale(.5);
  }
  .van-button--large{
    height: 3.5rem;
    line-height:3.5rem;
    background: #83accc;
    color: #fff;
  }
</style>
