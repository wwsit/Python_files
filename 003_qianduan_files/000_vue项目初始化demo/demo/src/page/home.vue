<template>
    <div class="homePage">
        <div>我是主页</div>
        <div>我是主页</div>
        <br>
        <div>
            <router-link to="/elementTable">表格组件</router-link>
        </div>

        <div>
            <router-link to="/elementPagination">分页功能</router-link>

        </div>

        <div>
            <router-link to="/elementTableOpen">表格展開</router-link>
        </div>

    </div>
</template>

<script>
export default {

}
</script>

<style  lange="less">
.homePage {
    margin-top: 5%;
    margin-left: 45%;
}
</style>
