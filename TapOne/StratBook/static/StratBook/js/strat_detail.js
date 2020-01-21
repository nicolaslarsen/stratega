$(document).ready(function(){
  $("#egoCheck").click(function(){
    var isChecked = $("#egoCheck").is(":checked");
    if (isChecked){
      $(".selfless").hide();
    }
    else {
      $(".selfless").show();
    }
    $(".show").removeClass('show');
  });
});
