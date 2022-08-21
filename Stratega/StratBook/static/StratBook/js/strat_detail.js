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
    var collapseTargetId = $(this).attr('data-target');
    var dataParentId = $(collapseTargetId).attr('data-parent');

    var isCollapsed = $(collapseTargetId).hasClass('show');

    $(dataParentId + " .fa-angle-up").toggleClass("fa-angle-up fa-angle-down");

    if (!isCollapsed){
      // Change this icon to angle-up to show collapse
      $(this).find("span").toggleClass("fa-angle-down fa-angle-up");
    }
  });

  $(window).on('resize', function(){
    $(".sticky-top").css('max-height', '100vh');
  }).resize();
});
