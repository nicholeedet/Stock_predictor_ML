// populating autocom-box
$.get( "http://127.0.0.1:5000/list_tickers", function( data ) {
    // console.log(data)
    data.forEach(function (tick, index) {
        console.log(tick);
        $('#tickers-list').append('<li>hello</li>');
      });
    
  });