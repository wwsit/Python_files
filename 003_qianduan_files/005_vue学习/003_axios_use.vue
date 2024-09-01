<template></template>

<script>
import axios from 'axios';


export default {
    name: '',
    components: {
    },

    data() {
        return {


        }
    },

    methods: {

        // 普通get/post请求
        async send_get_post_question() {


            await axios({
                url: "url地址",
                method: "post",
                // method: "get",
                headers: {
                    // 设置请求头
                    'token': this.$cookies.get("token")
                },
                data: {
                    // 设置请求体
                    oaid: this.$cookies.get("username")
                }

            }).then((res) => {

                // 设置响应内容
                if (res.data.result == "success") {
                    console.log(res.data)

                } else {
                    pageTips(res.data.info)
                }

            }).catch((err) => {
                console.log(err)
            })
        },


        // 表单形式传数据
        updateSubmitData() {

            let formData = new FormData()
            formData.append('files', this.update_upload)
            formData.append("file_url", this.update_download_url)
            formData.append('files_flag', this.update_backend_excel_flag)
            formData.append('filename', this.update_filename)
            formData.append("oaid", this.login_username)

            axios({
                url: "url地址",
                method: "post",
                data: formData,
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'token': this.$store.state.token
                }
            }).then((res) => {

                if (res.data.result == "success") {
                    pageTips(res.data.info)

                } else if (res.data.result == "error") {
                    pageTips(res.data.info)
                } else {
                    pageTips(res.data.info)
                }



            }).catch((error) => {

                pageTips(error)

            })

        },




    },

    mounted() {

    }

}
</script>

<style lange="less"></style>