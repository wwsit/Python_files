<template>
    <div class="level0">

        <div class="level1">
            <div>元素1</div>
            <div>元素2</div>
        </div>

        <div class="level2">
            <div>元素3</div>
        </div>
    </div>
</template>
  
<script>

</script>
  
<style lang="less">

.level0 {
    display: flex;

    justify-content: space-between;  // 让元素在两端对齐

    .level1 { 
        display: flex;
    }

    .level2 {
        display: flex;
    }
}
</style>
  