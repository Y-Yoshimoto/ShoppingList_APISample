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
curl -X POST 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"itemName":"イカ","quantity":"1杯"}'
curl -X POST 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"itemName":"たこ","quantity":"5匹"}'

### PUT
echo '\n\n item PUT'
curl -X PUT 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"id":"5","itemName":"まだこ","quantity":"5匹"}'
curl -X PUT 'http://127.0.0.1/shoppinglist_api/item' -H 'Content-Type: application/json' -d '{"id":"1","itemName":"やぎ","quantity":"17頭"}'

### DELETE
echo '\n\n item DELETE'
curl -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=3'
curl -X DELETE 'http://127.0.0.1/shoppinglist_api/item?id=5'

## showListテストリクエスト
echo 'showList'
curl -X GET 'http://127.0.0.1/shoppinglist_api/showList'


## Sendmailテスト
curl -X POST 'http://127.0.0.1/sendmail_api/sendmail' -H 'Content-Type: application/json' -d '{"from":"root@localdomain","to":"test@localdomain","subject":"TestMail","text":"This is TestMail."}'
