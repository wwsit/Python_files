<template>
    <div class="level0">

        <di>
            <span class="button1">
                <input type="checkbox">
            </span>
            <span>点击1</span>
        </di>

        <div>
            <!-- 在按钮的父级元素上 进行伪元素设置 -->
            <span class="button2">
                <input type="checkbox">
            </span>
            <span>点击2</span>

        </div>

    </div>
</template>
  
<script>

</script>
  
<style lang="less">
.level0 {

    margin-top: 5%;
    margin-left: 5%;


    .button2 {
        position: relative;
    }

    .button2 ::before {
        content: "";
        position: absolute;

        // 可以重新设置点击区域的范围
        top: 0px;
        right: -200px;
        bottom: 0px;
        left: 0px;
    }
}
</style>
