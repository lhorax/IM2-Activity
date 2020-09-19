
$(document).ready(function() {
	var d = new Date();
	var month = d.getMonth() + 1;
	var day = d.getDate();
	if(day<10){
		day="0"+day;
	}
	if(month<10){
		month="0"+month;
	}
	var year = d.getFullYear();
	var temp = ""+year+"/"+month+"/"+day;
	document.getElementById("dateRegistered").innerHTML = temp;

	
});

function PreviewImageProduct(id) {
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById(id).files[0]);

    oFReader.onload = function (oFREvent) {
    	if(id == "image1"){
    		var img="imgPreview1";
    	}
    	else if(id == "image2"){
    		var img = "imgPreview2";
    	}
    	else if(id == "image3"){
    		var img = "imgPreview3";
    	}
        document.getElementById(img).src = oFREvent.target.result;
    };
};

$("#image1").change(function() {
	$("#removeImage1").show(); // show remove link
});

$("#removeImage1").click(function(e) {
	e.preventDefault(); // prevent default action of link
	$("#image1").val(""); // clear image input value
	document.getElementById("imgPreview1").src = '/static/websiteImgs/placeholder2.png';	
	$("#removeImage1").toggle(); // hide remove link.
});	

$("#image2").change(function() {
	$("#removeImage2").show(); // show remove link
});

$("#removeImage2").click(function(e) {
	e.preventDefault(); // prevent default action of link
	$("#image2").val(""); // clear image input value
	document.getElementById("imgPreview2").src = '/static/websiteImgs/placeholder2.png';
	$("#removeImage2").toggle(); // hide remove link.
});

$("#image3").change(function() {
	$("#removeImage3").show(); // show remove link
});

$("#removeImage3").click(function(e) {
	e.preventDefault(); // prevent default action of link
	$("#image3").val(""); // clear image input value
	document.getElementById("imgPreview3").src = '/static/websiteImgs/placeholder2.png';
	$("#removeImage3").toggle(); // hide remove link.
});