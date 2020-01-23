#!/usr/bin/env python
# coding:utf-8
import json
import mysql.connector as mydb

# 接続先データベース情報
class PDAO:
    def __init__(self):
        self.connector = mydb.connect(
                        host='shoppinglist_apisample_unit_mariadb_1',
                        port=3306,
                        database='shoppinglist',
                        user='shoppinglistUser',
                        password='Password',
                        charset='utf8'
                        )

# 接続
    def connectDB(self):
        self.cursor = self.connector.cursor()

# 切断
    def closeDB(self):
        self.cursor.close()
        self.connector.close()

# Query
    def selectQuery(self,sqlQuery):
        self.cursor = self.connector.cursor()
        # SQL生成
        self.cursor.execute(sqlQuery)
        return self.cursor.fetchall()

    def InsertQuery(self,sqlQuery):
        self.cursor = self.connector.cursor()
        # SQL生成
        self.cursor.execute(sqlQuery)
        self.connector.commit()
        return "0"

    def UpdateQuery(self,sqlQuery):
        self.cursor = self.connector.cursor()
        # SQL生成
        self.cursor.execute(sqlQuery)
        self.connector.commit()
        return "0"

    def DeleteQuery(self,sqlQuery):
        self.cursor = self.connector.cursor()
        # SQL生成
        self.cursor.execute(sqlQuery)
        self.connector.commit()
        return "0"