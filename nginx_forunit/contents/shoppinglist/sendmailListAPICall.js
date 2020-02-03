// 買い物リストのメール送信
$(function () {
    $('#sendmailList').click(function () {
        //多重送信防止ボタン無効化
        var button = $(this);
        button.attr('disabled', true);
        // 送信データ生成
        var sed_data = {
            'to': String($('#toMail').val())
        }
        console.log('SendmailList')
        console.log(sed_data)
        //Ajax通信
        $.post({
            url: '../shoppinglist_api/sendmailList',
            data: JSON.stringify(sed_data),
            contentType: 'application/JSON',
            dataType: 'text'
        }).done(function (rcv_data) {
            console.log(rcv_data);
        }).fail(function (rcv_data, textStatus, errorThrown) {
            //エラー処理
            console.log(rcv_data);
            $("#getListMessage").text("サポートへご連絡ください。");
            console.log("ERROR");
        }).always(function () {
            //ボタンの再有効化
            button.attr("disabled", false);
        })
    })
})