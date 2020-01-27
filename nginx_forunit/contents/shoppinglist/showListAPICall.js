//買い物リスト取得
$(function () {
    getShowList();
})

function getShowList() {
    $(function () {
        $.get({//get形式
            url: "../shoppinglist_api/showList",    //URL
            dataType: "json",                //受信データ
        }).done(function (rcv_data) {
            // 受信データ処理
            console.log("GET:showListAPI");
            $("#showLiset_th").empty();
            $("#input_ID").empty();
            console.log(rcv_data);
            for (let i of rcv_data) {
                //console.log(i);
                var row = makeItemRow(i);
                var id = '<option>' + Number(i['id']) + '</option>'
                //表データ追加
                $("#showLiset_th").append(row);
                $("#input_ID").append(id);
            }
            $("#getListMessage").text('更新: ' + GetDate());
            console.log(GetDate());
            console.log("END:showListAPI");
        }).fail(function (rcv_data, textStatus, errorThrown) {
            // エラー処理
            console.log(rcv_data);
            $("#getListMessage").text("サポートへご連絡ください。");
            //alert(errorThrown);
            console.log("ERROR");
        }).always(function () {
        })
    })
}

function makeItemRow(itemRow) {
    //console.log(UserRow);
    //権限表記変更
    var flag = FlagSet(itemRow['flag']);
    //List要素生成
    var row = '<tr><th scope="row">' + itemRow['id'] + '</th><td>' + itemRow['itemName'] + '</td><td>' + itemRow['quantity'] + '</td><td>' + flag + '</td></tr>';
    //console.log(row);
    return row;
}
//ステータス表示
function FlagSet(flag) {
    switch (Number(flag)) {
        case 0:
            return '';
        case 1:
            return '完了';
    }
}

function GetDate() {
    //現在時刻取得
    var date = new Date();
    return date.toLocaleString()
}
