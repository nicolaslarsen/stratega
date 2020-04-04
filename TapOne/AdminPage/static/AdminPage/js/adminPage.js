$(document).ready(function(){
  $('.modal').on('hidden.bs.modal', function(){
    $(this).find('form')[0].reset();
  });
  $('.modal').on('focus', function(){
    var input = $(this).find('input')[0]
    if (input){
      input.focus();
    }
    var select = $(this).find('select')[0];
    if (select){
      select.focus();
    } 
  });
});
