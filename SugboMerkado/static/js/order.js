//orderList
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
    document.getElementById("datePurchased").value = temp;

    GrandTotalValue();
});

$('.btn-number').click(function(e){
    e.preventDefault();
    
    fieldName = $(this).attr('data-field');
    var num = fieldName.split('-')[1];
    type      = $(this).attr('data-type');
    var input = $("input[id='in-"+num+"']");
    var str1 = 'up-'+num;
    var str2 = 'tp-'+num;
    var str3 = 'tp-'+num+'-2';
    var unitPrice = document.getElementById(str1);
    var totalPrice = document.getElementById(str2);
    var totalInput = document.getElementById(str3);
    var currentVal = parseInt(input.val());
    var p1 = parseFloat(unitPrice.innerHTML.replace(',',''));
    if (!isNaN(currentVal)) {
        if(type == 'minus') {
            
            if(currentVal > input.attr('min')) {
                input.val(currentVal - 1).change();
                var p2 = parseFloat(p1*(currentVal-1))
                totalPrice.innerHTML = p2.toLocaleString();
                totalInput.value = p2;
            } 
            if(parseInt(input.val()) == input.attr('min')) {
                $(this).attr('disabled', true);
            }

        } else if(type == 'plus') {

            if(currentVal < input.attr('max')) {
                input.val(currentVal + 1).change();
                var p2 = parseFloat(p1*(currentVal+1))
                totalPrice.innerHTML = p2.toLocaleString();
                totalInput.value = p2;
            }
            if(parseInt(input.val()) == input.attr('max')) {
                $(this).attr('disabled', true);
            }

        }
    } else {
        input.val(0);
    }
    GrandTotalValue();
});

$('.input-number').focusin(function(){
   $(this).data('oldValue', $(this).val());
});

$('.input-number').change(function() {
    minValue =  parseInt($(this).attr('min'));
    maxValue =  parseInt($(this).attr('max'));
    valueCurrent = parseInt($(this).val());
    
    name = $(this).attr('id');
    var num = name.split('-')[1];
    if(valueCurrent >= minValue) {
        $(".btn-number[data-type='minus'][data-field='q-"+num+"']").removeAttr('disabled')
    } else {
        alert('Sorry, the minimum value was reached');
        $(this).val($(this).data('oldValue'));
    }
    if(valueCurrent <= maxValue) {
        $(".btn-number[data-type='plus'][data-field='q-"+num+"']").removeAttr('disabled')
    } else {
        alert('Sorry, the maximum value was reached');
        $(this).val($(this).data('oldValue'));
    }
    
    
});

$(".input-number").keydown(function (e) {
    // Allow: backspace, delete, tab, escape, enter and .

    if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 || (e.keyCode == 65 && e.ctrlKey === true) || (e.keyCode >= 35 && e.keyCode <= 39)) {
        // let it happen, don't do anything
        return;    
    }

    // Ensure that it is a number and stop the keypress
    if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
        e.preventDefault();
    }
});

function GrandTotalValue(){
    var x = document.getElementsByClassName('totalPrice');
    var total = 0;
    for(var i=0; i<x.length; i++){
        var p1 = parseFloat(x[i].innerHTML.replace(',',''));
        total = total + p1;
    }
    document.getElementById('grandTotal').innerHTML = "Php "+total.toLocaleString();
};