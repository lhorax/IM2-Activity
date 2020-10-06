
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
    var num = id.split('-')[1];
    var str = "p-"+num;
    oFReader.onload = function (oFREvent) {
        document.getElementById(str).src = oFREvent.target.result;
    };
    ChangeImage(id);
};

function ChangeImage(id) {
	var num = id.split('-')[1];
	var str = "r-"+num;
	var btn = document.getElementById(str);
	btn.style.display = "block";
};

function RemoveImage(id,e) {
	e.preventDefault();
	var num = id.split('-')[1];
	var str1 = 'p-'+num;
	var str2 = 'i-'+num;
	var img = document.getElementById(str2);
	document.getElementById(str1).src = '/static/websiteImgs/placeholder2.png';
	var btn = document.getElementById(id);
	btn.style.display = 'none';
	img.value = "";
};

$(document).ready(function() {
	
	var y = document.getElementsByClassName("imgArea");
	for (var i=0;i<y.length;i++){
		var k = y[i].children;
		for(var j=0;j<k.length;j++){
			if(k[j].id != 'img-container'){
				if(k.length == 3){	//has only one image; 3 because it counts hidden children
					k[j].style.display = "block";
				}
				else if(k.length == 4){
					k[j].style.display = "block";break;	
				}
			}
		}
	}
	
	
	var count = 1, count2=1;
	var x = document.getElementsByClassName("img-container");
	for (var i=0;i<x.length;i++){
		if(x[i].style.display == 'block'){
			var k = x[i].children;
			for(var j = 0; j < k.length; j++){
				if (k[j].classList[0] == "imgPreview"){
					var str = k[j].classList[0]+count;
					k[j].classList.replace('imgPreview',str);
					k[j].id = "p-"+count2;
				}
				if (k[j].classList[0] == "image"){
					var str = k[j].classList[0]+count;
					k[j].classList.replace('image',str);
					k[j].name+=count;
					k[j].id = "i-"+count2;
				}
				if (k[j].classList[0] == "removeImage"){
					var str = k[j].classList[0]+count;
					k[j].classList.replace('removeImage',str);
					k[j].id = "r-"+count2;
				}
				
			}
			count++;
		    if(count==4){
		    	count=1;
		    }
			count2++;
		}
	}

});
