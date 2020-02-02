//メール送信API
$(function () {
    $('#sendmailAPICall').click(function () {
        //多重送信防止//ボタンの無効化
        var button = $(this);
        button.attr("disabled", true);
        //　JSON形式に変形
        var sed_data = {
            'from': 'root@localdomain',
            'to': String($("#toMail").val()),
            'subject': String($("#subjectMail").val()),
            'text': String($("#textMail").val()),
        }
        console.log("sendmail");
        console.log(sed_data)
        // Ajax通信
        $.post({//POST形式
            url: "../sendmail_api/sendmail",    //URL
            data: sed_data,   //送信JSONデータ
            dataType: "text",                //受信データ
        }).done(function (rcv_data) {
            // 受信データ処理
            console.log(rcv_data);
            $('.SysMessage').css('color', '#D9534F');
            $("#SysMessage").text("送信しました。");

            console.log("END");
        }).fail(function (rcv_data, textStatus, errorThrown) {
            // エラー処理
            console.log(rcv_data);
            $('.SysMessage').css('color', '#D9534F');
            $("#SysMessage").text("サポートへご連絡ください。");
            //alert(errorThrown);
        }).always(function () {
            //ボタンの再有効化
            button.attr("disabled", false);
        })
    })
});
