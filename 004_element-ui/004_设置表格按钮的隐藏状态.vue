<template>
    <el-table :data="tableData" style="width: 100%">
        <el-table-column fixed prop="date" label="Date" width="150" />
        <el-table-column fixed="right" label="Operations">
            <template #default>
                <!-- 通过函数的形式设置按钮 是否禁用  ps: 通过变量绑定的形式去调用函数的使用需要加括号 -->
                <el-button link type="primary" size="small" :disabled="checkPermission()">编辑</el-button>

                <el-popconfirm width="300" confirm-button-text="确认" cancel-button-text="取消" confirm-button-type="danger"
                    cancel-button-type="success" title="确认删除这条数据" v-if="show_delete_button">
                    <!-- 如果想隐藏删除按钮，v-if 需要放在最外层 -->
                    <template #reference>
                        <el-button size="small" type="danger">删除</el-button>
                    </template>
                </el-popconfirm>
            </template>

        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: '',
    data() {
        return {
            tableData: [
                {
                    date: '2016-05-03',

                },
                {
                    date: '2016-05-01',

                },
            ],

            show_delete_button: false


        }
    },

    methods: {

        checkPermission() {

            // 返回true，按钮禁言
            // 返回false，按钮可以点击
            return true
        }
    }
}
</script>

<style scoped></style>