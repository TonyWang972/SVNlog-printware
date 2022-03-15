<template>
  <div>
    <div class="dataTable">
      <el-table
        :data="groupData"
        stripe
        border
        style="width: 100%">
        <el-table-column
          prop="groupName"
          label="统计项"
          width="150">
        </el-table-column>
        <el-table-column
          prop="createCode"
          label="创建代码"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modCode"
          label="更新代码"
          width="100">
        </el-table-column>
        <el-table-column
          prop="createDoc"
          label="创建文档"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modDoc"
          label="更新文档"
          width="100">
        </el-table-column>
        <el-table-column
          prop="createPic"
          label="创建图片"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modPic"
          label="更新图片"
          width="100">
        </el-table-column>
        <el-table-column
          prop="createVideo"
          label="创建视频"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modVideo"
          label="更新视频"
          width="100">
        </el-table-column>
      </el-table>
    </div>
    <div id="Echarts">
      <div id="svnChart" class="svnChart"></div>
    </div>
    <div class="buttonGroup">
      <el-button-group :default-active="activeIndex">
        <el-button index="1" type="info" icon="el-icon-mouse" size="small">产品组</el-button>
        <el-button index="2" type="info" icon="el-icon-upload" size="small">云平台组</el-button>
        <el-button index="3" type="info" icon="el-icon-share" size="small">软件组</el-button>
        <el-button index="4" type="info" icon="el-icon-cpu" size="small">硬件组</el-button>
      </el-button-group>
    </div>
  </div>

</template>
<script>

export default {
  name: 'Echarts',
  data() {
    return {
      activeIndex: '1',
      groupData:[],
    }
  },
  methods: {
    myEcharts() {
      var myChart = this.$echarts.init(document.getElementById('svnChart'));
      // 指定图表的配置项和数据
      var option = {
        legend: {
        },
        tooltip: {},
        dataset: {
          source: [
            ['product', '2012', '2013'],
            ['创建代码', 86.5, 92.1],
            ['创建文档', 41.1, 30.4],
            ['创建图片', 24.1, 67.2],
            ['创建视频', 55.2, 67.1]
          ],
          // createSource: [
          //   ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
          //   ['创建代码', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
          //   ['创建文档', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
          //   ['创建图片', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
          //   ['创建视频', 55.2, 67.1, 69.2, 72.4, 53.9, 39.1]
          // ],
          // updateSource: [
          //   ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
          //   ['更新代码', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
          //   ['更新文档', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
          //   ['更新图片', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
          //   ['更新视频', 55.2, 67.1, 69.2, 72.4, 53.9, 39.1]
          // ]
        },
        color:['#ff7070','#9fe080','#5c7bd9','#ffdc60','#5c7bd9','#CC6600'],
        series: [
          {
            type: 'pie',
            radius: '50%',
            center: ['30%', '50%'],
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
              text: '主标题',
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
            center: ['70%', '50%'],
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
      this.$axios({
        method:'get',
        url:'/api/getGroupMsg',
      }).then((response) =>{          //返回promise(ES6语法)
        this.groupData=response.data
        //console.log(response)       //请求成功返回的数据
        console.log(this.groupData)
      }).catch((error) =>{
        console.log(error)       //请求失败返回的数据
      })
    }
  },
  mounted(){
    this.myEcharts();
    this.getData();
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
.dataTable{
  width:fit-content;
  margin:0.5% auto;
  margin-bottom:3%;
  text-align:center;
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
.buttonGroup{

}
</style>
