<template>
  <div class="body" style="overflow: hidden;">
    <!-- <button @click="getAllSheetData()">提交数据</button> -->
    <div class="button_row">
      <el-button type="primary" @click="getAllSheetData()">提交数据</el-button>
    </div>

    <!-- <button @click="getSpecificSheetData('sheet_1')">获取指定sheet数据</button>
    <button @click="updateSpecificSheetData('sheet_1')">更新sheet数据</button> -->
    <div id="luckysheet"></div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'LuckySheetDemo',
  data() {
    return {
      options: {
        container: 'luckysheet',
        title: '表格',
        lang: 'zh',
        showinfobar: false, // 是否显示顶部信息栏
        showtoolbar: false, // 工具栏
        showtoolbarConfig: {
          undoRedo: true, //撤销重做，注意撤消重做是两个按钮，由这一个配置决定显示还是隐藏
          paintFormat: true, //格式刷
          currencyFormat: true, //货币格式
          percentageFormat: true, //百分比格式

          moreFormats: true, // '更多格式'
          font: true, // '字体'
          fontSize: true, // '字号大小'
          bold: true, // '粗体 (Ctrl+B)'
          italic: true, // '斜体 (Ctrl+I)'
          textColor: true, // '文本颜色'
          fillColor: true, // '单元格颜色'
          mergeCell: true, // '合并单元格'
          horizontalAlignMode: true, // '水平对齐方式'
          verticalAlignMode: true, // '垂直对齐方式'
          textWrapMode: true, // '换行方式'
          function: true, // '公式'
          frozenMode: true, // '冻结方式'
          sortAndFilter: true, // '排序和筛选'
          conditionalFormat: true, // '条件格式'
          screenshot: true, // '截图'
          print: true, // '打印'

        },
        data: [],
        local_data: [
          {
            name: 'Sheet1',
            color: '',
            index: 'sheet_1',
            status: 1,
            order: 0,
            hide: 0,
            row: 36,
            column: 22,
            defaultRowHeight: 20,
            defaultColWidth: 80,
            celldata: [{
              r: 0,
              c: 0,
              v: {
                v: "标题",
                ct: { fa: "General", t: "g" },
                ff: "微软雅黑",
                fs: 16,
                bl: 1,
                m: "标题"
              }
            },
            {
              r: 1,
              c: 1,
              v: 100
            },
            {
              r: 1,
              c: 2,
              v: {
                v: new Date(),
                ct: { fa: "yyyy-MM-dd", t: "d" },
                m: "2024-01-18"
              }
            },
            {
              r: 2,
              c: 0,
              v: {
                v: "=SUM(B2:B10)",
                ct: { fa: "General", t: "g" },
                f: "=SUM(B2:B10)"
              }
            }],
            config: {
              merge: {},
              rowlen: {},
            },
          },
          {
            name: 'Sheet1',
            color: '',
            index: 'sheet_1',
            status: 1,
            order: 0,
            hide: 0,
            row: 36,
            column: 22,
            defaultRowHeight: 10,
            defaultColWidth: 50,
            celldata: [],
            config: {
              merge: {},
              rowlen: {},
            },
          }
        ],
        myFolderUrl: 'https://www.baidu.com/',

        column: 21,
        row: 36,
        scrollTop: 0,

      }
    }
  },

  methods: {

    initLuckySheet(data) {
      this.options.data = data; // 设置数据
      window.luckysheet.create(this.options);
    },

    // 将表格所有数据提交到后端
    async getAllSheetData() {
      const data = window.luckysheet.getAllSheets();
      try {
        const res = await axios({
          url: "http://192.168.255.10:6700/luckysheet/updateTabelData",
          method: "post",
          data: {
            data: data
          }
        });

        if (res.data.result == "success") {
          this.initTabelData()
          console.log("更新成功！");
        } else {
          console.log(res.data);
        }
      } catch (e) {
        console.log(e);
      }
    },

    getSpecificSheetData(sheetIndex) {
      const data = window.luckysheet.getSheetData();
      console.log(`Sheet ${sheetIndex} 的数据:`, data);
      return data;
    },

    // 更新指定sheet的数据
    updateSpecificSheetData(sheetIndex) {
      // 方法1：使用 setCellValue 更新单元格
      window.luckysheet.setCellValue(0, 1, 2332222222222);

      // 方法2：批量更新多个单元格
      const batchData = [
        { r: 2, c: 1, v: 10000 },
        { r: 2, c: 2, v: 2000000 }
      ];
      batchData.forEach(cell => {
        window.luckysheet.setCellValue(cell.r, cell.c, cell.v);
      });
    },

    // 从后端加载表格数据
    async initTabelDataByBackend() {
      try {
        const res = await axios({
          url: "http://192.168.255.10:6700/luckysheet/initTabelData",
          method: "post"
        });

        if (res.data.result == "success") {
          this.initLuckySheet(res.data.data); // 初始化 Luckysheet 并设置数据
        } else {
          console.log(res.data);
        }
      } catch (e) {
        console.log(e);
      }
    },


      // 从本地加载表格数据
  initTableData(){
    this.initLuckySheet(this.local_data);
  },
  },



  beforeUnmount() {
    window.luckysheet.destroy();
  },

  mounted() {
    // this.initTabelDataByBackend(); // 发送 POST 请求加载数据

    this.initTableData()
  },
}
</script>

<style>
.body {
  width: 100%;
  height: 100vh;
  background-color: white;
  transform: none;
}


.button_row{
  display: flex;
  justify-content: end;
  padding-top: 0.5%;
  margin-right: 2%;
  margin-bottom: 0.5%;
}

#luckysheet {
  width: 100%;
  height: 90%;
  margin: 0;
  padding: 0;
}
</style>