
$(document).ready(function() {
	var table=$('#example').DataTable( {
        dom: "<'row'<'col-sm-4'l><'col-sm-4 text-center'B><'col-sm-4'f>>" +
      "<'row'<'col-sm-12'tr>>" +
      "<'row'<'col-sm-5'i><'col-sm-7'p>>",
        buttons: [
			{	
				extend:'excelHtml5',
				text:'Export an Excel File',
				className:'excelBtn',
				exportOptions: {
					columns: ':not(:last-child)',
				},
				title:'Customer Report Summary'
			}
        ],
		select:true
    } );
	$('#min').on('change', function() {
		table.draw();
	});
	$('#max').on('change',function () {
		table.draw();
	});
} );

$.fn.dataTable.ext.search.push(
	function (settings, data, dataIndex, rowData, counter) {
		if(settings.nTable.id!='example'){return true;}
		var start = new Date($('#min').val());
		start.setHours(0);
		var end = new Date($('#max').val());
		end.setHours(0);
		var filter = new Date(data[0]);
		if (start == "Invalid Date" && end == "Invalid Date") { return true; }
		if (start == "Invalid Date" && filter <= end) { return true;}
		if(end == "Invalid Date" && filter >= start) {return true;}
		if (filter >= start && filter <= end) { return true; }
		return false;
	}
);


// $(document).ready(function() {
// 	var table2=$('#example1').DataTable( {
//         dom: "<'row'<'col-sm-4'l><'col-sm-4 text-center'B><'col-sm-4'f>>" +
//       "<'row'<'col-sm-12'tr>>" +
//       "<'row'<'col-sm-5'i><'col-sm-7'p>>",
//         buttons: [
// 			{	
// 				extend:'excelHtml5',
// 				text:'Export an Excel File',
// 				className:'excelBtn',
// 				exportOptions: {
// 					columns: ':not(:last-child)',
// 				},
// 				title:'Product Report Summary'
// 			}
//         ],
// 		select:true
//     } );
// 	$('#minProd').on('change', function() {
// 		table2.draw();
// 	});
// 	$('#maxProd').on('change',function () {
// 		table2.draw();
// 	});
// } );

// $.fn.dataTable.ext.search.push(
// 	function (settings, data, dataIndex, rowData, counter) {
// 		if(settings.nTable.id!='example1'){return true;}
// 		var start = new Date($('#minProd').val());
// 		start.setHours(0);
// 		var end = new Date($('#maxProd').val());
// 		end.setHours(0);
// 		var filter = new Date(data[0]);
// 		if (start == "Invalid Date" && end == "Invalid Date") { return true; }
// 		if (start == "Invalid Date" && filter <= end) { return true;}
// 		if(end == "Invalid Date" && filter >= start) {return true;}
// 		if (filter >= start && filter <= end) { return true; }
// 		return false;
// 	}
// )

$("#addElementary").click(function(){
    $("#repeat-elementary").append('<div id="elementary-details" class="shadow p-5"><button id="remove-btn-elem" class="btn btn-danger float-right mb-3" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash-alt" aria-hidden="true"></i></button><div class="form-group"><h5>School</h5><input placeholder="" name="elem-school[]"></div><div class="row form-group"><div class="col-12 col-sm"><h5>Grade</h5><input placeholder=""  name="elem-grade[]"></div><div class="col-12 col-sm"><h5>Year Completed</h5><input placeholder=""  name="elem-year[]"></div></div><div class="form-group"><h5>Awards</h5><input placeholder=""  name="elem-awards[]"></div></div>');
});

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