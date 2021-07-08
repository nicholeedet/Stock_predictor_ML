const searchWrapper = document.querySelector('.searchbar')
const inputBox = searchWrapper.querySelector('input')
const suggBox = document.querySelector('.autocom-box')

// if user press any key and release
inputBox.onkeyup = (e) =>{
    let userData = e.target.value;
    let emptyArray = [];
    if(userData){
        emptyArray = suggestions.filter((data)=>{
            // filtering array value and user char to lowercase and return only those word/sentence that starts with the users input
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            return data = '<li>' + data + '</li>';
        });
        console.log(emptyArray);
        searchWrapper.classList.add("active");
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll('li');
        for(var i=0; i< allList.length; i++){
            // Adding OnClick event to results
            allList[i].setAttribute("onclick","select(this)")
        }
    }else{
        searchWrapper.classList.remove("active"); // hide autocomplete box
    }
    
}

function select(element){
    let selectUserData = element.textContent;
    inputBox.value = selectUserData;
    searchWrapper.classList.remove("active")
}

function showSuggestions(list){
    let listData;
    if(!list.length){
        uservValue = inputBox.value;
        listData = '<li>'+ uservValue + '</li>';
    }else{
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}

$( ".submit_btn" ).click(function() {
    // alert( inputBox.value);
    if (suggestions.includes(inputBox.value)){
        const myarray = inputBox.value.split(" ");
        var ticker = myarray[myarray.length-1];
        window.open('http://127.0.0.1:5000/models/' + ticker);
    }else{
        alert("Please select a valid Company")
    }
  });