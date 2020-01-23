#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from urllib.parse import parse_qs
import mysqlDAO as DAO

def get(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Unit for Wsgi is Up.   Ver 0.1"]


def not_found(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return [b"404 Not Found."]

### 全体表示
def getList(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    # データベースコネクション
    dao = DAO.PDAO()
    dao.connectDB()
    # SQLリクエスト
    sqlQuery = 'SELECT * FROM t_shoppinglist WHERE deleteFlag = 0;'
    result = dao.selectQuery(sqlQuery)
    dao.closeDB()
    # レスポンスデータ生成
    list =[]
    for row in result:
        list.append({"id":row[0], "商品":row[1], "価格":row[2], "Flag":row[3]})
        response = json.dumps(list, ensure_ascii=False, indent=4).encode('utf-8')
    return response
def getAllList(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    # データベースコネクション
    dao = DAO.PDAO()
    dao.connectDB()
    # SQLリクエスト
    sqlQuery = 'SELECT * FROM t_shoppinglist;'
    result = dao.selectQuery(sqlQuery)
    dao.closeDB()
    # レスポンスデータ生成
    list =[]
    for row in result:
        list.append({"id":row[0], "商品":row[1], "価格":row[2], "Flag":row[3]})
        response = json.dumps(list, ensure_ascii=False, indent=4).encode('utf-8')
    return response


### 個別操作API
def product(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    ## GET
    if method == 'GET':
        start_response('200 OK', [('Content-Type', 'application/json')])
        ids = parse_qs(environ.get('QUERY_STRING'))['id']
        # データベースコネクション
        dao = DAO.PDAO()
        dao.connectDB()
        list = []
        # レスポンスデータ生成
        for id in ids:
            sqlQuery = 'SELECT * FROM t_shoppinglist WHERE id = ' + id + ';'
            row = dao.selectQuery(sqlQuery)
            print(row)
            list.append({"id":row[0][0], "商品":row[0][1], "価格":row[0][2], "Flag":row[0][3]})
        response = json.dumps(list, ensure_ascii=False).encode('utf-8')
        dao.closeDB()


    ## POST
    elif method == 'POST':
        start_response('200 OK', [('Content-Type', 'application/json')])
        wsgi_input = environ["wsgi.input"]
        # 受信データのパース
        fromData = wsgi_input.read(int(environ.get('CONTENT_LENGTH', 0))).decode('utf-8')
        productName = json.loads(fromData)['productName']
        price = json.loads(fromData)['price']
        # データベースコネクション
        dao = DAO.PDAO()
        dao.connectDB()
        sqlQuery = 'INSERT INTO t_shoppinglist VALUES (NULL,"'+ str(productName)+ '",'+ str(price) +',0);'
        print(sqlQuery)
        dao.InsertQuery(sqlQuery)
        dao.closeDB()
        response = [b"200 OK."]
        
    ## PUT
    elif method == 'PUT':
        start_response('200 OK', [('Content-Type', 'application/json')])
        wsgi_input = environ["wsgi.input"]
        # 受信データのパース
        fromData = wsgi_input.read(int(environ.get('CONTENT_LENGTH', 0))).decode('utf-8')
        id = json.loads(fromData)['id']
        productName = json.loads(fromData)['productName']
        price = json.loads(fromData)['price']
        # データベースコネクション
        dao = DAO.PDAO()
        dao.connectDB()
        sqlQuery = 'UPDATE t_shoppinglist SET productName="'+ str(productName)+ '", price='+ str(price) +' WHERE id = '+ str(id)+';'
        print(sqlQuery)
        dao.UpdateQuery(sqlQuery)
        dao.closeDB()
        response = [b"200 OK."]

    ## DELETE
    elif method == 'DELETE':
        start_response('200 OK', [('Content-Type', 'application/json')])
        ids = parse_qs(environ.get('QUERY_STRING'))['id']
        # データベースコネクション
        dao = DAO.PDAO()
        dao.connectDB()
        list = []
        # データ削除
        for id in ids:
            sqlQuery = 'UPDATE t_shoppinglist SET deleteFlag = 1 WHERE id = '+ str(id)+';'
            row = dao.DeleteQuery(sqlQuery)
        dao.closeDB()
        response = [b"200 OK."]

    else: 
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        response = [b"404 Not Found."]        

    return response
