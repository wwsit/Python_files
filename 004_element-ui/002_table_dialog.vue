<template>
    <div class="clickButton">
        <button @click="openDialog">打开弹窗</button>
    </div>

    <!--  弹窗内容 -->
    <el-dialog :title=this.currentDialogTitle v-model="centerDialogVisible" width="50%" center>
        <el-table :data="DialogDataList" height="50vh">
            <el-table-column type="index" width="100" label="序号" align="center" />
            <el-table-column prop="name" label="枚举值" :formatter="forMatterLink" align="center" show-overflow-tooltip />


        </el-table>
        <div class="ErrorTip" v-if="is_show_error_tip">{{ error_msg }}</div>
        <div class="AddButton">
            <button @click="addRowData"> + 添加一行</button>
        </div>

        <!-- 底部按钮 -->
        <div class="ConfigBottom">
            <span class="button_enter">
                <el-button type="primary" @click="submitDialogData">确 定</el-button>
            </span>
            <el-button @click="centerDialogVisible = false">取 消</el-button>

        </div>
    </el-dialog>
</template>
  
<script>
export default {
    name: '',
    data() {

        return {
            is_show_error_tip:false,
            currentDialogTitle: "设置弹窗的标题",
            centerDialogVisible: false,
            DialogDataList: [{ "name": "小明" }, { "name": "小二" }, { "name": "小天" }, { "name": "小小" }]

        }
    },


    methods: {

        // 打开弹窗
        openDialog() {
            this.centerDialogVisible = true
        },

        // 关闭弹窗
        submitDialogData() {
            this.centerDialogVisible = false
        },

        // 添加一行数据
        addRowData() {

            // 添加一行空白的数据
            this.DialogDataList.push({ "name": "" },)


            this.$nextTick(() => {
                // const inputEl = this.$refs.table.$el.querySelector(`tr[data-row-key="${row.id}"] input`);
                const inputEl = document.getElementsByClassName("dialogValue")[this.DialogDataList.length - 1]
                if (inputEl) {
                    inputEl.focus();
                }
            });

        },

        //  格式化
        forMatterLink(row, column, cellValue, index) {

            // 临时保存  
            const handleBlur = (event) => {


                // 
                this.dialogCilikCellNum = this.DialogDataList.indexOf(row)  // 操作的是第几行
                const cell_value = document.getElementsByClassName("dialogValue")[this.dialogCilikCellNum].value
                this.DialogDataList[this.dialogCilikCellNum] = { "name": cell_value }  // 保存内容
                let cacheRepeatList = []
                let cacheDataList = this.DialogDataList

                // 获取重复的内容
                for (let i = 0; i < cacheDataList.length; i++) {
                    // 先全部标黑
                    document.getElementsByClassName("dialogValue")[i].style.border = "1px solid black"
                    for (let j = i + 1; j < cacheDataList.length; j++) {
                        if (cacheDataList[i].name == cacheDataList[j].name && cacheDataList[i].name) {
                            cacheRepeatList.push(i)
                            cacheRepeatList.push(j)
                        }
                    }
                }

                // 去重
                let newcacheRepeatList = [...new Set(cacheRepeatList)]

                // 标红
                if (newcacheRepeatList.length > 0) {
                    for (let i = 0; i < newcacheRepeatList.length; i++) {
                        let num = newcacheRepeatList[i]
                        document.getElementsByClassName("dialogValue")[num].style.border = "1px solid red"
                    }
                    this.is_show_error_tip = true
                    this.error_msg = "有重复的枚举值，请修改！"
                } else {
                    this.is_show_error_tip = false
                    this.error_msg = ""
                }

            }



            return <input type="text" value={cellValue} class="dialogValue" style="height: 25px;width: 50%;" onblur={handleBlur}></input>
        },



    }


}
</script>
  
<style scoped>

.clickButton button{
    margin-top: 2%;
    margin-left: 45%;
}
.element_ui_table {
    width: 80%;
    padding-top: 2%;
}


.AddButton button {
    margin-top: 2%;
    margin-bottom: 2%;
    width: 98%;
    height: 40px;
    color: #006eff;
    cursor: pointer;

}

.ErrorTip {
    color: red;
    margin-top: 2%;
    margin-left: 2%;
}




.button_enter button {
    margin-left: 40%;
    margin-right: 2%;
}
</style>