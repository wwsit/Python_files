<template>
    <!-- 
        自动补全输入框
        文档地址：https://element-plus.org/zh-CN/component/autocomplete.html
    -->
    <div class="content_area">
        <el-autocomplete class="index_top2_input" id="detail_top2_input_id" v-model="input_key"
            :fetch-suggestions="querySearch" clearable placeholder="请输入名称" @select="handleSelect" />
    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: '',
    components: {
    },

    data() {
        return {

            input_key: "",

        }
    },

    methods: {



        // 根据关键字去获取内容 queryString:输入的内容
        async querySearch(queryString, cb) {

            console.log(queryString)

            // 本地交互,返回内容已写死
            // 需要是列表嵌字典结构，字典中必须要有value字段
            // eg:[{"value":"xx1"},{"value":"xx2"},{"value":"xx3"}]
            cb(
                [
                    {
                        "code": "001234",
                        "name": "\u56fd\u91d1\u4f17\u8d62\u8d27\u5e01",
                        "value": "\u56fd\u91d1\u4f17\u8d62\u8d27\u5e01(001234)"
                    },
                    {
                        "code": "011234",
                        "name": "\u5b8f\u5229\u4e2d\u503a1-5\u5e74\u56fd\u5f00\u503a\u6307\u6570A",
                        "value": "\u5b8f\u5229\u4e2d\u503a1-5\u5e74\u56fd\u5f00\u503a\u6307\u6570A(011234)"
                    },
                    {
                        "code": "012340",
                        "name": "\u4e1c\u8d22\u98df\u54c1\u996e\u6599\u589e\u5f3aA",
                        "value": "\u4e1c\u8d22\u98df\u54c1\u996e\u6599\u589e\u5f3aA(012340)"
                    },
                    {
                        "code": "012343",
                        "name": "\u5e7f\u53d1\u745e\u6cfd\u7cbe\u9009\u6df7\u5408C",
                        "value": "\u5e7f\u53d1\u745e\u6cfd\u7cbe\u9009\u6df7\u5408C(012343)"
                    },
                    {
                        "code": "012344",
                        "name": "\u5609\u5b9e\u9886\u5148\u4f18\u52bf\u6df7\u5408A",
                        "value": "\u5609\u5b9e\u9886\u5148\u4f18\u52bf\u6df7\u5408A(012344)"
                    },
                    {
                        "code": "012345",
                        "name": "\u5609\u5b9e\u9886\u5148\u4f18\u52bf\u6df7\u5408C",
                        "value": "\u5609\u5b9e\u9886\u5148\u4f18\u52bf\u6df7\u5408C(012345)"
                    }
                ]
            )

            // 发送请求给后端
            // if (queryString.length > 2) {

            //     await axios({
            //         url: "url",
            //         method: "post",
            //         headers: {
            //             'token': this.$store.state.token
            //         },
            //         data: {
            //             keyword: queryString,
            //             oaid: this.$store.state.username
            //         },

            //     }).then((res) => {

            //         if (res.data.result == "success") {
            //             // cb(data) 给 Autocomplete 组件返回建议。
            //             cb(res.data.data)
            //         }
            //     })

            // }
        },



        // 点击下拉菜单
        handleSelect(item) {
            console.log(item)
        },


    },




    mounted() {

    }

}
</script>

<style lange="less">
.content_area {

    margin-top: 5%;
    display: flex;
    justify-content: center;

    .index_top2_input {
        width: 500px;
    }
}
</style>