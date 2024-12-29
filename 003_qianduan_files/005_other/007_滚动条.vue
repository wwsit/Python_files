<template>
  
    <div class="level0">

        <div>内容1</div>
        <div>内容2</div>
        <div>内容3</div>
        <div>内容4</div>
        <div>内容5</div>
        <div></div>
        <div>内容1</div>
        <div>内容2</div>
        <div>内容3</div>
        <div>内容4</div>
        <div>内容5</div>


    </div>

</template>
  
<script>

</script>
  
<style lang="less">


    .level0{
        height: 100px;     // 当内容的高度超过 100px，就会显示垂直滚动条
        overflow-y: auto;  // 只想显示垂直方向的滚动条

        // overflow: auto;   // 给内容的父级添加滚动属性
        // overflow-y: auto;  // 只想显示垂直方向的滚动条
        // overflow-x  auto;   // 只想显示水平方向的滚动条
    }
</style>
  