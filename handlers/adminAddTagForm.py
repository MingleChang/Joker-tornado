#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from models.models import Tag
from handlers.base import BaseHandler

class AdminAddTagFormHandler(BaseHandler):
    def get(self):
        content=self.get_argument('content','')
        code=self.get_argument('code','')
        self.addTag(content,code)

    def post(self):
        content=self.get_argument('content','')
        code=self.get_argument('code','')
        self.addTag(content,code)

    def addTag(self,content,code):
        if content=='' or code=='':
            self.render('admin/addtag.html',info='')
        elif code != 'mingle':
            self.render('admin/addtag.html',info='code error')
        else:
            self.insertTag(content)
    
    def checkTag(self,content):
        tags=self.db.query(Tag).filter(Tag.content==content)
        if tags.count()==0:
            return False
        else:
            return True

    def insertTag(self,content):
        if content=='':
            self.render('admin/addtag.html',info='')
        elif self.checkTag(content):
            self.render('admin/addtag.html',info='已存在')
        else:
            tag=Tag()
            tag.content=content
            tag.tagid=uuid.uuid1().hex
            self.db.add(tag)
            self.db.commit()
            self.db.close()

            self.render('admin/addtag.html',info='成功')
        