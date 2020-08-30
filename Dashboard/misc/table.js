$(document).ready(function() {
    $('#customerTable').DataTable({
		"pagingType": "full_numbers"
	});
	
	$('#productTable').DataTable({
		"pagingType": "full_numbers"
	});
	
	$("[data-toggle=tooltip]").tooltip();
} );