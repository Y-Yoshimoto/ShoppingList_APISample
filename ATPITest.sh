#bin/bash
## showListテストリクエスト
echo 'showList'
curl -X GET 'http://127.0.0.1/shoppinglist_api/showList'
curl -X GET 'http://127.0.0.1/shoppinglist_api/showList?flag=1&flag=2'

## itemテストリクエスト
### GET 
echo '\n\n item GET'
curl -X GET 'http://127.0.0.1/shoppinglist_api/item?id=1&id=2'
### POST
echo '\n\n item POST'
curl -X POST 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"itemName":"イカ","quantity":"200"}'
curl -X POST 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"itemName":"たこ","quantity":"500"}'

### PUT
echo '\n\n item PUT'
curl -X PUT 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"id":"5","itemName":"まだこ","quantity":"700"}'
curl -X PUT 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"id":"1","itemName":"やぎ","quantity":"1700"}'

### DELETE
echo '\n\n item DELETE'
curl -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=3'
curl -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=5'

## showListテストリクエスト
echo 'showList'
curl -X GET 'http://127.0.0.1/shoppinglist_api/showList'