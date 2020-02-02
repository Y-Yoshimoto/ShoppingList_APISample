//GET
$(function () {
    $('#itemGET').click(function () {
        //多重送信防止//ボタンの無効化
        var button = $(this);
        button.attr("disabled", true);
        $.get({//get形式
            url: "../shoppinglist_api/item",    //URL
            data: { 'id': String($("#input_ID").val()) },
            dataType: "json"               //受信データ
        }).done(function (rcv_data) {
            // 受信データ処理
            console.log("START:itemGET");
            console.log(rcv_data);
            $("#input_itemName").val(rcv_data[0]['itemName']);
            $("#input_quantity").val(rcv_data[0]['quantity']);
            console.log("END:itemGET");
        }).fail(function (rcv_data, textStatus, errorThrown) {
            // エラー処理
            console.log(rcv_data);
            $("#getListMessage").text("サポートへご連絡ください。");
            //alert(errorThrown);
            console.log("ERROR");
        }).always(function () {
            //ボタンの再有効化
            button.attr("disabled", false);
        })
    })
})

//POST
$(function () {
    $('#itemPOST').click(function () {
        //多重送信防止//ボタンの無効化
        var button = $(this);
        button.attr("disabled", true);
        //　JSON形式に変形
        var sed_data = {
            'itemName': String($("#input_itemName").val()),
            'quantity': String($("#input_quantity").val()),
        }
        console.log("POST: itemPOST");
        console.log(sed_data)
        // Ajax通信
        $.post({//POST形式
            url: "../shoppinglist_api/item",    //URL
            data: JSON.stringify(sed_data),   //送信JSONデータ
            contentType: 'application/JSON',
            dataType: "text",                //受信データ
        }).done(function (rcv_data) {
            // 受信データ処理
            console.log(rcv_data);
        }).fail(function (rcv_data, textStatus, errorThrown) {
            // エラー処理
            console.log(rcv_data);
            $("#getListMessage").text("サポートへご連絡ください。");
            //alert(errorThrown);
            console.log("ERROR");
        }).always(function () {
            //ボタンの再有効化
            button.attr("disabled", false);
            getShowList();
        })
    })
})

//PUT
$(function () {
    $('#itemPUT').click(function () {
        //多重送信防止//ボタンの無効化
        var button = $(this);
        button.attr("disabled", true);
        //　JSON形式に変形
        var sed_data = {
            'id': String($("#input_ID").val()),
            'itemName': String($("#input_itemName").val()),
            'quantity': String($("#input_quantity").val()),
        }
        console.log("PUT: itemPUT");
        console.log(sed_data)
        // Ajax通信
        $.ajax({//PUT形式
            type: "PUT",
            url: "../shoppinglist_api/item",    //URL
            data: JSON.stringify(sed_data),   //送信JSONデータ
            contentType: 'application/JSON',
            dataType: "text",                //受信データ
        }).done(function (rcv_data) {
            // 受信データ処理
            console.log(rcv_data);
        }).fail(function (rcv_data, textStatus, errorThrown) {
            // エラー処理
            console.log(rcv_data);
            $("#getListMessage").text("サポートへご連絡ください。");
            //alert(errorThrown);
            console.log("ERROR");
        }).always(function () {
            //ボタンの再有効化
            button.attr("disabled", false);
            getShowList();
        })
    })
})

//DELETE
$(function () {
    $('#itemDELETE').click(function () {
        //多重送信防止//ボタンの無効化
        var button = $(this);
        var sed_data = {
            'id': String($("#input_ID").val()),
        }
        button.attr("disabled", true);
        $.ajax({//DELETE
            type: "DELETE",
            url: "../shoppinglist_api/item",    //URL
            data: JSON.stringify(sed_data),   //送信JSONデータ
            contentType: 'application/JSON',
            dataType: "text"               //受信データ
        }).done(function (rcv_data) {
            // 受信データ処理
            console.log("START:itemDELETE");
            console.log(rcv_data);
            console.log("END:itemDELETE");
        }).fail(function (rcv_data, textStatus, errorThrown) {
            // エラー処理
            console.log(rcv_data);
            $("#getListMessage").text("サポートへご連絡ください。");
            //alert(errorThrown);
            console.log("ERROR");
        }).always(function () {
            //ボタンの再有効化
            button.attr("disabled", false);
            getShowList();
        })
    })
})