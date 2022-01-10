
// 指定图表的配置项和数据
let option = {
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [
        {
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
        }
    ]
};

$(document).ready(function(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('main'));
    $.ajax({
        url: "/pm25-data/groupby=county",
        method: "GET",
        dataType: "json",
        success: function(res){
            //console.log(res);
            var _jobj = res;
            option['title'] = {'text':`資料時間: ${_jobj.time}`};
            option['xAxis']['data'] = _jobj.columns;
            option['series'][0]['name'] = 'PM25';
            option['series'][0]['data'] = _jobj.datas;
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        },
        error: (e) => {alert(e)} 
    })

})