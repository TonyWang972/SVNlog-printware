<template>
  <div>
<!-- 组信息可视化展示-->
    <div id="Echarts">
       <div id="svnChart" class="svnChart"></div>
    </div>
    <div class="buttonGroup">
      <el-button-group :default-active="activeIndex" >
        <el-button index="1" type="primary" icon="el-icon-mouse" size="small" @click="updateLog()">产品组</el-button>
        <el-button index="2" type="primary" icon="el-icon-upload" size="small">云平台组</el-button>
        <el-button index="3" type="primary" icon="el-icon-share" size="small">软件组</el-button>
        <el-button index="4" type="primary" icon="el-icon-cpu" size="small">硬件组</el-button>
      </el-button-group>
      <el-button class="updateLog"v-bind:icon="iconData" type="success" size="small" @click="updateLogByDay()">更新日Log文件</el-button>
      <el-switch class="tableSwitch" active-text="显示删除" inactive-color="#A0A0A0" active-color="#6587ee"
                 v-model="displayDel" @change ="changeDisplayDelState()">
      </el-switch>
    </div>
<!--    表格-->
    <div class="mainContent">
      <el-table class="dataTable"
                :key="tableKey"
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
        width="30%"
        :before-close="handleClose">
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
      tableKey:0,
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
        legend: {
        },
        tooltip: {},
        title: [
          {
            subtext: '代码',
            left: '25%',
            top: '80%',
            textAlign: 'center',
            subtextStyle:{
              color:'#505050',
              fontSize:16
            }
          },
          {
            subtext: '文档',
            left: '50%',
            top: '80%',
            textAlign: 'center',
            subtextStyle:{
              color:'#505050',
              fontSize:16
            }
          },
          {
            subtext: '图片&视频',
            left: '75%',
            top: '80%',
            textAlign: 'center',
            subtextStyle:{
              color:'#505050',
              fontSize:16
            }
          }
        ],
        dataset: {
          //要设的值
          source: [
            ['product', '2012', '2013'],
            ['创建', 86.5, 92.1, 92.1],
            ['修改', 41.1, 30.4, 30.4],
            ['删除', 24.1, 67.2, 67.2],
            ['添加', 55.2, 67.1, 67.1]
          ],
        },
        color:['#ff7070','#9fe080','#5c7bd9','#ffdc60','#5c7bd9','#CC6600'],
        series: [
          {
            type: 'pie',
            radius: '50%',
            center: ['25%', '50%'],
            itemStyle: {
              normal: {
                label: {
                  textStyle: {
                    color:'black',
                    fontSize: 14,
                  }
                }
              }
            },
            title : {
              show:true,
              text: '代码',
              textStyle:{
                color:'#ccc',//'red'，字体颜色
                fontStyle:'normal',//'italic'(倾斜) | 'oblique'(倾斜体) ，字体风格
                fontWeight:'normal',//'bold'(粗体) | 'bolder'(粗体) | 'lighter'(正常粗细) ，字体粗细
                fontFamily:'sans-serif',//'sans-serif' | 'serif' | 'monospace' | 'Arial' | 'Courier New'
                // 'Microsoft YaHei'(微软雅黑) ，文字字体
                fontSize:18,//字体大小
                lineHeight:18,//字体行高
              },
            }
          },
          {
            type: 'pie',
            radius: '50%',
            center: ['50%', '50%'],
            itemStyle: {
              normal: {
                label: {
                  textStyle: {
                    color:'black',
                    fontSize: 14,
                  }
                }
              }
            },
            encode: {
              itemName: 'product',
              value: '2013'
            }
          },
          {
            type: 'pie',
            radius: '50%',
            center: ['75%', '50%'],
            itemStyle: {
              normal: {
                label: {
                  textStyle: {
                    color:'black',
                    fontSize: 14,
                  }
                }
              }
            },
            encode: {
              itemName: 'product',
              value: '2013'
            }
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
          type:"day"
        }
      }).then((response) =>{          //返回promise(ES6语法)
        this.groupData=response.data
        //标记信息类型（组/个人）
        for (var val in this.groupData)
          this.groupData[val]['tag']='group';
        this.tableData=this.tableData.concat(this.groupData);
        /*
        *在这里可以导数据至Echarts
         */
      }).catch((error) =>{
        console.log(error)       //请求失败返回的数据
      }),
      this.$axios({
        method:'get',
        url:'/api/getUserMsg',
        params:{
          type:"day"
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
      tableData.concat(this.groupData).concat(this.userData);
    },
    changeDisplayDelState(){
      for (var val in this.showColumn) {
        this.showColumn[val]=!this.showColumn[val];
      }
    },
    updateLogByDay(){
      this.buttonLoading();
      this.$axios({
        method:'get',
        url:'/api/updateLogByDay',
      }).then((response) =>{          //返回promise(ES6语法)
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

    // updateLog(){
    //   this.buttonLoading();
    //   //  调用SVN更新接口
    //   var myDate = new Date();
    //   var year=myDate.getFullYear();    //获取完整的年份(4位,1970-????)
    //   var month=myDate.getMonth();       //获取当前月份(0-11,0代表1月)
    //   var day = myDate.getDate();        //获取当前日(1-31)
    //   var time1 = year+'-'+month+'-'+day;
    //
    //   var tomorrowDate = new Date();
    //   tomorrowDate.setTime(tomorrowDate.getTime()+24*60*60*1000);
    //   year=tomorrowDate.getFullYear();    //获取完整的年份(4位,1970-????)
    //   month=tomorrowDate.getMonth();       //获取当前月份(0-11,0代表1月)
    //   day = tomorrowDate.getDate();        //获取当前日(1-31)
    //   var time2 = year+'-'+month+'-'+day;
    //   console.log(time1)
    //   console.log(time2)
    //
    //   this.$axios({
    //     method:'post',
    //     url:'/api/updateLog',
    //     data:{
    //       startTime: time1,
    //       endTime: time2
    //     }
    //   }).then((response) =>{          //返回promise(ES6语法)
    //     this.$message({
    //       duration:3000,
    //       showClose: true,
    //       message: 'LOG文件更新完成！',
    //       type: 'success'
    //     });
    //     this.loaded();
    //   }).catch((error) =>{
    //     this.$message({
    //       duration:3000,
    //       showClose: true,
    //       message: 'LOG文件更新失败！',
    //       type: 'error'
    //     });
    //     this.loaded();
    //   })
    // },
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
  height:300px;
  margin:0 auto;
  margin-top:0.5%;
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
.buttonGroup{
  margin-bottom:1%;
}
.updateLog{
  margin-left: 10px;
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
