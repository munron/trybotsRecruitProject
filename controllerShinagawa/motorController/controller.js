var app=require('http').createServer(handler),
    fs =require('fs'),
    os=require('os'),
    sys=require('sys'),
    url = require('url'),
    qs = require('querystring');
app.listen(1337);

var yellow  = '\u001b[33m';
var reset   = '\u001b[0m';

function handler(req,res){
   if(req.method=='GET') {
       var url_parts = url.parse(req.url,true);
       console.log(url_parts.query.dc);
	fs.readFile(__dirname+'/index.html','utf-8',function(err,data){
	    res.writeHead(200);
	    res.write(data);
	    res.end();   
	});
    }
}
