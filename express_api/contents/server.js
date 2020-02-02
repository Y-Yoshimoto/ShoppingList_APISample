'use strict';
// express,bodyParser読み込み
const express = require('express');
const bodyParser = require('body-parser');
//メール関連読み込み
var sendmail = require("./sendmail");

// express起動
const PORT = 8040;
const HOST = '0.0.0.0';
const app = express();

// urlencoded,jsonパース
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

// アプリケーション
app.get('/', (req, res) => {
    res.send('This is SendMail API.');
});

app.post('/sendmail', (req, res) => {
    console.log(req.body);
    //sendmail.send('root@localdomain', 'test@localdomain', 'This is TestMail.', 'This is TestMail.');
    sendmail.send(req.body.from, req.body.to, req.body.subject, req.body.text);
    res.send('/sendmail');
});


app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);