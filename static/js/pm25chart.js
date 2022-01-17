var myChart;

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

function ShowData(res){
    //console.log(res);
    var _jobj = res;
    option['title'] = {'text':`資料時間: ${_jobj.time}`};
    option['xAxis']['data'] = _jobj.columns;
    option['series'][0]['name'] = 'PM25';
    option['series'][0]['data'] = _jobj.datas;
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);

}
function showData(groupby){
    // 基于准备好的dom，初始化echarts实例
    myChart = echarts.init(document.getElementById('main'));
    if(typeof groupby == "undefined") groupby='county';
    var _url = "/pm25-data" + ((groupby=='') ?'' :'/groupby='+groupby);
    console.log(_url);
    $.ajax({
        url: _url,
        method: "GET",
        dataType: "json",
        success: (res) => {
            //console.log(res);
            var _jobj = res;
            var _extra = _jobj.extra
            option['title'] = {'text':`資料時間: ${_extra.DateTime}`};
            option['xAxis']['data'] = _jobj.columns;
            option['series'][0]['name'] = 'PM25';
            option['series'][0]['data'] = _jobj.datas;
            //console.log(_extra);
            $('#pnlMaxSite').text(`${_extra['Max']['Site']}(${_extra['Max']['County']})`);
            $('#pnlMaxValue').text(`${_extra.Max.Value}`);
            $('#pnlMinSite').text(`${_extra.Min.Site}(${_extra.Min.County})`);
            $('#pnlMinValue').text(`${_extra.Min.Value}`);

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        },
        error: function (jqXHR, exception) {
            var msg = '';
            if (jqXHR.status === 0) {
                msg = 'Not connect.\n Verify Network.';
            } else if (jqXHR.status == 404) {
                msg = 'Requested page not found. [404]';
            } else if (jqXHR.status == 500) {
                msg = 'Internal Server Error [500].';
            } else if (exception === 'parsererror') {
                msg = 'Requested JSON parse failed.';
            } else if (exception === 'timeout') {
                msg = 'Time out error.';
            } else if (exception === 'abort') {
                msg = 'Ajax request aborted.';
            } else {
                msg = 'Uncaught Error.\n' + jqXHR.responseText;
            }
            //$('#post').html(msg);
            $('#post').append($('<div />').addClass('alert alert-success').attr('role', 'alert').text(msg).append($('<button />').attr('type','button').attr('class','close').attr('data-dismiss','alert').attr('aria-label','close').append($('<span aria-hidden="true">&times;</span>'))));
        } 
    })
}

function switchGroupby(e){
    console.log(e);
}

$(document).ready(function(){
    showData();

    $('#frmSwitchDisp').on('click','input',[],function(e){
        //console.log($(this));
        var _groupby = $(this).val();
        showData(_groupby);
    }).on('click','.btn',[],function(e){
        //console.log($(this).children());
        //$(this).find('input').click();
    })
    window.onresize = function(){
        myChart.resize();
    };
})