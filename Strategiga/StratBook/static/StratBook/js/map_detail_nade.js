$(document).ready(function(){
  var maxHeight = 0;

  var nadepics = $(".nadepic").each(function(){
    var height = $(this).height()
    if (height > maxHeight){
      maxHeight = height
    }
  });

  nadepics.height(maxHeight);
});
