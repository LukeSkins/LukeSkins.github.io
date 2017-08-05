window.onload = function() {
  (function() {

    var menubutton = document.querySelector('.menubtn'),
      menu = document.querySelector('.menu'),
      closebutton = document.querySelector('.closebtn'),
      content = document.querySelector('body');

    menubutton.onclick = function() {
      menu.classList.toggle('hide');
      content.classList.toggle('noscroll');
    }

    closebutton.onclick = function() {
      menu.classList.toggle('hide');
      content.classList.toggle('noscroll');
    }


  }());

};
