<template>

    <el-pagination
      v-model:current-page="currentPage4"
      v-model:page-size="pageSize4"
      :page-sizes="[100, 200, 300, 400]"
      :small="small"
      :disabled="disabled"
      :background="background"
      layout="total, sizes, prev, pager, next, jumper"
      :total="400"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
</template>
<script>
export default {
    name: '',

    // 定义数据
    data() {
        return {
            currentPage4: 4,
            pageSize4:400,
            small :false,
            disabled:false,
            background:false,
        }
    },


    methods:{

        handleSizeChange(){

        },

        handleCurrentChange(){}
    }
}


</script>
  
<style scoped>
.demo-pagination-block+.demo-pagination-block {
    margin-top: 10px;
}

.demo-pagination-block .demonstration {
    margin-bottom: 16px;
}
</style>
  