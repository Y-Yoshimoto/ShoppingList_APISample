#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from urllib.parse import parse_qs
import mysqlDAO as DAO


############ showList ############
def getList(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    # データベースコネクション
    dao = DAO.PDAO()
    if len(environ.get('QUERY_STRING')) > 0:
        flag = parse_qs(environ.get('QUERY_STRING'))['flag']
        flag_str = ",".join(flag)
        sqlQuery = 'SELECT * FROM t_shoppinglist WHERE flag in (' + flag_str + ');'
    else:
        sqlQuery = 'SELECT * FROM t_shoppinglist;'
    # SQLリクエスト
    print(sqlQuery)
    result = dao.selectQuery(sqlQuery)

    # レスポンスデータ生成
    ## data = list(map(lambda row: {"id": row[0], "itemName": row[1], "quantity": row[2], "flag": row[3]}, result))
    ## response = json.dumps(data, ensure_ascii=False).encode('utf-8')
    response = json.dumps(result, ensure_ascii=False).encode('utf-8')
    return response


def sendmailList(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    wsgi_input = environ["wsgi.input"]
    fromData = wsgi_input.read(int(environ.get('CONTENT_LENGTH', 0))).decode('utf-8')
    ## パラメータチェック,パース,SQL生成
    try:
        toMail = json.loads(fromData)['to']
        print(toMail)
        ## リスト取得,パース
        dao = DAO.PDAO()
        sqlQuery = 'SELECT * FROM t_shoppinglist WHERE flag in (0);'
        result = dao.selectQuery(sqlQuery)
        message = '|商品 |数量 |\n' + "\n".join(list(map(lambda item: '|' + item['itemName'] + ' |' + item['quantity'] + '|', result)))
        print(str(message))

        ## メール送信
        url = 'http://express_api:8040/sendmail'
        message = {'from': 'SoppingList@SoppingList.com','to': toMail,'subject': '買い物リスト','text': str(message)}
        response = requests.post(url, json=message)        
        print(response.status_code)

    except Exception as error:
        print(error)
        start_response('500 Internal Server Error.', [('Content-Type', 'text/html')])
        return [b"500 Internal Server Error."]
    response = [b"200 sendmail."]
    return response