<template>
  <div className="second_label_name">
    <div id="myChart" style="height: 400px"></div>
  </div>

</template>

<script>
import * as echarts from 'echarts'

export default {

  methods: {

    // 画折线图
    // 使用 async await 等待接口返回的数据，然后程序才继续往下执行
    async drawChartByInterface() {

      await axios({
        url: "",
        method: "post",
      }).then((res) => {
        if (res.data.result == "success") {
          // 配置折线图的数据和样式
          this.drawLineOption = res.data.data
        } else {
          pageTips(res.data.info)
        }
      }).catch((err) => {
        pageTips(res.data.info)
      })

      // 创建一个 ECharts 实例
      let chart = echarts.init(document.getElementById("myChart"))

      // 使用刚指定的配置项和数据显示图表
      chart.setOption(this.drawLineOption);

    },

    // 画折线图
    drawChart() {

      this.drawLineOption = {

        // 设置主标题和副标题属性
        title: {
          text: '这里是设置图表主题',
          x: 'center',
        },

        // x轴
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },

        // Y轴
        yAxis: {
          type: 'value'
        },

        // 鼠标放置数值提示
        tooltip: {
          axisPointer: {
            type: 'cross'
          }
        },

        series: [
          {
            data: [150, 230, 224, 218, 135, 147, 260],
            type: 'line'   // 设置成折线图
          }
        ]
      };

      // 创建一个 ECharts 实例
      let chart = echarts.init(document.getElementById("myChart"))
      // 使用刚指定的配置项和数据显示图表
      chart.setOption(this.drawLineOption);

    },


  },


  mounted() {

    this.drawChart()
  },


}
</script>

<style lang="less">
.level0 {

  margin-top: 5%;
  margin-left: 5%;


}
</style>
