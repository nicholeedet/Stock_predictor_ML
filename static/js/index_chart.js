$.get( "http://127.0.0.1:5000/get_historical/AAPL", function( data ) {
    console.log(data)
    alert( "Load was performed." );
  });