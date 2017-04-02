// https://plot.ly/javascript/figure-labels/
var dataPoints = [];

var myData = (function() {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': "json/branddata.json",
        'dataType': "json",
        'success': function (data) {
            json = data;
            // Sorted via 1st brand, put count w/ 2nd brand

            for (var i=0; i< data.length; i++){
               dataPoints.push({
                   // first, second, count
                   name: data[i][0],
                   x: data[i][1],
                   y: data[i][2],
                   mode: 'markers',
                   marker: {
                    size: data[i][3]
                   }
               })
            }
        }
    });
    return json;
})();

//document.getElementById("demo").innerHTML = myData[1][1];
//document.getElementById("demo").innerHTML = JSON.stringify(dataPoints);

var data = dataPoints;
var layout = {
  width: window.screen.availWidth * 0.65,
  height: window.screen.availHeight * 0.70,
  legend: {
    x: 100,
    y: 1,
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
  margin: {
    autosize: true,
    l: 50,
    r: 20,
    b: 100,
    t: 0,
    pad: 4
  },
  xaxis: {
    title: 'Brands',
    titlefont: {
      family: 'Courier New, monospace',
      size: 18,
      color: '#7f7f7f'
    }
  },
  yaxis: {
    title: 'Counter',
    titlefont: {
      family: 'Courier New, monospace',
      size: 18,
      color: '#7f7f7f'
    }
  }
};
Plotly.newPlot('divBrands', data, layout)
