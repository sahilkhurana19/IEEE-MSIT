var modalJSON = "https://api.myjson.com/bins/5aahg";

$("document").ready(function(){
	$(".modal-trigger").on("click", function(){
		ajaxByParameter(modalJSON);
	});
});	


function ajaxByParameter(url1){
	$.ajax({
		url: modalJSON,
		dataType: "json",
		type: "GET",
		data: {},
		success: function(data) {
			console.log("Request got")
			$("#modalContent").html("<h4>" + data.heading + "</h4><p>" + data.info + "</p>");
		}
	})
}
