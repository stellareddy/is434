// https://plot.ly/javascript/figure-labels/
var dataPoints = [];

var myData = (function() {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': "json/sentimentdata.json",
        'dataType': "json",
        'success': function (data) {
            json = data;
            // Sorted via 1st brand, put count w/ 2nd brand

            for (var i=0; i< data.length; i++){
               dataPoints.push({
               name: data[i][0],
               x: data[i][1],
               y: data[i][3],
               legendgroup: data[i][4],
               text: data[i][2],
               mode: 'markers+lines',
               connectgaps: true,
               type: 'scatter'})
            }
        }
    });
    return json;
})();

//document.getElementById("demo").innerHTML = JSON.stringify(dataPoints);

var data = dataPoints;
var layout = {
  width: window.screen.availWidth * 0.65,
  height: window.screen.availHeight * 0.68,
  showlegend: true,
  legend: {
    //"orientation": "h",
    x: 100,
    y: 0,
    traceorder: 'normal',
    font: {
      family: 'sans-serif',
      size: 12,
      color: '#000'
    },
    bgcolor: '#E2E2E2',
    bordercolor: '#FFFFFF',
    borderwidth: 2
  },
  xaxis: {
    title: 'Scores for the past 12 month',
    titlefont: {
      family: 'Courier New, monospace',
      size: 18,
      color: '#7f7f7f'
    }
  },
  yaxis: {
    title: 'Buzz Count',
    titlefont: {
      family: 'Courier New, monospace',
      size: 16,
      color: '#7f7f7f'
    }
  },
  margin: {
    autosize: true,
    l: 70,
    r: 20,
    b: 100,
    t: 5,
    pad: 4
  }
};

Plotly.newPlot('divSentiment', data, layout, hoverinfo = "text");