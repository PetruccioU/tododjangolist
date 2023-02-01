$('#Parent').scroll(function() {
    $('#FixedDiv').css('top', $(this).scrollTop());
});















//$('#ParentContainer').scroll(function() {
//    $('#FixedDiv').css('top', $(this).scrollTop());
//});
//
//A better JQuery answer would be:
//
//$('#ParentContainer').scroll(function() {
//    $('#FixedDiv').animate({top:$(this).scrollTop()});
//});
//You can also add a number after scrollTop i.e .scrollTop() + 5 to give it buff.
//
//A good suggestion would also to limit the duration to 100 and go from default swing to linear easing.
//
//$('#ParentContainer').scroll(function() {
//    $('#FixedDiv').animate({top:$(this).scrollTop()},100,"linear");
//})