var express = require('express');
var app = express();
var toubiao = require('./sign');

// 获取头条 _signature 参数
app.get('/toutiao', function (req, res) {
    var nonce = req.query["nonce"].toString();
    var url = req.query["url"].toString();
    var userAgent = req.query["userAgent"].toString();
    result = toubiao.get_sign(nonce, url, userAgent);
    if (result) {
        res.send(result);
    } else {
        res.send('keys未生成!');
    }
});

var server = app.listen(8000);
console.log("server running http://127.0.0.1:8000");