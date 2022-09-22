$(function() {
  $.ajax({
    type: 'GET',
    url: 'https://stefanbohacek.com/hellosalut/?lang=es',
    success: function(data){
      $('DIV#hello').text(data.hello);
    },
    error: function() {
      alert('Error for loading API');
    }
  })
});
