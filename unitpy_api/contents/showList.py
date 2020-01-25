#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
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
    data = list(map(lambda row: {"id": row[0], "商品": row[1], "価格": row[2], "flag": row[3]}, result))
    response = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return response