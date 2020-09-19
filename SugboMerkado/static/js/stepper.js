var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    // if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
        // add an "invalid" class to the field:
        y[i].className += " invalid";
        // and set the current valid status to false
        valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}

function PreviewImage() {
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


$("#addJr").click(function(){
    $("#repeat-jr").append('<div id="jr-details" class="shadow p-5"><button id="remove-btn-jr" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder="" name="jr-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Grade</h5><input placeholder=""  name="jr-grade[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder=""  name="jr-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder=""  name="jr-awards[]"></div></div>');
});

$("body").on("click","#remove-btn-jr",function(e){
    $(this).parents('#jr-details').remove();
});


$("#addSr").click(function(){
    $("#repeat-sr").append('<div id="sr-details" class="shadow p-5"><button id="remove-btn-sr" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder=""  name="sr-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Grade</h5><input placeholder=""  name="sr-grade[]"></div><div class="col-12 col-sm"><h5>Strand</h5><input placeholder=""  name="sr-strand[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder=""  name="sr-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder=""  name="sr-awards[]"></div></div>');
});

$("body").on("click","#remove-btn-sr",function(e){
    $(this).parents('#sr-details').remove();
});

$("#addClg").click(function(){
    $("#repeat-clg").append('<div id="clg-details" class="shadow p-5"><button id="remove-btn-clg" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder=""  name="clg-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Course</h5><input placeholder="" name="clg-course[]"></div><div class="col-12 col-sm"><h5>Level</h5><input placeholder="" name="clg-lvl[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder="" name="clg-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder="" name="clg-awards[]"></div></div>');
});

$("body").on("click","#remove-btn-clg",function(e){
    $(this).parents('#clg-details').remove();
});


$("#addPg").click(function(){
    $("#repeat-pg").append('<div id="pg-details" class="shadow p-5"><button id="remove-btn-pg" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder=""  name="pg-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Course</h5><input placeholder="" name="pg-course[]"></div><div class="col-12 col-sm"><h5>Level</h5><input placeholder="" name="pg-lvl[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder="" name="pg-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder="" name="pg-awards[]"></div></div>');
});

$("body").on("click","#remove-btn-pg",function(e){
    $(this).parents('#pg-details').remove();
});

document.getElementById('datedis').value = new Date().toISOString().substring(0, 10);
