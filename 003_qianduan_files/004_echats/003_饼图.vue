<template>
    <div class="second_label_name">
        <div id="myChart1" style="height: 400px;margin-top: 5%;"></div>
    </div>

    <div class="second_label_name">
        <div id="myChart2" style="height: 400px;margin-top: 5%;"></div>
    </div>
</template>
  
<script>
import * as echarts from 'echarts'

export default {

    methods: {


        // 画饼图1
        drawChart1() {

            this.drawLineOption = {

                title: {
                    text: '奖金分配情况',
                    left: 'center'
                },

                // 鼠标放置显示数值
                tooltip: {
                    trigger: 'item' // 触发类型 item使用在饼图
                },

                // 显示图例
                legend: {
                    orient: 'vertical',
                    left: 'left'
                },

                series: [
                    {
                        type: 'pie',
                        radius: '50%',
                        data: [
                            { value: 200, name: '一班' },
                            { value: 300, name: '二班' },
                            { value: 100, name: '三班' },
                            { value: 150, name: '四班' },
                            { value: 250, name: '五班' }
                        ],

                        // 高亮状态的扇区和标签样式
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };

            // 创建一个 ECharts 实例
            let chart = echarts.init(document.getElementById("myChart1"))
            // 使用刚指定的配置项和数据显示图表
            chart.setOption(this.drawLineOption);

        },



        // 画饼图2
        drawChart2() {

            this.drawLineOption = {

                title: {
                    text: '奖金分配情况',
                    left: 'center'
                },

                // 鼠标放置显示数值
                tooltip: {
                    trigger: 'item' // 触发类型 item使用在饼图
                },


                // 显示图例
                legend: {
                    orient: 'vertical',
                    left: 'left'
                },

                series: [
                    {
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },

                        // 显示各个区域的文本标签
                        label: {
                            show: true,
                            position: 'outside'  // 显示在外围
                        },

                        // 是否显示 连接文本标签的 线
                        labelLine: {
                            show: true
                        },
                        data: [
                            { value: 200, name: '一班' },
                            { value: 300, name: '二班' },
                            { value: 100, name: '三班' },
                            { value: 150, name: '四班' },
                            { value: 250, name: '五班' }
                        ],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            },
                         
                        }
                    }
                ]
            };

            // 创建一个 ECharts 实例
            let chart = echarts.init(document.getElementById("myChart2"))
            // 使用刚指定的配置项和数据显示图表
            chart.setOption(this.drawLineOption);

        },


    },


    mounted() {

        this.drawChart1()
        this.drawChart2()
    },


}
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