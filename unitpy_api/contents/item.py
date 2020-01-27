#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from urllib.parse import parse_qs
import mysqlDAO as DAO

############ item ############ 
############### get 
def get(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    ## パラメータチェック,パース,SQL生成
    try:
        ids = parse_qs(environ.get('QUERY_STRING'))['id']
        ids_str = ",".join(ids)
        sqlQuery = 'SELECT * FROM t_shoppinglist WHERE id in (' + ids_str + ');'
    except Exception as error:
        print(error)
        start_response('400 Bad request', [('Content-Type', 'text/html')])
        return [b"400 Bad request."]
    ## DB接続
    dao = DAO.PDAO()
    print(sqlQuery)
    result = dao.selectQuery(sqlQuery)
    ## レスポンス
    ## data = list(map(lambda row: {"id": row[0], "itemName": row[1], "quantity": row[2], "flag": row[3]}, result))
    ## response = json.dumps(data, ensure_ascii=False).encode('utf-8')
    response = json.dumps(result, ensure_ascii=False).encode('utf-8')
    return response

############### post 
def post(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    wsgi_input = environ["wsgi.input"]
    fromData = wsgi_input.read(int(environ.get('CONTENT_LENGTH', 0))).decode('utf-8')
    ## パラメータチェック,パース,SQL生成
    try:
        itemName = json.loads(fromData)['itemName']
        quantity = json.loads(fromData)['quantity']
        sqlQuery = 'INSERT INTO t_shoppinglist VALUES (NULL,"'+ str(itemName)+ '",'+ str(quantity) +',0);'
    except Exception as error:
        print(error)
        start_response('400 Bad request', [('Content-Type', 'text/html')])
        return [b"400 Bad request."]
    ## DB接続
    dao = DAO.PDAO()
    print(sqlQuery)
    dao.TransactionQuery(sqlQuery)
    return [b"200 OK."]

############### put 
def put(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    wsgi_input = environ["wsgi.input"]
    fromData = wsgi_input.read(int(environ.get('CONTENT_LENGTH', 0))).decode('utf-8')
    # 受信データのパース
    try:
        id = json.loads(fromData)['id']
        itemName = json.loads(fromData)['itemName']
        quantity = json.loads(fromData)['quantity']
        sqlQuery = 'UPDATE t_shoppinglist SET itemName="'+ str(itemName)+ '", quantity='+ str(quantity) +' WHERE id = '+ str(id)+';'
    except Exception as error:
        print(error)
        start_response('400 Bad request', [('Content-Type', 'text/html')])
        return [b"400 Bad request."]
    # DB接続
    dao = DAO.PDAO()
    print(sqlQuery)
    dao.TransactionQuery(sqlQuery)
    return [b"200 OK."]

############### delete
def delete(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    ## パラメータチェック,パース,SQL生成
    try:
        ids = parse_qs(environ.get('QUERY_STRING'))['id']
        ids_str = ",".join(ids)
        sqlQuery = 'UPDATE t_shoppinglist SET flag = 1 WHERE id in (' + ids_str + ');'
    except Exception as error:
        print(error)
        start_response('400 Bad request', [('Content-Type', 'text/html')])
        return [b"400 Bad request."]
    ## DB接続
    dao = DAO.PDAO()
    print(sqlQuery)
    result = dao.TransactionQuery(sqlQuery)
    return [b"200 OK."]