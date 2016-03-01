console.log("ok");

for(var i=2;i<=12;i++){
    $('.parameter_dive #select_head').append($('<option>').html(i).val(i));
    console.log(i);
}

for(var i=2;i<=12;i++){
    $('.parameter_left #select_head').append($('<option>').html(i).val(i));
    console.log(i);
}

for(var i=2;i<=12;i++){
    $('.parameter_right #select_head').append($('<option>').html(i).val(i));
    console.log(i);
}

