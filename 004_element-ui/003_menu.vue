<template>
    <!-- 
        default-active：当前激活的菜单 ；default-openeds 设置打开的目录  select 点击某个目录执行的方法
     -->
    <el-menu :default-active="active_value" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
        background-color="#1e222d" text-color="white" :default-openeds="openeds" @select="handleSelect">

        <el-sub-menu index="1">
            <template #title>
                <span>一级目录1</span>
            </template>
            <el-menu-item index="1-1" class="left_menu">二级目录1</el-menu-item>
            <el-menu-item index="1-2" class="left_menu">二级目录2</el-menu-item>
            <el-menu-item index="1-3" class="left_menu">二级目录3</el-menu-item>
        </el-sub-menu>

        <!-- disabled 设置这个目录不可点击 -->
        <el-sub-menu index="2" disabled>
            <template #title>
                <span>一级目录2</span>
            </template>
            <el-menu-item index="2-1" class="left_menu">二级目录1</el-menu-item>
            <el-menu-item index="2-2" class="left_menu">二级目录2</el-menu-item>
        </el-sub-menu>

        <el-menu-item index="3" disabled>
            <template #title>一级目录3</template>
        </el-menu-item>

    </el-menu>
</template>
  
<script>
export default {
    name: '',
    data() {
        return {

            // 一级目录1 默认是展示课状态
            openeds: ["1"],

            // 获取之前的激活状态，没有的话就打开 1-1
            active_value: sessionStorage.getItem('activeIndex') || '1-1'
        }
    },

    methods: {

        handleOpen(key, keyPath) {
            // console.log(key, keyPath)
        },

        handleClose(key, keyPath) {
            // console.log(key, keyPath)
        },

        // 点击目录要执行的方法
        handleSelect(key, keyPath) {
            // console.log(keyPath)

            if (key == "1-1") {
                this.$router.push("/")
            }
            else if (key == "1-2") {
                this.$router.push("/xxx2")
            }
            else if (key == "1-3") {
                this.$router.push("/xxx3")
            }

            // 菜单组件默认是不会记住页面刷新前激活的菜单状态的，因为在刷新页面后，应用会被重新加载，导致之前的状态数据丢失。
            // 存储之前的状态
            sessionStorage.setItem('activeIndex', key);


        }

    },

    mounted() {

        // 解决激活页面 与跳转页面 不一致的问题 
        let current_url = this.$route.path

        if (current_url == "/") {
            this.active_value = '1-1'
        }
        else if (current_url == "/xxx2") {
            this.active_value = '1-2'
        }
        else if (current_url == "/xxx3") {
            this.active_value = '1-3'
        }

    }


}
</script>
  
<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 100vh;
}

.left_menu {
    margin-left: 30px;
}
</style>
  