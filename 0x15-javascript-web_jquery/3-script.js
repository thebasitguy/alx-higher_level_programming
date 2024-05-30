// Script that uses the jQuery API to add a red class to the header tag
// and turn it red when a user clicks the DIV#red_header tag.

$('div#red_header').click(function () {
    $('header').addClass('red');
  });
