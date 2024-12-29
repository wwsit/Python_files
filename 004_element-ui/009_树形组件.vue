<template>
    <!-- 
           default-expanded-keys 置默认展开的节点。 需要注意的是，此时必须设置 node-key
  
     -->
  
    <el-tree :data="treeData" :props="defaultProps" :default-expanded-keys="[0, 1]" node-key="id"
      @node-click="handleNodeClick">
  
      <!-- 使用插槽，进行节点内容自定义 -->
      <template v-slot="{ node, data }">
        <span>
          <span>{{ data.label }}</span>
          <el-button type="text" @click="handleDelete(data, $event)">Delete</el-button>
        </span>
      </template>
    </el-tree>
  </template>
  
  <script>
  export default {
    data() {
      return {
        treeData: [
          {
            id: 0,
            label: '一级目录1',
            children: [
              { label: '二级目录 1', id: "0-1", children: [{ label: '三级目录 1' }, { label: '三级目录 2' }] },
              { label: '二级目录 2' }
            ]
          },
          {
            id: 1,
            label: '一级目录2',
            children: [
              { label: '二级目录 3' },
              { label: '二级目录 4' }
            ]
          },
          {
            id: 2,
            label: '一级目录3',
  
          }
        ],
  
        defaultProps: {
          children: 'children',
          label: 'label'
        }
      };
    },
    methods: {
  
      // 点击删除按钮
      handleDelete(data, event) {
  
        // 阻止事件冒泡，不展开子节点
        event.stopPropagation();
  
        // 处理删除节点的逻辑
        console.log('Delete node:', data);
      },
  
  
      // 点击某个节点
      handleNodeClick(data) {
        console.log(data)
      }
    }
  };
  </script>