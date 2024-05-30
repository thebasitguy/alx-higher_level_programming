// Script that adds a <li> element to a list when the DIV#add_item tag is clicked.
// The new element must be <li>Item</li> and added to UL.my_list.

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
