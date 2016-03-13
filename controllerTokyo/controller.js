var app=require('http').createServer(handler),
    io=require('socket.io').listen(app),
    fs =require('fs'),
    os=require('os'),
    exec = require('child_process').exec,
    serialport=require('serialport');

if(process.argv.length < 3) {
    console.log('引数が足りていません');
    return;
}

var sp = new serialport.SerialPort(process.argv[2], {
	baudRate: 115200,
	dataBits: 8,
	parity: 'none',
	stopBits: 1,
	flowControl: false,
	parser: serialport.parsers.readline("\n")
    });

setTimeout(function(){
	app.listen(1337);
	console.error("try connecting .....")
	sp.write("a", function(err, results){
		console.error("アクセスを検知..シリアル通信開始");
		console.error("err : "+ err + " ,result status : " + results);
		if(results==1)console.error("正常です");
	    });
    },3000);

function handler(req,res){
    var url = req.url;
    if ('/' == url){
	fs.readFile(__dirname+'/index.html','UTF-8',function(err,data){
		res.writeHead(200,{'Content-Type': 'text/html'});
		res.write(data);
		res.end();
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

var sensorData=io.of('/sensorData').on('connection',function(socket){
    });

sp.on('data', function(input) {
	try{
	    var jsonData = JSON.parse(input);
	    console.log(jsonData);		    
	    if(jsonData.type=="fliper"){
		sensorData.json.emit("fliperData",jsonData);
	    }else if(jsonData.type=="hmd"){
		sensorData.json.emit("hmdData",jsonData);
		    }	
	}catch(e){
	    console.error("error : " + e);
	}
    });




