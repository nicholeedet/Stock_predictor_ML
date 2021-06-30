const mainMenu = document.querySelector('.mainMenu')
const closeMenu = document.querySelector('.closeMenu')
const openMenu = document.querySelector('.openMenu')

openMenu.addEventListener('click',show);
closeMenu.addEventListener('click',close_);

function show(){
    mainMenu.style.display = 'flex';
    mainMenu.style.top= '-15px';
}

function close_(){
    mainMenu.style.top = '-105%';
}