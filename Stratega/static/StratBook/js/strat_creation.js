$(document).ready(function(){
  $('#add-more').click(function() {
    var form_index = $('#id_bullet_set-TOTAL_FORMS').val();
    var bullet_set_id_text = "bullet_set-" + form_index
    $('#shown-bullets').append($('#hidden-bullet').html().replace(
            /bullet_set-[0-9]/g, bullet_set_id_text));
    $('#id_bullet_set-TOTAL_FORMS').val(parseInt(form_index) + 1);
    $('#delete_bullet_set-' + form_index).on('click', removeClick);

    $('#id_' + bullet_set_id_text + '-text').on('focus', function(){
      var tmp = $(this).val();
      $(this).val('');
      $(this).val(tmp);
    });
    $('#id_' + bullet_set_id_text + '-text').focus();
  });

  var removeClick = function(){
      var index = this.id.match(/\d+/)[0];
      $('#row_bullet_set-' + index).remove();
      // TODO: probably decrement the TOTAL_FORMS. But the id's would need to change
  };

  $('[id^=delete_bullet_set-]').each(function(){
    $(this).on("click", removeClick);
  })

});
