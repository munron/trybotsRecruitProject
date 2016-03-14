var app=require('http').createServer(handler),
    fs =require('fs'),
    os=require('os'),
    sys=require('sys'),
    url = require('url'),
    qs = require('querystring'),
    serialport=require('serialport');


var yellow  = '\u001b[33m';
var reset   = '\u001b[0m';
var flag=0;

if(process.argv.length < 3) {
    console.error(yellow+'引数が足りていません'+reset);
    return;
}

var sp = new serialport.SerialPort(process.argv[2], {
    baudRate: 9600,
    dataBits: 8,
    parity: 'none',
    stopBits: 1,
    flowControl: false,
    parser: serialport.parsers.readline("\n")
});

setTimeout(function(){
    app.listen(1337);
    console.error("localhost:1337");
},3000);

function handler(req,res){
    if(req.url=="/"){
        fs.readFile(__dirname+'/index.html','utf-8',function(err,data){
	          res.writeHead(200);
	          res.write(data);
	          res.end();   
	      });
    }
   if(req.method=='GET') {
       var url_parts = url.parse(req.url,true);
       console.log(url_parts.query.dc);

       //緊急停止処理
       if(url_parts.query.dc == 2){
           sp.write('0',function(err,results){
               console.error(yellow+"緊急停止割り込み発生");
               console.error("err : "+ err + " ,result status : " + results + reset);
               if(results==1)console.error(yellow + "正常です" + reset) ;
           });
           flag=1;
       }
       
       //緊急停止解除処理
       if(url_parts.query.dc == 3){
           flag=0;
       }
       
       if(flag == 0){
           sp.write(url_parts.query.dc,function(err,results){
               console.error(yellow+"シリアル通信開始");
               console.error("err : "+ err + " ,result status : " + results + reset);
               if(results==1)console.error(yellow + "正常です" + reset) ;
           });
       }
	     fs.readFile(__dirname+'/index.html','utf-8',function(err,data){
	         res.writeHead(200);
	         res.write(data);
	         res.end();   
	     });
    }
}


sp.on('data', function(input) {
    console.error(input);
});
