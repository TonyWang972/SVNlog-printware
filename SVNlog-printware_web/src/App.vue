<template>
<div id="app">
  <el-header class="header">
    <el-menu :default-active="activeIndex" class="el-menu-demo wp" mode="horizontal" @select="handleSelect">
        <div class="logo left">
          <img class="pic_logo" src="/static/logo.png"  alt="logo" />
        </div>
        <div class="logo left">
          <span class="logo_title"><strong>SVNlog-printware</strong></span>
        </div>
        <el-popover
          placement="bottom"
          title="Update SVN"
          width="50"
          trigger="hover"
          content="更新SVN文件至最新版本，可能需要等待较长时间">
          <el-button slot="reference" v-bind:icon="iconData" type="primary" circle class="updateSVN right" @click="updateSVN"></el-button>
        </el-popover>
        <el-menu-item index="3" @click = "comName='diyStat'" class="right">自定义SVN统计</el-menu-item>
        <el-menu-item index="2" @click = "comName='weekStat'" class="right">上周SVN统计</el-menu-item>
        <el-menu-item index="1" @click = "comName='dayStat'" class="right">当天SVN统计</el-menu-item>
    </el-menu>
  </el-header>
  <el-main>
        <component :is='comName'></component>
  </el-main>

  <el-footer>
      <div class ="footer">
          <div class ="authorLink">
            版权所有 2022 © Techinao  •  Powered by&nbsp;<a href="http://tonywang.cn" target="_blank" class="authorWebsite">TonyWang</a>
          </div>
      </div>
  </el-footer>
</div>
</template>

<script  type="text/javascript">
import dayStat from './pages/dayStat.vue'
import weekStat from './pages/weekStat.vue'
import diyStat from './pages/diyStat.vue'
export default {
    inject: [ 'loaded','loading'],
    name: 'Echarts',
    data() {
       return {
         activeIndex: '1',
         comName:'dayStat',
         groupMsg:{},
         iconData:'el-icon-refresh'
      }
    },
    components:{
        dayStat,
        weekStat,
        diyStat
    },
    created(){
    },
  methods: {
    buttonLoading(){
      this.iconData = 'el-icon-loading'
    },
    loaded(){
      this.iconData = 'el-icon-refresh'
    },
    updateSVN(){
      //  调用SVN更新接口
      this.buttonLoading(),
      this.$axios({
        method:'get',
        url:'/api/updateSVN',
      }).then((response) =>{          //返回promise(ES6语法)
        this.loaded(),
        this.$message({
          duration:3000,
          showClose: true,
          message: 'SVN更新完成！',
          type: 'success'
        });
      }).catch((error) =>{
        this.loaded(),
        this.$message({
          duration:3000,
          showClose: true,
          message: 'SVN更新失败！',
          type: 'error'
        });
      })
    },
    filterType(value, row){
      return row.tag === value;
    },
  },
};
</script>

<style scoped>
img{border:none;}

body{
  margin: 0;
  padding: 0;
  border: 0;
  overflow:scroll;
}
.logo{
  height: 100%;
  padding-top: 1%;
}
.pic_logo{
  height: 30px;
  margin-top:5%;
  margin-right:15px;
}
.logo_title{
  width: fit-content;
  height: 30px;
  margin-top:50%;
  /*font-weight:lighter;*/
  font-size: 25px;
  color: #707070;
}.updateSVN{
   margin-top:12px;
   margin-left:5px;
 }
.el-main{
    box-sizing: border-box;
    box-shadow: inset 0px 20px 20px -20px #707070;
    background-color: #f3f4f5;
    width: 100%;
    height: 100%;
    text-align: center;
    padding-top:2%;
    border-top-style:solid;
    border-bottom-style:solid;
    padding-bottom: 5%;
    border-color: #D0D0D0;
    border-width:1px;
    margin:0px
 }
/*.svnChart{*/
/*  width: 80%;*/
/*  height:500px;*/
/*  margin:0 auto;*/
/*  margin-top:0.5%;*/
/*}*/
.header{
  width: 100%;
  height: 80px;
}
.wp{
  width: 70%;
  margin: 0px auto;
  font-size: 25px;
  color: #707070;
  border-bottom-style:solid;
  border-bottom:1px ;
}
.footer{
  width: 80%;
  height: 30px;
  padding: 20px 30px 20px 280px;
  margin:0px auto;
  display: inline-block;
  color: #707070;
}
.authorLink{
  float: left;
  color: #909090;
  width: fit-content;
  margin:0 auto;
  font-size: 14px;
}
.authorWebsite{
  text-decoration:none;
  color: #409EFF;
}

.right{
  float:right;
}
.left{
  float:left;
}
</style>
