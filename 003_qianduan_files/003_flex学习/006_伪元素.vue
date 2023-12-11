<template>
    <div class="level0">

        <di>
            <span class="button1">
                <input type="checkbox">
            </span>
            <span>点击1</span>
        </di>

        <div>
            <span class="button2">
                <input type="checkbox">
            </span>
            <span>点击2</span>

        </div>

        <label>
            <span class="button1">
                <input type="checkbox">
            </span>
            <span>点击1-使用label标签也可以实现同样的效果</span>
        </label>


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
        top: 0px;
        right: -200px;
        bottom: 0px;
        left: 0px;
    }
}
</style>
