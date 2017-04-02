////// https://plot.ly/javascript/figure-labels/
var dataPoints = [];
var colorlist = ['red','blue','green','orange','grey','purple','cyan','lightpink','lime','navy'];
var optlist = [0, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75];
var vislist = [true,"legendonly","legendonly","legendonly","legendonly","legendonly","legendonly","legendonly","legendonly","legendonly","legendonly"]

var myData = (function() {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': "json/corpfbsourcedata.json",
        'dataType': "json",
        'success': function (data) {
            json = data;
            // Sorted via 1st brand, put count w/ 2nd brand

            for (var i=0; i< data.length; i++){
               dataPoints.push({
                   x: data[i][1], // timestamp
                   y: data[i][2], // scores
                   type: 'bar',
                   name: data[i][0], // brand
                   opacity: 0.5,
                   visible: vislist[i],
                   marker: {
                    color: colorlist[i]
                   },
               });
            }
        }
    });
    return json;
})();

//document.getElementById("demo2").innerHTML = JSON.stringify(dataPoints);

var data = dataPoints;

var layout = {
  width: window.screen.availWidth * 0.65,
  height: window.screen.availHeight * 0.65,
  barmode: "group",
//  barmode: "overlay",
  margin: {
    autosize: true,
    l: 55,
    r: 20,
    b: 55,
    t: 0,
    pad: 4
  },
  xaxis: {title: "timestamp"},
  yaxis: {title: "score"}
};

Plotly.newPlot('divhisfacebook', data, layout);