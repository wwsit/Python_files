<template>
    <div class="table_body">

        <div class="leftTable">

            <!-- 

              cell-mouse-enter: 鼠标悬浮在单元格上执行的方法
              cell-mouse-leave：鼠标离开单元格上后执行的方法
              cell-click: 点击单元格要执行的方法

              ref解释：
              ref 是一种特殊的属性，用于给元素或组件注册引用信息。通过使用 ref，您可以在组件中访问具有该引用的元素或组件实例。
              当您在Vue组件中使用 ref 属性时，可以通过 this.$refs 来访问注册了引用的元素或组件。
              在您的代码中，通过 this.$refs.table，您可以访问到包含了 <el-table> 元素的实例，可以通过这个引用来操作表格的属性、方法或直接访问 DOM 元素。

              # header 设置表头的样式
           -->


            <el-table :data="tableData" style="width: 40%;" border :header-cell-style="HeaderCellStyle"
                :row-style=ListRowStyle @cell-mouse-enter="handleCellMouseEnter"
                @cell-mouse-leave="handleCellMouseLeave" @cell-click="cellClick" ref="table">

                <el-table-column prop="data">

                    <template #header>
                        <div class="top_area">
                            <span class="title">数据分组</span>
                            <span class="table_header">

                                <el-button key="primary" type="primary" link @click="addCategorizeName">

                                    <el-icon>
                                        <Plus />
                                    </el-icon>
                                    添加分组
                                </el-button>
                            </span>

                        </div>
                    </template>
                </el-table-column>

            </el-table>
        </div>


    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: '',
    components: {
    },

    data() {
        return {

            selectedCell: null,

            tableData: [


                { "data": "测试" },
                { "data": "开发" },
                { "data": "生产" },
                { "data": "预发布" },
            ],

        }
    },

    methods: {


        // 设置表头的样式
        HeaderCellStyle(row, column, rowIndex, columnIndex) {
            return {
                'background': '#F2F6FC',
                'color': '#000000',
                'font-size': '20px',
                // 'padding-top': '5%',
                'padding-bottom': '2%',
                'font-weight': 'bold'
            }
        },

        // 每一行的样式
        ListRowStyle(row, rowIndex) {
            return { background: '#f1f2f5', color: '#000000', fontSize: '15px' }
        },

        // 当单元格 hover 进入时会触发该事件
        handleCellMouseEnter(row, column, cell) {
            cell.style.backgroundColor = '#a3ccff';
            // cell.style.color = 'white';
        },

        handleCellMouseLeave(row, column, cell) {
            cell.style.backgroundColor = '';
        },

        // 点击单元格
        cellClick(row, column, cell, event) {

            if (this.selectedCell) {

                // 删除原来的样式
                this.selectedCell.classList.remove('highlighted-cell');
            }


            // 添加class值
            cell.classList.add('highlighted-cell');

            // 进行记录
            this.selectedCell = cell;


        },


        setCellhighlight() {

            if (this.selectedCell) {
                // 删除原有的高亮值
                this.selectedCell.classList.remove('highlighted-cell');
            }

            // 默认给第一个单元格设置高亮，获取第一个单元格元素
            // const firstCell = this.$refs.table.$el.querySelector('tr');
            const firstCell = this.$refs.table.$el.querySelector('.el-table__body-wrapper tbody tr ');

            if (firstCell) {

                // 加上高亮的标签
                firstCell.classList.add('highlighted-cell');
                this.selectedCell = firstCell;
            }
        },


        addCategorizeName() {
            console.log("点击添加分组按钮之后，进行的操作")
        }






    },




    mounted() {

        this.setCellhighlight()
    }

}
</script>

<style lange="less">
.table_body {
    margin-top: 5%;
    margin-left: 25%;


    /* 高亮标签的样式 */
    .highlighted-cell {
        background-color: #a3ccff !important;
    }

}
</style>