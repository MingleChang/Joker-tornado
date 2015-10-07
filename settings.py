#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

DEBUG = True
LISTEN_PORT = 8000

#文件路径
BASH_PATH = os.path.dirname(__file__)
TEMPLATES_PATH = os.path.join(BASH_PATH, "templates")
STATIC_PATH = os.path.join(BASH_PATH, "static")

#数据库设置
DB_CONNECT_STRING = 'sqlite:///'+BASH_PATH+'/test.db'
# DB_CONNECT_STRING = 'mysql+mysqlconnector://root:890805@localhost:3306/test'
DB_ECHO = False
DB_ENCODING = 'utf-8'
POOL_RECYCLE = 5


settings=dict(
    template_path=TEMPLATES_PATH,
    static_path=STATIC_PATH,
    cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    xsrf_cookies=True,
    login_url="/login",
    debug=True
)