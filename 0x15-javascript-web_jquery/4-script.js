// Script that toggles the class of the <header> when a user
// clicks the DIV#toggle_header tag

$('div#toggle_header').click(function () {
    $('header').ToggleClass('red');
  });
