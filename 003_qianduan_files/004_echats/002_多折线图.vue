<template>
    <div class="second_label_name">
        <div id="myChart" style="height: 400px;margin-top: 10%;"></div>
    </div>
</template>
  
<script>
import * as echarts from 'echarts'

export default {

    methods: {


        // 画折线图 
        drawChart() {

            this.drawLineOption = {

                // 设置主标题和副标题属性
                title: {
                    text: '成绩统计图',
                    x: 'center',
                },

                // 显示图例
                legend: {
                    orient: 'horizontal',
                    top: '8%',
                    left: 'center',
                    textStyle: {
                        fontSize: 13,
                    },
                    // data: ['小A', '小B', '小C', '小D', '小E']  // 设置图例的值

                },


                // 直角坐标系内绘图网格
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },

                // 鼠标放置显示数组
                tooltip: {
                    axisPointer: {
                        type: 'cross'
                    },
                },

                // 工具栏,内置有导出图片，数据视图，动态类型切换，数据区域缩放，重置五个工具。
                toolbox: {
                    feature: {
                        saveAsImage: {
                            name: "图片"
                        }
                    }
                },

                // x轴
                xAxis: {
                    type: 'category',
                    data: ['第一模拟考试成绩', '第二模拟考试成', '第三模拟考试成', '第四模拟考试成', '第五模拟考试成', '第六模拟考试成'],
                    axisLabel: {
                        interval: 0,
                        rotate: -45   // 坐标倾斜
                    }

                },

                // Y轴
                yAxis: {
                    type: 'value'
                },

                series: [
                    {
                        name: '小A',
                        type: 'line',
                        data: [10, 12, 13, 10, 12, 18],
                        itemStyle: {
                            borderWidth: 20
                        }
                    },
                    {
                        name: '小B',
                        type: 'line',
                        data: [20, 30, 41, 54, 60, 73],
                        itemStyle: {
                            borderWidth: 20
                        }
                    },
                    {
                        name: '小C',
                        type: 'line',
                        data: [30, 44, 40, 33, 40, 45],
                        itemStyle: {
                            borderWidth: 20
                        }
                    },
                    {
                        name: '小D',
                        type: 'line',
                        data: [90, 82, 81, 85, 95, 90],
                        itemStyle: {
                            borderWidth: 20
                        }
                    },
                    {
                        name: '小E',
                        type: 'line',
                        data: [82, 93, 90, 93, 90, 100],
                        itemStyle: {
                            borderWidth: 20
                        }
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