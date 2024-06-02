function makeStackChart( categoriesData,
    seriesData,chartTitle){
    Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: chartTitle.title,
            align: 'left'
        },
        xAxis: {
            // season
            // categories: ['Arsenal', 'Chelsea', 'Liverpool', 'Manchester United']
            categories: categoriesData,
            title: {
                text: chartTitle.xAxisTitle
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: chartTitle.yAxisTitle
            },
            stackLabels: {
                enabled: true
            }
        },
        legend: {
            align: 'left',
            x: 70,
            verticalAlign: 'bottom',
            // y: 70,
            floating: false,
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            headerFormat: '<b>{point.x}</b><br/>',
            pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: true
                }
            }
        },
        // series: [{
        //     name: 'BPL',
        //     data: [3, 5, 1, 13]
        // }, {
        //     name: 'FA Cup',
        //     data: [14, 8, 8, 12]
        // }, {
        //     name: 'CL',
        //     data: [0, 2, 6, 3]
        // }]
        series: seriesData
});

}