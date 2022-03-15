<template>
<div id="app">
  <el-container>
  <el-header class="header">
    <div class="logo left">
        <img class="pic_logo" src="/static/logo.png"  alt="logo" />
    </div>
    <div class="logo left">
        <span class="logo_title"><strong>SVNlog-printware</strong></span>
    </div>
    <el-menu :default-active="activeIndex" class="el-menu-demo right" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1"  @click = "getPreMsg('type1')">当天SVN统计</el-menu-item>
        <el-menu-item index="2" @click = "getPreMsg('type2')">本周SVN统计</el-menu-item>
        <el-menu-item index="3" @click = "getPreMsg('type3')">自定义SVN统计</el-menu-item>
    </el-menu>
    </el-header>

  <el-main>
<!--    <div id="svnChart" class="svnChart"></div>-->
<!--    <div id="Echarts">-->
<!--      <div id="svnChart" class="svnChart"></div>-->
<!--    </div>-->
    <dayStat> </dayStat>
  </el-main>

  <el-footer>
    <div class ="footer">
      <div class ="authorLink">
        2022 © Techinao  •  Powered by&nbsp;<a href="http://tonywang.cn" target="_blank" class="authorWebsite">TonyWang</a>
        </div>
    </div>
  </el-footer>
  </el-container>
</div>
</template>
<!--<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.11"></script>-->
<!--<script>-->
<!--    var options = {-->
<!--      stringsElement: '#typed-strings',-->
<!--      typeSpeed: 50, loop: true-->
<!--    };-->
<!--    var typed = new Typed('#typed', options);-->
<!--</script>-->
<script  type="text/javascript">
import dayStat from './components/dayStat.vue'
import weekStat from './components/weekStat.vue'
import diyStat from './components/diyStat.vue'
export default {
    name: 'Echarts',
    data() {
       return {
         activeIndex: '1',
         groupMsg:{},
      }
    },
    components:{
        dayStat,
        weekStat,
        diyStat
    },
    created(){
    },
};
</script>

<style scoped>
img{border:none;}

body{
  margin: 0;
  padding: 0;
  border: 0;
  overflow: hidden;
}
.logo{
  height: 100%;
  padding-top: 0.6%;
}
.pic_logo{
  height: 30px;
  margin-top:5%;
  margin-right:15px;
}
.logo_title{
  width: 200px;
  height: 30px;
  margin-top:50%;
  /*font-weight:lighter;*/
  font-size: 25px;
  color: #707070;
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
.svnChart{
  width: 80%;
  height:500px;
  margin:0 auto;
  margin-top:0.5%;
}
.header{
  width: 85%;
  margin: 0px auto;
  font-size: 25px;
  color: #707070;
  border-bottom-style:solid;
  border-bottom:1px ;
}
.weatherChart{
 width: 87%;
 height: 500px;
 margin:80px auto;
}
.copyright{
  margin:5px auto;
  margin-top:30px;
  color: #707070;
}
.footer{
  width: 80%;
  height: 30px;
  padding: 20px 30px 20px 280px;
  margin-top: 40px;
  margin:0px auto;
  display: inline-block;
  color: #707070;
  /*width: fit-content;*/
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
.titleBottomLine{
width:45%;
margin:5px auto;
border-bottom:2px solid #0066FF;
}
.mainTitle{
  width: 200px;
  margin:30px auto;
  font-weight:lighter;
  font-size: 50px;
  color: #707070;
  }
.box{
  height:100px;
}

.right{
  float:right;
}
.left{
  float:left;
}
</style>
