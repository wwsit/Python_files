<template>
    <div class="area_all">
      <div class="area1">
        <div>单选-筛选选项</div>
        <div>
  
          <el-select v-model="value" filterable placeholder="Select" style="width: 240px">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
        </div>
      </div>
  
      <div class="area2">
        <div>多选</div>
        <div>
          <el-select v-model="value2" filterable placeholder="Select" style="width: 240px" multiple clearable  collapse-tags
        collapse-tags-tooltip>
            <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value"  />
          </el-select>
        </div>
      </div>
    </div>
  
    <!-- https://element-plus.gitee.io/zh-CN/component/select.html -->
  </template>
  
  <script>
  import axios from 'axios'
  export default {
  
  
    data() {
      return {
        value: "",
        value2:"",
        options: [
          {
            value: 'Option1',
            label: '选项名1',
          },
          {
            value: 'Option2',
            label: '选项名2',
          },
          {
            value: 'Option3',
            label: '选项名3',
          },
          {
            value: 'Option4',
            label: '选项名4',
          },
          {
            value: 'Option5',
            label: '选项名5',
          },
        ],
        options2: [
          {
            value: 'Option1',
            label: '选项名1',
          },
          {
            value: 'Option2',
            label: '选项名2',
          },
          {
            value: 'Option3',
            label: '选项名3',
          },
          {
            value: 'Option4',
            label: '选项名4',
          },
          {
            value: 'Option5',
            label: '选项名5',
          },
        ]
      }
    },
  
    methods: {
  
  
    },
  
  
    mounted() {
  
    },
  
  
  }
  </script>
  
  <style lang="less">
  .area_all {
  
    margin-top: 5%;
    margin-left: 45%;
  
    .area2{
      margin-top: 5%;
    }
  }
  </style>