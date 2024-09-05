<template>
    <el-table :data="tableData">
        <el-table-column prop="date" label="Date"></el-table-column>
        <el-table-column prop="name" label="Name"></el-table-column>


        <el-table-column label="自定义单元格内容">

            <!-- 对表单内容使用插槽 -->
            <template v-slot:default="scope">

                <!-- 根据条件设置不同的样式 -->
                <el-tag type="success" effect="dark" v-if="scope.row.tag == 'Cool'">{{ scope.row.tag }}</el-tag>
                <el-tag type="primary" effect="dark" v-else>{{ scope.row.tag }}</el-tag>

            </template>

        </el-table-column>



        <el-table-column prop="header">

            <template #header>

                <div class="top_area">
                    <span class="title">自定义头部样式</span>
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




        <el-table-column label="操作" fixed="right" align="center">

            <template #default="scope" align="center">
                <el-button size="small" type="primary">添加</el-button>
                <el-popconfirm width="300" confirm-button-text="确认" cancel-button-text="取消" confirm-button-type="danger"
                    cancel-button-type="success" title="确认删除这条数据" @confirm="fundRemoveButton(scope)">
                    <template #reference>
                        <el-button size="small" type="danger">移除</el-button>
                    </template>
                </el-popconfirm>


            </template>
        </el-table-column>




    </el-table>
</template>

<script>
export default {
    data() {
        return {
            tableData: [{
                date: '2016-05-03',
                name: 'Tom',
                tag: 'Cool'
            }, {
                date: '2016-05-02',
                name: 'Jerry',
                tag: 'Nice'
            }, {
                date: '2016-05-04',
                name: 'John',
                tag: 'Great'
            }]
        }
    },


    methods: {


        addCategorizeName() {

            console.log("点击添加按钮")
        },


    }



}
</script>

