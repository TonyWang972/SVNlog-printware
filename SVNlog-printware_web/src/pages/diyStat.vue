<template>
  <div>
    <!--    表格-->
    <div class="tableControl">
        <div class="dateSelect">
            <el-date-picker
              v-model="value2"
              type="daterange"
              align="right"
              unlink-panels
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              :picker-options="pickerOptions">
            </el-date-picker>
          </div>
        <el-switch class="tableSwitch" active-text="显示删除" inactive-color="#A0A0A0"
                   v-model="displayDel" @change ="changeDisplayDelState()">
        </el-switch>
    </div>
    <div class="mainContent">
      <el-table class="dataTable"
                :data="tableData"
                stripe
                border
                style="width: 100%">
        <el-table-column
          prop="name"
          label="统计项"
          width="150"
          :filters="[{ text: '显示组', value: 'group' }, { text: '显示个人', value: 'user' }]"
          :filter-method="filterType">
        </el-table-column>
        <el-table-column
          prop="createCode"
          label="创建代码"
          width="100">
        </el-table-column>
        <el-table-column
          prop="createDoc"
          label="创建文档"
          width="100">
        </el-table-column>
        <el-table-column
          prop="createVideo"
          label="创建视频"
          width="100">
        </el-table-column>
        <el-table-column
          prop="createPic"
          label="创建图片"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modCode"
          label="更新代码"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modDoc"
          label="更新文档"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modPic"
          label="更新图片"
          width="100">
        </el-table-column>
        <el-table-column
          prop="modVideo"
          label="更新视频"
          width="100">
        </el-table-column>
        <el-table-column
          prop="delCode"
          label="删除代码"
          width="100"
          v-if="showColumn.delCode">
        </el-table-column>
        <el-table-column
          prop="delDoc"
          label="删除文档"
          width="100"
          v-if="showColumn.delDoc">
        </el-table-column>
        <el-table-column
          prop="delPic"
          label="删除图片"
          width="100"
          v-if="showColumn.delPic">
        </el-table-column>
        <el-table-column
          prop="delVideo"
          label="删除视频"
          width="100"
          v-if="showColumn.delVideo">
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
  name: 'Echarts',
  data() {
    return {
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
    getData(){
      this.$axios({
        method:'get',
        url:'/api/getGroupMsg',
      }).then((response) =>{          //返回promise(ES6语法)
        this.groupData=response.data
        //标记信息类型（组/个人）
        for (var val in this.groupData)
          this.groupData[val]['tag']='group';
        this.tableData=this.tableData.concat(this.groupData);
        console.log('concat:'+this.tableData.concat(this.groupData));
      }).catch((error) =>{
        console.log(error)       //请求失败返回的数据
      }),
        this.$axios({
          method:'get',
          url:'/api/getUserMsg',
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
      tableData.concat(this.groupData).concat(this.userData);
      console(tableData);
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
        console.log(response)
      }).catch((error) =>{
        console.log(error)       //请求失败返回的数据
      })
      this.$message({
        duration:3000,
        showClose: true,
        message: 'SVN更新完成！',
        type: 'success'
      });
    },
    filterType(value, row){
      return row.tag === value;
    }
  },
  mounted(){
    this.getData();
    this.displayTableData();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
.dateSelect{
  display:inline-block;
}
.tableControl{
  width: 74%;
  margin:0px auto;
}
.tableSwitch{
  margin-left:8px;
  margin-top:10px;
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
