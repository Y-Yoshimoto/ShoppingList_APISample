# Unitのセットアップについて

## テストリクエスト
### GET 
    curl -v -X GET 'http://127.0.0.1/shoppinglist_api/product?id=1&id=2'
### POST
    curl -v -X POST 'http://127.0.0.1/shoppinglist_api/product' \
  -H 'Content-Type: application/json' -d '{"productName":"イカ","price":"200"}'
      curl -v -X POST 'http://127.0.0.1/shoppinglist_api/product' \
  -H 'Content-Type: application/json' -d '{"productName":"たこ","price":"500"}'

### PUT
      curl -v -X PUT 'http://127.0.0.1/shoppinglist_api/product' \
  -H 'Content-Type: application/json' -d '{"id":"5","productName":"まだこ","price":"700"}'
        curl -v -X PUT 'http://127.0.0.1/shoppinglist_api/product' \
  -H 'Content-Type: application/json' -d '{"id":"1","productName":"やぎ","price":"1700"}'

### DELETE
    curl -v -X DELETE 'http://127.0.0.1/shoppinglist_api/product?id=3'
    curl -v -X DELETE 'http://127.0.0.1/shoppinglist_api/product?id=5'

