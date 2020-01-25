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
    ('/showList','GET', showList.getList),
    ('/item','GET', item.get),
    ('/item','POST', item.post),
    ('/item','PUT', item.put),
    ('/item','DELETE', item.delete),
]