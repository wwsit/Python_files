<template>
  <div class="table_body">

      <!--
              必须加的参数
              row-key="id"   行数据key, 值需要唯一

              :tree-props="{ children: 'children', hasChildren: 'hasChildren' }"
              children ：子节点的内容，list值 [{},{} ...]
              hasChildren 可以不写，boolen值，是否有子节点内容

           -->
      <el-table :data="tableData" style="width: 50%;margin-bottom: 20px;" row-key="id" border
          :tree-props="{ children: 'children', hasChildren: 'hasChildren' }" max-height="70vh">

          <el-table-column prop="topic" label="班级" width="100px" header-align="center">
          </el-table-column>
          <el-table-column prop="score" label="分数" width="100" align="center">
          </el-table-column>
          <el-table-column prop="approve_note" label="审批备注" header-align="center">
          </el-table-column>

      </el-table>
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



          tableData: [
              { "id": "1", "topic": "1班", "score": "80", "approve_note": "xxx", "children": [{ "id": "11", "approve_note": "333" }, { "id": "12", "approve_note": "333" }] },
              { "id": "2", "topic": "2班", "score": "80", "approve_note": "xxx" },
              { "id": "3", "topic": "3班", "score": "40", "approve_note": "xxx", "children": [{ "id": "11", "approve_note": "33311" }, { "id": "12", "approve_note": "33322" }] },
              { "id": "4", "topic": "4班", "score": "80", "approve_note": "xxx" },
              { "id": "5", "topic": "5班", "score": "90", "approve_note": "xxx" },
          ],

      }
  },

  methods: {

  },




  mounted() {

  }

}
</script>

<style lange="less">
.table_body {
  margin-top: 5%;
  margin-left: 25%;
}
</style>