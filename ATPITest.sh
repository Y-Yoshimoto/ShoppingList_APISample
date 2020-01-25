#bin/bash
## showListテストリクエスト
echo 'showList'
curl -X GET 'http://127.0.0.1/shoppinglist_api/showList'
curl -X GET 'http://127.0.0.1/shoppinglist_api/showList?flag=1&flag=2'

## itemテストリクエスト
### GET 
echo 'item GET'
curl -X GET 'http://127.0.0.1/shoppinglist_api/item?id=1&id=2'
### POST
echo 'item POST'
curl -X POST 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"itemName":"イカ","price":"200"}'
curl -X POST 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"itemName":"たこ","price":"500"}'

### PUT
echo 'item PUT'
curl -X PUT 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"id":"5","itemName":"まだこ","price":"700"}'
curl -X PUT 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"id":"1","itemName":"やぎ","price":"1700"}'

### DELETE
echo 'item DELETE'
curl -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=3'
curl -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=5'

