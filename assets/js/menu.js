(function(){
    var burger = document.querySelector('.burger-container'),
        page__header = document.querySelector('.page__header');

    burger.onclick = function() {
        page__header.classList.toggle('menu-opened');
    }
}());
