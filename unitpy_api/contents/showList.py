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
    # dao.connectDB()
    # SQLリクエスト
    # sqlQuery = 'SELECT * FROM t_shoppinglist WHERE deleteFlag = 0;'
    sqlQuery = 'SELECT * FROM t_shoppinglist;'
    result = dao.selectQuery(sqlQuery)
    # dao.closeDB()
    # レスポンスデータ生成
    list = []
    for row in result:
        list.append({"id": row[0], "商品": row[1], "価格": row[2], "Flag": row[3]})
        response = json.dumps(list, ensure_ascii=False,
                              indent=4).encode('utf-8')
    return response