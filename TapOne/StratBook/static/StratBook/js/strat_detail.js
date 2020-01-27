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

  $(".card-link").click(function(){
    $(this).find("span").toggleClass("fa-angle-down fa-angle-up");
  });

  $(window).on('resize', function(){
    $(".sticky-top").css('max-height', '70vh');
  }).resize();
});
