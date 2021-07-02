const searchWrapper = document.querySelector('.searchbar')
const inputBox = searchWrapper.querySelector('input')
const suggBox = document.querySelector('.autocom-box')

// if user press any key and release
inputBox.onkeyup = (e) =>{
    let userData = e.target.value;
    let emptyArray = [];
    if(userData){
        emptyArray = suggestions.filter((data)=>{
            return data.toLocaleLowerCase()
        });
        console.log(emptyArray);
    }
}