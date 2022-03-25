<template>
  <div>
    <!--    组信息可视化展示-->
    <div id="Echarts">
      <div id="svnChart" class="svnChart"></div>
    </div>
    <div class="buttonGroup">
      <el-button-group :default-active="activeIndex">
        <el-button index="1" type="primary" icon="el-icon-mouse" size="small">产品组</el-button>
        <el-button index="2" type="primary" icon="el-icon-upload" size="small">云平台组</el-button>
        <el-button index="3" type="primary" icon="el-icon-share" size="small">软件组</el-button>
        <el-button index="4" type="primary" icon="el-icon-cpu" size="small">硬件组</el-button>
      </el-button-group>
      <el-button class="updateLog"v-bind:icon="iconData" type="success" size="small" @click="updateLogByWeek()">更新周Log文件</el-button>
      <el-switch class="tableSwitch" active-text="显示删除" inactive-color="#A0A0A0" active-color="#6587ee"
                 v-model="displayDel" @change ="changeDisplayDelState()">
      </el-switch>
    </div>
    <!--    表格-->
    <div class="mainContent">
      <el-table class="dataTable"
                :data="tableData"
                stripe
                border
                style="width: 100%">
        <el-table-column
          prop="name"
          label="统计项"
          width="120"
          :filters="[{ text: '显示组', value: 'group' }, { text: '显示个人', value: 'user' }]"
          :filter-method="filterType">
        </el-table-column>
        <el-table-column
          prop="createCode"
          label="创建代码"
          width="90">
        </el-table-column>
        <el-table-column
          prop="createDoc"
          label="创建文档"
          width="90">
        </el-table-column>
        <el-table-column
          prop="createVideo"
          label="创建视频"
          width="90">
        </el-table-column>
        <el-table-column
          prop="createPic"
          label="创建图片"
          width="90">
        </el-table-column>
        <el-table-column
          prop="modCode"
          label="更新代码"
          width="90">
        </el-table-column>
        <el-table-column
          prop="modDoc"
          label="更新文档"
          width="90">
        </el-table-column>
        <el-table-column
          prop="modPic"
          label="更新图片"
          width="90">
        </el-table-column>
        <el-table-column
          prop="modVideo"
          label="更新视频"
          width="90">
        </el-table-column>
        <el-table-column
          prop="delCode"
          label="删除代码"
          width="90"
          v-if="showColumn.delCode">
        </el-table-column>
        <el-table-column
          prop="delDoc"
          label="删除文档"
          width="90"
          v-if="showColumn.delDoc">
        </el-table-column>
        <el-table-column
          prop="delPic"
          label="删除图片"
          width="90"
          v-if="showColumn.delPic">
        </el-table-column>
        <el-table-column
          prop="delVideo"
          label="删除视频"
          width="90"
          v-if="showColumn.delVideo">
        </el-table-column>
        <el-table-column
          prop="otherOperation"
          label="其他操作"
          width="90">
        </el-table-column>
      </el-table>
    </div>

    <!--    Dialog-->
    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%">
      <span>SVN更新完成！</span>
      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
  </span>
    </el-dialog>
  </div>

</template>
<script>

export default {
  inject: [ 'loaded','loading'],
  name: 'Echarts',
  data() {
    return {
      iconData:'el-icon-refresh',
      activeIndex: '1',
      tableData:[],
      groupData:[],
      userData:[],
      displayDel:true,
      dialogVisible:false,
      // 列的配置化对象，存储配置信息
      showColumn: {
        delCode: true,
        delDoc: true,
        delPic: true,
        delVideo: true,
      },

    }
  },
  methods: {
    buttonLoading(){
      this.iconData = 'el-icon-loading'
    },
    loaded(){
      this.iconData = 'el-icon-refresh'
    },
    myEcharts() {
      var myChart = this.$echarts.init(document.getElementById('svnChart'));
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: '上周工作成果统对比(Sample)'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['创建&更新代码', '创建&更新文档', '创建&更新图片', '创建&更新视频', '创建&更新视频']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['Last Mon', 'Last Tue', 'Last Wed', 'Last Thu', 'Last Fri', 'Last Sat', 'Last Sun','This Mon', 'This Tue', 'This Wed', 'This Thu', 'This Fri', 'This Sat', 'This Sun']
        },
        yAxis: {
          type: 'value',
          axisLine:{
            show:false,
          }
        },
        color:['#5470c6','#91cc75','#fac858','#ee6666','#73c0de','#3ba272','#fc8452','#fc8452','#9a60b4','#ea7ccc'],

        series: [
          {
            name: '创建&更新代码',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210,120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: '创建&更新文档',
            type: 'line',
            stack: 'Total',
            data: [220, 182, 191, 234, 290, 330, 310,120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: '创建&更新图片',
            type: 'line',
            stack: 'Total',
            data: [150, 232, 201, 154, 190, 330, 410,120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: '创建&更新视频',
            type: 'line',
            stack: 'Total',
            data: [320, 332, 301, 334, 390, 330, 320,120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: '创建&更新视频',
            type: 'line',
            stack: 'Total',
            data: [820, 932, 901, 934, 1290, 1330, 1320,120, 132, 101, 134, 90, 230, 210]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    },
    getData(){
      this.tableData=[];
      this.$axios({
        method:'get',
        url:'/api/getGroupMsg',
        params:{
          type:"week"
        }
      }).then((response) =>{          //返回promise(ES6语法)
        this.groupData=response.data
        //标记信息类型（组/个人）
        for (var val in this.groupData)
          this.groupData[val]['tag']='group';
        this.tableData=this.tableData.concat(this.groupData);
      }).catch((error) =>{
        console.log(error)       //请求失败返回的数据
      }),
        this.$axios({
          method:'get',
          url:'/api/getUserMsg',
          params:{
            type:"week"
          }
        }).then((response) =>{          //返回promise(ES6语法)
          this.userData=response.data
          //标记信息类型（组/个人）
          for (var val in this.userData)
            this.userData[val]['tag']='user';
          this.tableData=this.tableData.concat(this.userData);
        }).catch((error) =>{
          console.log(error)       //请求失败返回的数据
        })
    },
    displayTableData(){
      this.tableData=[];
      this.tableData=this.tableData.concat(this.groupData).concat(this.userData);
    },
    changeDisplayDelState(){
      for (var val in this.showColumn) {
        this.showColumn[val]=!this.showColumn[val];
      }
    },
    updateSVN(){
      //  调用SVN更新接口
      this.$axios({
        method:'post',
        url:'/api/updateSVN',
      }).then((response) =>{          //返回promise(ES6语法)
        this.getData();
        this.$message({
          duration:3000,
          showClose: true,
          message: 'SVN更新完成！',
          type: 'success'
        });
      }).catch((error) =>{
        this.$message({
          duration:3000,
          showClose: true,
          message: 'SVN更新失败！',
          type: 'error'
        });
      })

    },
    updateLogByWeek(){
      this.buttonLoading();
      this.$axios({
        method:'get',
        url:'/api/updateLogByWeek',
      }).then((response) =>{
        this.getData();
        this.tableKey++;
        this.$message({
          duration:3000,
          showClose: true,
          message: 'LOG文件更新完成！',
          type: 'success'
        });
        this.loaded();
      }).catch((error) =>{
        this.$message({
          duration:3000,
          showClose: true,
          message: 'LOG文件更新失败！',
          type: 'error'
        });
        this.loaded();
      })
    },
    filterType(value, row){
      return row.tag === value;
    }
  },
  mounted(){
    this.myEcharts();
    this.getData();
    this.displayTableData();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.svnChart{
  width: 80%;
  height:500px;
  margin:0 auto;
  margin-bottom:0.5%;
}
.mainContent{
  width:fit-content;
  margin:0.5% auto;
  margin-bottom:3%;
  text-align:center;
}
.dataTable{
  width:fit-content;
  text-align:center;
}
.tableButton{
  /*float: left;*/
  width:120px;
}

.tableSwitch{
  margin-left: 8px;
  margin-top:1px;
  /*float: left;*/
}
/*最外层透明*/
.el-table, .el-table__expanded-cell{
  background-color: transparent;
}
/* 表格内背景颜色 */
/deep/.el-table th,
/deep/.el-table tr,
/deep/.el-table td {
  background-color: transparent;
}
.left{
  float: left;
}
</style>
