var app=require('http').createServer(handler),
    io=require('socket.io').listen(app),
    fs =require('fs'),
    os=require('os');
    readline = require('readline'),
    rl = readline.createInterface(process.stdin, process.stdout);
app.listen(1337);

var yellow  = '\u001b[33m';
var reset   = '\u001b[0m';

function handler(req,res){
    var url = req.url;
    if ('/' == url){
	fs.readFile(__dirname+'/index.html','UTF-8',function(err,data){
		res.writeHead(200,{'Content-Type': 'text/html'});
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

rl.on('line', function (input) {
	try{
	    var jsonData = JSON.parse(input);
	    //console.log("%j",jsonData);		    
	    if(jsonData.type=="fliper"){
		sensorData.json.emit("fliperData",jsonData);
	    }else if(jsonData.type=="hmd"){
		sensorData.json.emit("hmdData",jsonData);
		    }	
	}catch(e){
	    console.error("error : " + e);
	}
    });






