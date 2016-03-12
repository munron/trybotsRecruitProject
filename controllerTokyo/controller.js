var app=require('http').createServer(handler),
    io=require('socket.io').listen(app),
    fs =require('fs'),
    os=require('os'),
    exec = require('child_process').exec,
    serialport=require('serialport');
app.listen(1337);

// Serial Port
var array;
var portName;
var sp;
var startFlag=0;

function serialInit(){
    sp = new serialport.SerialPort(portName, {
	    baudRate: 115200,
	    dataBits: 8,
	    parity: 'none',
	    stopBits: 1,
	    flowControl: false,
	    parser: serialport.parsers.readline("\n")
	});
}

function handler(req,res){
    var url = req.url;
    if ('/' == url){
	fs.readFile(__dirname+'/index.html','UTF-8',function(err,data){
		res.writeHead(200,{'Content-Type': 'text/html'});
		res.write(data);
		res.end();
		/*
		sp.write("a", function(err, results){
      			console.log("アクセスを検知..シリアル通信開始");
			console.log("err : "+ err + " ,result status : " + results);
			if(results==1)console.log("正常です");
			
		    });
		*/
		child = exec('ls /dev/{cu,tty}.*',function (error, stdout, stderr) {
			array=new Array(stdout.split(/\r\n|\r|\n/));
			console.log('stdout: ' + array);
			console.log('stderr: ' + stderr);
			if (error !== null) {
			    console.log('exec error: ' + error);
			}
		    });		
	    });
    } else if ('/test.js' == url) {
	fs.readFile(__dirname+'/test.js', 'UTF-8', function (err, data) {
		res.writeHead(200);
		res.write(data);
		res.end();
	    });
    }else if('/jquery-1.11.1.min.js'==url){
	fs.readFile(__dirname+'/jquery-1.11.1.min.js', 'UTF-8', function (err, data) {
                res.writeHead(200, {'Content-Type': 'text/plain'});
                res.write(data);
                res.end();
            });	
    }else if('/trybots.jpg'==url){
	fs.readFile('trybots.jpg',function(err,data){
                res.writeHead(200, {'Content-Type': 'mage/jpeg'});
                res.write(data);
                res.end();
	    });
    }
}

var portData=io.of('/portData').on('connection',function(socket){
	socket.json.emit("portData",array);
	socket.on("portData",function(data){
		console.log(data);
		portName=data;
		serialInit();
		serialFlag=1;
	    });
    });

var fliperData=io.of('/fliperData').on('connection',function(socket){

	sp.on('data', function(input) {
		var jsonData = JSON.parse(input);
		if(jsonData.type=="fliper"){
		    socket.json.emit("fliperData",jsonData);
		}	
	    });

    });

var hmdData=io.of('/hmdData').on('connection',function(socket){

	    sp.on('data', function(input) {
		    var jsonData = JSON.parse(input);
		    if(jsonData.type=="hmd"){
			//console.log(jsonData);
			socket.json.emit("hmdData",jsonData);
		    }	
		});

    });




