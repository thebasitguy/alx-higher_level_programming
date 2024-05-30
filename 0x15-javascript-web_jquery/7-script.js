// Script that fetches the character name from a URL and displayed
// in the HTML tag DIV#character

let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('div#character').text(data.name);
});
