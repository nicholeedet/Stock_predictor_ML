// populating autocom-box
// let suggestions=[];

// $.get( "http://127.0.0.1:5000/list_tickers", function( data ) {
//     // console.log(data)
//      suggestions = data;
//   });

//   console.log(suggestions)
url = "http://127.0.0.1:5000/list_tickers"

async function getData(url) {
    const response = await fetch(url);
  
    return response.json();
  }
  
  let data = getData(url);
  console.log(data)