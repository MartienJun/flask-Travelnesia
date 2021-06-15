// Add the following code if you want the name of the file appear on select
$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

// Live search
$(document).ready(function() {
    $("#searchPost").on("keyup", function() {
        var search = $(this).val().toLowerCase();
        $("#myPosts div.mypost").filter(function() {
            $(this).toggle($(this).find("#title").text().toLowerCase().indexOf(search) > -1)
        });
    });
});