function makeColumnBarChart(
    categoriesData,
    seriesData,
    chartTitle
) {
    Highcharts.chart("container", {
        chart: {
            type: "column",
        },
        title: {
            text: chartTitle.title,
            align: "left",
        },
        xAxis: {
            categories: categoriesData,
            // categories: ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],

            crosshair: true,
            accessibility: {
                description: "Countries",
            },
            title: {
                text: chartTitle.xAxisTitle,
            },
        },
        yAxis: {
            min: 0,
            title: {
                text: chartTitle.yAxisTitle,
            },
        },
        tooltip: {
            valueSuffix: " (Matches)",
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0,
            },
        },
        series: [
            {
                // data: [58, 57, 60, 73, 74, 76, 60, 59, 60, 59]
                data: seriesData,
                showInLegend: false,
            },
        ],
    });
}
