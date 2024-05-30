// Script that fetches and prints how to say “Hello” depending on the language.

document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate')[0].addEventListener('click', function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data, stat) {
      $('DIV#hello').text(data.hello);
    });
  });
});
