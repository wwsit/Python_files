
<template>
    <div class="toolbar">

        <div>开发1</div>
        <div>开发2</div>
        <div>开发3</div>
        <div>开发4</div>

    </div>
</template>

<script>
export default {
    name: '',
    data() {
        return {

        }
    },

    methods: {


    }
}
</script>

<style lang="less">
@back_color: pink;


@media (width: 414px) {

    /* 设置根元素的字体大小 */
    html {
        // font-size: 10px;
        font-size: 1px;
    }
}

@media (width: 1920px) {
    html {
        font-size: 2px;
    }
}




.toolbar {

    background-color: pink  ;
    // height: 5rem;  // rem 相对单位
    height: (50 / 1rem); // 设置的相对单位 = 实际高度/根元素大小
    width: 100%;
    left: 0;
    bottom: 0;
    position: fixed;
    display: flex;
    justify-content: space-around
}
</style>