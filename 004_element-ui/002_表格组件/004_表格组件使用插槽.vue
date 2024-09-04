<template>
  <el-table :data="tableData">
   <el-table-column prop="date" label="Date"></el-table-column>
   <el-table-column prop="name" label="Name"></el-table-column>
   <el-table-column label="Tag">

    <!-- 对表单内容使用插槽 -->
    <template v-slot:default="scope">

      <!-- 可以替换成其它组件的内容 -->
     <el-tag>{{ scope.row.tag }}</el-tag>

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
  }
 }
 </script>





