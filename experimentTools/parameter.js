//サーボモーターの可動範囲を設定
//-------------------------------
for(var i=2;i<=12;i++){
    $('.parameter_dive #select_head').append($('<option>').html(i).val(i));

}

for(var i=2;i<=12;i++){
    $('.parameter_left #select_head').append($('<option>').html(i).val(i));

}

for(var i=2;i<=12;i++){
    $('.parameter_right #select_head').append($('<option>').html(i).val(i));

}
//-------------------------------
for(var i=2;i<=12;i++){
    $('.parameter_dive #select_tail').append($('<option>').html(i).val(i));

}

for(var i=2;i<=12;i++){
    $('.parameter_left #select_tail').append($('<option>').html(i).val(i));

}

for(var i=2;i<=12;i++){
    $('.parameter_right #select_tail').append($('<option>').html(i).val(i));

}
//-------------------------------
for(var i=2;i<=12;i++){
    $('.parameter_dive #select_foot').append($('<option>').html(i).val(i));
}

for(var i=2;i<=12;i++){
    $('.parameter_left #select_foot').append($('<option>').html(i).val(i));
}

for(var i=2;i<=12;i++){
    $('.parameter_right #select_foot').append($('<option>').html(i).val(i));
}
//--------------------------------

//パラメーター情報
var parameter         = io.connect('http://192.168.2.75:1337/parameter');
//パラメーター初期値情報
var default_parameter = io.connect('http://192.168.2.75:1337/default_parameter');
//指令情報
var signal            = io.connect('http://192.168.2.75:1337/signal');

default_parameter.emit("initial","initial");
default_parameter.on("default_text",function(data){
    $("#log").append($('<h5>').text("default parameter received"));
    $("#log").append($('<h5>').text(data));
    var data=JSON.parse(data);
    console.log(data);

    //初期値の設定
    $('.parameter_dive #select_head').val(data.dive_head);
    $('.parameter_dive #select_tail').val(data.dive_tail);
    $('.parameter_dive #select_foot').val(data.dive_foot);
    $('.parameter_left #select_head').val(data.left_head);
    $('.parameter_left #select_tail').val(data.left_tail);
    $('.parameter_left #select_foot').val(data.left_foot);
    $('.parameter_right #select_head').val(data.right_head);
    $('.parameter_right #select_tail').val(data.right_tail);
    $('.parameter_right #select_foot').val(data.right_foot);
});

$("#forward").mousedown(function(e){
    console.log("forward clicked");
    var date=new Date()
    signal.emit("signal",1);
    $("#log").append($('<h5>').text(date+" : forward (signal=1)"));

});

$("#left").mousedown(function(e){
    console.log("left clicked");
    var date=new Date()
    signal.emit("signal",2);
    $("#log").append($('<h5>').text(date+" : left (signal=2)"));
});

$("#dive").mousedown(function(e){
    console.log("dive clicked");
    var date=new Date()
    signal.emit("signal",3);
    $("#log").append($('<h5>').text(date+" : dive (signal=3)"));
});


$("#right").mousedown(function(e){
    console.log("right clicked");
    var date=new Date()
    signal.emit("signal",4);
    $("#log").append($('<h5>').text(date+" : right (signal=4)"));
});

//パラメーターをサーバーに送信
$("#set").mousedown(function(e){
    var param={dive_head:$('.parameter_dive #select_head').val(),
	       dive_tail:$('.parameter_dive #select_tail').val(),
	       dive_foot:$('.parameter_dive #select_foot').val(),
	       left_head:$('.parameter_left #select_head').val(),
	       left_tail:$('.parameter_left #select_tail').val(),
	       left_foot:$('.parameter_left #select_foot').val(),
	       right_head:$('.parameter_right #select_head').val(),
	       right_tail:$('.parameter_right #select_tail').val(),
	       right_foot:$('.parameter_right #select_foot').val()};

    parameter.json.emit("message",param)
    $("#log").append($('<h5>').text("ファイルに設定を書き込みます"));
    $("#log").append($('<h5>').text(JSON.stringify(param)));

});

var width=$('.controller').width();
var height=$('body').height();
console.log("width : "+width);
console.log("height : "+height);
$("#forward").css({'width':width/5,'height':width/5,'margin-left':width*2/5-15,'padding':'0px'});
$("#left").css({'width':width/5,'height':width/5,'margin-left':width/10-15});
$("#dive").css({'width':width/5,'height':width/5,'margin-left':width/10});
$("#right").css({'width':width/5,'height':width/5,'margin-left':width/10});
$("#log").css({'width':width*0.9,'height':height});
$(".box").css({'width':width/3});
$("#set").css({'width':width/3,'height':'40px','margin-left':width/3+6,'margin-top':'20px'});
