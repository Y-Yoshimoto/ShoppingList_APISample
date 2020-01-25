# Unitのセットアップについて

## showListテストリクエスト
### GET 
    curl -v -X GET 'http://127.0.0.1/shoppinglist_api/showList'
    curl -v -X GET 'http://127.0.0.1/shoppinglist_api/showList?flag=0'
    curl -v -X GET 'http://127.0.0.1/shoppinglist_api/showList?flag=1'
    curl -v -X GET 'http://127.0.0.1/shoppinglist_api/showList?flag=1&flag=2'

## itemテストリクエスト
### GET 
    curl -v -X GET 'http://127.0.0.1/shoppinglist_api/item?id=1&id=2'
### POST
    curl -v -X POST 'http://127.0.0.1/shoppinglist_api/item' \
    -H 'Content-Type: application/json' -d '{"itemName":"イカ","price":"200"}'
    curl -v -X POST 'http://127.0.0.1/shoppinglist_api/item' \
    -H 'Content-Type: application/json' -d '{"itemName":"たこ","price":"500"}'

### PUT
    curl -v -X PUT 'http://127.0.0.1/shoppinglist_api/item' \
    -H 'Content-Type: application/json' -d '{"id":"5","itemName":"まだこ","price":"700"}'
    curl -v -X PUT 'http://127.0.0.1/shoppinglist_api/item' \
    -H 'Content-Type: application/json' -d '{"id":"1","itemName":"やぎ","price":"1700"}'

### DELETE
    curl -v -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=3'
    curl -v -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=5'

