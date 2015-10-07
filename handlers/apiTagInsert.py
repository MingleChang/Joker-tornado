#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
# import json
# from sqlalchemy.orm import class_mapper
from models.models import Tag
from handlers.api import APIHandler

class APITagInsertHandler(APIHandler):
    def get(self):
        content=self.get_argument('content','')
        self.tagInsert(content)
        
    def post(self):
        content=self.get_argument('content','')
        self.tagInsert(content)

    def checkTag(self,content):
        if content=='':
            self.status=201
            self.message='content不能为空'
            return True
        tags=self.db.query(Tag).filter(Tag.content==content)
        if tags.count()==0:
            return False
        else:
            self.status=201
            self.message='该tag已存在'
            return True

    def tagInsert(self,content):
        if self.checkTag(content):
            self.status=201
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        else:
            tag=Tag()
            tag.content=content
            tag.tagid=uuid.uuid1().hex
            self.db.add(tag)
            self.db.commit()
            self.db.close()

            self.status=200
            self.message='tag添加成功'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)