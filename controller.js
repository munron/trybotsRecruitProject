var ejs=require('ejs');
var os =require('os');
var exec=require('child_process').exec;
var app=require('http').createServer(handler),
    io=require('socket.io').listen(app),
    fs =require('fs');
app.listen(1337);

var template=fs.readFileSync(__dirname + '/index.ejs','utf-8');
var ipaddr=os.networkInterfaces().eth0[0].address;
//console.log("local ip address" + ipaddr);

function handler(req,res){
    var html=ejs.render(template,{
	ipaddr:ipaddr
    });
    res.writeHead(200);
    res.write(html);
    res.end();    
}

/*
function handler(req,res){
    fs.readFile(__dirname + '/index.html',function(err,data){
        if(err){
            res.writeHead(500);
            return res.end('Error');
            }
	res.writeHead(200);
	res.write(data);
        res.end();
    
    });
}
*/

var default_parameter=io.of('/default_parameter').on('connection',function(socket){
    socket.on('initial', function(data) {
        //console.log(data);
        fs.readFile("./setting.txt",'utf-8',function(err,text){
            if(err) throw err;
            //console.log(text);
            socket.emit("default_text",text);            
        });
        
    });
});

var parameter=io.of('/parameter').on('connection',function(socket){
    socket.on('message', function(data) {
        //console.log(data);
        fs.writeFile("./setting.txt",JSON.stringify(data),function(err){
            if(err) throw err;
            //console.log("パラメーターをsetting.txtに上書きしました");
        });
    });
});


var signal=io.of('/signal').on('connection',function(socket){
    socket.on('signal', function(data) {
        //console.log("signal="+data);
	console.log(data);        
    });
});


