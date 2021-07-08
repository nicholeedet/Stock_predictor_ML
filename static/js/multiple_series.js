var chart = LightweightCharts.createChart(document.body, {
	width: 600,
  height: 300,
	rightPriceScale: {
		visible: true,
    borderColor: 'rgba(197, 203, 206, 1)',
	},
	leftPriceScale: {
		visible: true,
    borderColor: 'rgba(197, 203, 206, 1)',
	},
	layout: {
		backgroundColor: '#ffffff',
		textColor: 'rgba(33, 56, 77, 1)',
	},
  grid: {
    horzLines: {
      color: '#F0F3FA',
    },
    vertLines: {
      color: '#F0F3FA',
    },
  },
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 1)',
	},
	handleScroll: {
		vertTouchDrag: true,
	},
});

ticker = document.title;
// Fetching api data from our flask app
fetch('http://127.0.0.1:5000/get_historical/' + ticker)
	.then((r) => r.json())
	.then((response) => {
		console.log(response);

	});