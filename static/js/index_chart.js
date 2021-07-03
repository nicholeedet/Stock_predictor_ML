var chart_init = LightweightCharts.createChart(document.getElementById("chart"), {
	width: $(".container").width(),
  height: $(window).height()-$(document.getElementsByTagName("header")).height(),
	layout: {
		textColor: '#d1d4dc',
		backgroundColor: '#000000',
	},
	rightPriceScale: {
		scaleMargins: {
			top: 0.3,
			bottom: 0.25,
		},
	},
	crosshair: {
		vertLine: {
			width: 5,
			color: 'rgba(224, 227, 235, 0.1)',
			style: 0,
		},
		horzLine: {
			visible: false,
			labelVisible: false,
		},
	},
	grid: {
		vertLines: {
			color: 'rgba(42, 46, 57, 0)',
		},
		horzLines: {
			color: 'rgba(42, 46, 57, 0)',
		},
	},
});

var areaSeries = chart_init.addAreaSeries({
  topColor: 'rgba(0, 230, 64, 0.7)',
  bottomColor: 'rgba(0, 230, 64, 0.04)',
  lineColor: 'rgba(0, 230, 64, 1)',
  lineWidth: 2,
  crossHairMarkerVisible: false,
});

// Fetching api data from our flask app
fetch('http://127.0.0.1:5000/get_historical/AAPL')
	.then((r) => r.json())
	.then((response) => {
		console.log(response);
		areaSeries.setData(response);
	});
  
    document.body.style.position = 'relative';

    var legend = document.createElement('div');
    legend.classList.add('legend');
    document.getElementById("chart").appendChild(legend);
    
    var firstRow = document.createElement('div');
    firstRow.innerText = 'AAPLE';
    firstRow.style.color = 'white';
    legend.appendChild(firstRow);
    
    function pad(n) {
        var s = ('0' + n);
        return s.substr(s.length - 2);
    }
    
    chart_init.subscribeCrosshairMove((param) => {
        if (param.time) {
            const price = param.seriesPrices.get(areaSeries);
            firstRow.innerText = 'APPLE' + '  ' + price.toFixed(2);
        }
      else {
          firstRow.innerText = 'APPLE';
      }
    });

    chart_init.applyOptions({
        handleScroll: {
            mouseWheel: false,
            pressedMouseMove: false,
            handleScroll: false,
        },
        handleScale: {
            axisPressedMouseMove: false,
            mouseWheel: false,
            pinch: false,
        },
    });
    chart_init.applyOptions({
        handleScroll: false,
        handleScale: false,
    });

    // handling onresize event(chart's dimensions will be readjusted)
    $(window).on('resize', function(){
        var new_width = $(".container").width();
        var new_height= $(window).height()-$(document.getElementsByTagName("header")).height();
        chart_init.resize(new_width, new_height);
    });