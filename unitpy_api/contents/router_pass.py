#!/usr/bin/env python
# -*- coding: utf-8 -*-
import showList as showList
import item as item

## alive
def alive(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Unit for Wsgi is Up."]

## not_found
def not_found(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return [b"404 Not Found."]

routes = [
    ('/','GET', alive),
    ('/getList','GET', showList.getList),
    ('/product','GET', item.get),
    ('/product','POST', item.post),
    ('/product','PUT', item.put),
    ('/product','DELETE', item.delete),
]