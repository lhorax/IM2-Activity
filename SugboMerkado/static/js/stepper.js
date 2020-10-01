var currentTab = 0; 
showTab(currentTab);

function showTab(n) {
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";

    //add require
    var y = x[currentTab].querySelectorAll('.validate');
    y.forEach(function (item) { 
        item.required = true;
    });

    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
        document.getElementById("nextBtn").setAttribute("name","submitBtn");
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    fixStepIndicator(n)
}

function nextPrev(n) {
    var myform = $("#regForm")[0];
    
    if (!myform.checkValidity()) {
        if (myform.reportValidity) {
            myform.reportValidity();
        } 
    }else{
        var x = document.getElementsByClassName("tab");
        x[currentTab].style.display = "none";
        currentTab = currentTab + n;
        if (currentTab >= x.length) {
            document.getElementById("regForm").submit();
            return false;
        }
        showTab(currentTab);
    }
    
}


function fixStepIndicator(n) {
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    x[n].className += " active";
}

function PreviewImageRegister() {
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("uploadImage").files[0]);

    oFReader.onload = function (oFREvent) {
        document.getElementById("uploadPreview").src = oFREvent.target.result;
    };
};

//add elementary
$("#addElementary").click(function(){
    $("#repeat-elementary").append('<div id="elementary-details" class="shadow p-5"><button id="remove-btn-elem" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder="" name="elem-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Grade</h5><input placeholder=""  name="elem-grade[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder=""  name="elem-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder=""  name="elem-awards[]"></div></div>');
});
//remove elementary
$("body").on("click","#remove-btn-elem",function(e){
    $(this).parents('#elementary-details').remove();
});

//add junior
$("#addJr").click(function(){
    $("#repeat-jr").append('<div id="jr-details" class="shadow p-5"><button id="remove-btn-jr" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder="" name="jr-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Grade</h5><input placeholder=""  name="jr-grade[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder=""  name="jr-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder=""  name="jr-awards[]"></div></div>');
});
//remove junior
$("body").on("click","#remove-btn-jr",function(e){
    $(this).parents('#jr-details').remove();
});

//add senior high
$("#addSr").click(function(){
    $("#repeat-sr").append('<div id="sr-details" class="shadow p-5"><button id="remove-btn-sr" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder=""  name="sr-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Grade</h5><input placeholder=""  name="sr-grade[]"></div><div class="col-12 col-sm"><h5>Strand</h5><input placeholder=""  name="sr-strand[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder=""  name="sr-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder=""  name="sr-awards[]"></div></div>');
});
//remove senior high
$("body").on("click","#remove-btn-sr",function(e){
    $(this).parents('#sr-details').remove();
});
//add college
$("#addClg").click(function(){
    $("#repeat-clg").append('<div id="clg-details" class="shadow p-5"><button id="remove-btn-clg" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder=""  name="clg-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Course</h5><input placeholder="" name="clg-course[]"></div><div class="col-12 col-sm"><h5>Level</h5><input placeholder="" name="clg-lvl[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder="" name="clg-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder="" name="clg-awards[]"></div></div>');
});
//remove college
$("body").on("click","#remove-btn-clg",function(e){
    $(this).parents('#clg-details').remove();
});

//add post grad
$("#addPg").click(function(){
    $("#repeat-pg").append('<div id="pg-details" class="shadow p-5"><button id="remove-btn-pg" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder=""  name="pg-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Course</h5><input placeholder="" name="pg-course[]"></div><div class="col-12 col-sm"><h5>Level</h5><input placeholder="" name="pg-lvl[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder="" name="pg-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder="" name="pg-awards[]"></div></div>');
});
//remove post grad
$("body").on("click","#remove-btn-pg",function(e){
    $(this).parents('#pg-details').remove();
});

