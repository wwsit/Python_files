
#### 函数延时执行

      this.setCellhighlight()
            setTimeout(() => {
                console.log(this.$route.query.projectId);
            }, 100); // 增加一些延迟


      setTimeout(() => {
                this.setCellhighlight()
            }, 100);


#### 同步发送请求

        async initSonTableData() {
            try {
                const response = await axios({
                    url: "请求地址",
                    method: "post",
                    headers: {
                        'token': this.$store.state.token
                    },
                    data: {
                        type: "基金涨跌情况",
                        oaid: this.$store.state.username
                    }
                });

                if (response.data.result === "success") {
                    this.tableData = response.data.data;
                    console.log(this.tableData);
                } else {
                    this.tableData = [];
                    pageTips(response.data.info);
                }
            } catch (error) {
                console.log(error);
            }
        },
