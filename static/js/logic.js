// populating autocom-box
$.get( "http://127.0.0.1:5000/list_tickers", function( data ) {
    // console.log(data)
    var ul = document.getElementsByClassName("tickers-list");
    data.forEach(function (tick, index) {
        // console.log(tick);
        var li = document.createElement('li');
        li.appendChild(document.createTextNode(tick));
        ul.appendChild(li);
      });
    
  });