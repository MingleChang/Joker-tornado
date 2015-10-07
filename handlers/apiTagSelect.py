#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.orm import class_mapper
from models.models import Tag
from handlers.api import APIHandler

class APITagSelectHandler(APIHandler):
    def get(self):
        self.selectTag()
        
    def post(self):
        self.selectTag()

    def selectTag(self):
        tags=self.db.query(Tag)
        tagArr=[]
        for tag in tags:
            columns = [c.key for c in class_mapper(tag.__class__).columns]
            dic = dict((c, self.getAttrModel(tag, c)) for c in columns)
            tagArr.append(dic)
        self.status=200
        jsonStr=self.getJsonResult(result=tagArr,count=tags.count())
        self.write(jsonStr)