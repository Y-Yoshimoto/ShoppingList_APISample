#!/usr/bin/env python
# -*- coding: utf-8 -*-
import router_func as rfunc

routes = [
    ('/', rfunc.get),
    ('/getList', rfunc.getList),
    ('/product', rfunc.product),
    ('/getAllList', rfunc.getAllList),
]
