$(document).ready(function(){
	$("#activeDutyCheck").click(function(){
    var isChecked = $("#activeDutyCheck").is(":checked");
    if(isChecked){
      $("#inactive_maps").hide();
    }
    else{
      $("#inactive_maps").show();
    }
	});
});
