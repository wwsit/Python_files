<template>
    
</template>
  
<script>
export default {
    methods: {
        async getUserPermission() {
            try {
                const response = await axios({
                    url: constantdict.url_prefix + "xxx",
                    method: "post",
                    data: {
                        username: this.$store.state.username
                    }
                });

                if (response.data.result === "success") {
                    this.permission_code_list = response.data.code;
                    let showPermissionPage = !this.permission_code_list.includes("001002001");
                    console.log("函数：" + showPermissionPage);
                    return showPermissionPage  // 返回 showPermissionPage 的值

                } else if (response.data.result === "error") {
                    console.log(response.data.info);
                }
            } catch (error) {
                pageTips(error.response.data.info);
            }
        }
    },




    async mounted() {
        try {
            // 打印返回的值
            // let receive_showPermissionPage = await this.getUserPermission();
            // console.log(receive_showPermissionPage)

            // 执行完getUserPermission函数，并获取到值，程序才会继续往下走
            await this.getUserPermission();
            if (this.showPermissionPage) {
                console.log(11)
            }
            else {
                console.log(222)
            }
        } catch (error) {
            console.log(error);
        }
    }

}

