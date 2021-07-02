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
    }else{

    }
    showSuggestions(emptyArray);
}

function showSuggestions(list){
    let listData;
    if(!list.length){
        listData = 'No results';
    }else{
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}