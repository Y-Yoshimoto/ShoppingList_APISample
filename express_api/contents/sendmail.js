//モジュールの読み込み
var nodemailer = require("nodemailer");

//SMTP指定_25
var smtp25 = nodemailer.createTransport({
    host: 'shoppinglist_apisample_mail_1',
    port: 25
});
/*SMTP指定_587
var smtp25 = nodemailer.createTransport({
    host: 'shoppinglist_apisample_mail_1',
    port: 587,
    secire: true,
    auth: {
        user: 'root',
        pass: 'password'
    }
});*/


exports.send = function (fromArg, toArg, subjectArg, textArg) {
    //メール情報の作成
    var message = {
        from: fromArg,
        to: toArg,
        subject: subjectArg,
        text: textArg
    };
    // メール送信
    try {
        smtp25.sendMail(message, function (error, info) {
            if (error) {
                console.log("sendmail failed");
                console.log(error.message);
                return;
            }
            // 送信成功
            console.log("sendmail successful");
            console.log(info.messageId);
        });
    } catch (e) {
        console.log("Error", e);
    }
};




