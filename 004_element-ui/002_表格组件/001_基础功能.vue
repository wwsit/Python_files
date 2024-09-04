<template>
    <div class="element_ui_table">

        <!--   
            align="center" 设置内容居中； sortable 增加排序功能 ；  
            fixed固定该列；  show-overflow-tooltip 隐藏多出来的内容，悬停时使用 Tooltip 显示它们 
            cell-style 单元格的回调函数； row-style 行的回调函数
            height 设置表格的高度
        -->
        <el-table :data="tableData" :header-cell-style="HeaderCellStyle" :cell-style="CellStyle" :row-style=ListRowStyle
            height="30vh">
            <el-table-column fixed type="index" width="100" label="自动生成的序号" align="center" />
            <el-table-column fixed prop="number" label="序号" :width='"90%"' align="center" sortable />
            <el-table-column fixed prop="class" label="班级" :width='"190%"' align="center" />
            <el-table-column fixed prop="name" label="姓名" width="250" align="center" />
            <el-table-column prop="total" label="分数" :formatter="forMattertotal" width="160" align="center" sortable />
            <el-table-column prop="rank" label="排名" width="140" align="center" sortable />
            <el-table-column prop="link" label="链接地址" width="300%" align="center" show-overflow-tooltip
                :formatter="forMatterLink" />

            <el-table-column prop="notes" label="备注" width="120" align="center" show-overflow-tooltip />
            <el-table-column label="操作" fixed="right" align="center">

                <template #default="scope" align="center">
                    <el-button size="small" @click="searchData(scope)" type="primary">查看</el-button>
                    <el-button size="small" @click="tableUpdateButton(scope)" type="primary">更新</el-button>
                    <el-popconfirm width="300" confirm-button-text="确认" cancel-button-text="取消" confirm-button-type="danger"
                        cancel-button-type="success" title="确认删除这条数据" @confirm="ListHandleDelete(scope)">
                        <template #reference>
                            <el-button size="small" type="danger">删除</el-button>
                            number
                        </template>
                    </el-popconfirm>


                </template>
            </el-table-column>


        </el-table>
    </div>
</template>
  
<script>
export default {
    name: '',
    data() {

        return {

            tableData: [

                {
                    "number": 1,
                    "class": "一班",
                    "name": "小A",
                    "total": 100,
                    "rank": "1",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },
                {
                    "number": 2,
                    "class": "一班",
                    "name": "小B",
                    "total": 90,
                    "rank": "2",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },
                {
                    "number": 3,
                    "class": "一班",
                    "name": "小C",
                    "total": 80,
                    "rank": "3",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },
                {
                    "number": 4,
                    "class": "一班",
                    "name": "小D",
                    "total": 70,
                    "rank": "4",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },

                {
                    "number": 5,
                    "class": "一班",
                    "name": "小A",
                    "total": 60,
                    "rank": "5",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },
                {
                    "number": 6,
                    "class": "一班",
                    "name": "小B",
                    "total": 50,
                    "rank": "6",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },
                {
                    "number": 7,
                    "class": "一班",
                    "name": "小C",
                    "total": 40,
                    "rank": "7",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },
                {
                    "number": 8,
                    "class": "一班",
                    "name": "小D",
                    "total": 30,
                    "rank": "8",
                    "link": "https://www.baidu.com/",
                    "notes": "12345678901234567890"
                },
            ]
        }
    },


    methods: {

        // 设置表头的样式
        HeaderCellStyle(row, column, rowIndex, columnIndex) {
            return { background: '#F2F6FC', color: '#000000', fontSize: '12px' }
        },


        // 设置每一个单元格的样式
        CellStyle(row, column, rowIndex, columnIndex) {
            return { fontSize: '15px', color: "rgba(0,0,0,.9)", paddingTop: '0px', paddingBottom: '0px' }

        },

        // 格式化
        forMattertotal(row, column, cellValue, index) {
            return <span style="color: red;font-weight: bold;">{cellValue}</span>
        },

        // 格式化
        forMatterLink(row, column, cellValue, index) {
            return <a target='_blank' href={cellValue} style="text-decoration: none;color: #006eff;">{cellValue}</a>
        },

        // 查看按钮
        searchData(scope) {
            console.log(scope)  // 打印点击这一行的内容
        },


        // 删除操作
        ListHandleDelete(scope) {
            console.log(scope)
        },

        // 更新操作
        tableUpdateButton(scope) {
            console.log(scope)
        },

        // 每一行的样式
        ListRowStyle() {
            return { height: '50px' }

        },



    }


}
</script>
  
<style scoped>
.element_ui_table {
    width: 80%;
    padding-top: 2%;
}
</style>