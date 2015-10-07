#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from models.models import init_db,update_db

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from settings import settings,LISTEN_PORT,DB_CONNECT_STRING,DB_ECHO,DB_ENCODING,POOL_RECYCLE
from urls import url_patterns

from tornado.options import define, options

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(url_patterns, **settings)
        #数据库
        engine = create_engine(DB_CONNECT_STRING,encoding=DB_ENCODING, echo=DB_ECHO)
        self.db = scoped_session(sessionmaker(bind=engine))
        init_db(engine)#初始化数据库
        
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(LISTEN_PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()