#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5
from sqlalchemy.orm import class_mapper
from models.models import User
from handlers.api import APIHandler

class APILoginHandler(APIHandler):
    def get(self):
        username=self.get_argument('username','')
        password=self.get_argument('password','')
        self.login(username,password)
        
    def post(self):
        username=self.get_argument('username','')
        password=self.get_argument('password','')
        self.login(username,password)
        
    def login(self,username,password):
        m1 = md5.new()   
        m1.update(password)   
        users=self.db.query(User).filter(User.username==username).filter(User.password==m1.hexdigest())
        if users.count()>0:
            user=users[0]
            columns = [c.key for c in class_mapper(user.__class__).columns]
            dic = dict((c, self.getAttrModel(user, c)) for c in columns)
            dic.pop('password')
            dic.pop('create')
            dic.pop('update')
            self.status=200
            jsonStr=self.getJsonResult(result=dic)
            self.write(jsonStr)
        else:
            self.status=201
            self.message='帐号或密码错误'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)