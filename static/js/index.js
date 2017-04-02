// https://plot.ly/javascript/figure-labels/
var dataPoints = [];

var myData = (function() {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': "json/brandsourcedata.json",
        'dataType': "json",
        'success': function (data) {
            json = data;
            // Sorted via 1st brand, put count w/ 2nd brand

            for (var i=0; i< data.length; i++){
               dataPoints.push({
               name: data[i][0], // brand
               x: [data[i][5]], // category
               y: [data[i][1]], // buzz count
               mode: 'markers',
               marker: {
                color: [data[i][3]],
                size: [data[i][2]]
               }
//               connectgaps: true,
//               type: 'scatter'
               })
            }
        }
    });
    return json;
})();

//document.getElementById("demo").innerHTML = JSON.stringify(dataPoints);

// EXAMPLE:
//    var trace0 = {
//      name: "vogue", //index0
//      x: [420, 131, 46, 281, 51, 721, 32, 222, 133, 212], //index2
//      y: ['chanel', 'calvin_klein', 'coach', 'gucci', 'hermes', 'kate_spade', 'longchamp', 'louis_vuitton', 'michael_kors', 'prada'], //index1
//      text: ['Brand: chanel</br> Count: 420', 'Brand: calvin_klein</br> Count: 131', 'Brand: coach</br> Count: 46', 'Brand: gucci</br> Count: 281', 'Brand: hermes</br> Count: 51', 'Brand: kate_spade</br> Count: 721', 'Brand: longchamp</br> Count: 32', 'Brand: louis_vuitton</br> Count: 222', 'Brand: michael_kors</br> Count: 133', 'Brand: prada</br> Count: 212'], //index5
//      mode: 'markers',
//      marker: {
//        color: ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'], //index4
//        size: [50, 20, 10, 30, 10, 80, 10, 30, 20, 30] //index3
//      }
//    };

var data = dataPoints;
var layout = {
  width: window.screen.availWidth * 0.65,
  height: window.screen.availHeight * 0.65,
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
    l: 100,
    r: 20,
    b: 55,
    t: 0,
    pad: 4
  },
  xaxis: {
    titlefont: {
      family: 'Courier New, monospace',
      size: 16,
      color: '#7f7f7f'
    }
  },
  yaxis: {
    title: 'Total Buzz',
    titlefont: {
      family: 'Courier New, monospace',
      size: 18,
      color: '#7f7f7f'
    }
  }
};

Plotly.newPlot('divMarketOverview', data, layout);