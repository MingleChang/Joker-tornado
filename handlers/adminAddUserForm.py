#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5
import uuid
from models.models import User
from handlers.base import BaseHandler

class AdminAddUserFormHandler(BaseHandler):
    def get(self):
        username=self.get_argument('username','')
        password=self.get_argument('password','')
        code=self.get_argument('code','')
        self.register(username,password,code)

    def post(self):
        username=self.get_argument('username','')
        password=self.get_argument('password','')
        code=self.get_argument('code','')
        self.register(username,password,code)

    def register(self,username,password,code):
        if username=='' or password=='' or code=='':
            self.render('admin/adduser.html',info='')
        elif code != 'mingle':
            self.render('admin/adduser.html',info='code error')
        elif self.checkUsername(username):
            self.render('admin/adduser.html',info='username error')
        elif self.checkPassword(password):
            self.render('admin/adduser.html',info='password error')
        elif self.checkUserExist(username):
            self.render('admin/adduser.html',info='username exist')
        else:
            userid=uuid.uuid1().hex
            m1 = md5.new()   
            m1.update(password)   
            newuser=User()
            newuser.userid=userid
            newuser.username=username
            newuser.password=m1.hexdigest()
            newuser.nickname=username
            self.db.add(newuser)
            self.db.commit()
            self.db.close()

            self.render('admin/adduser.html',info='success')


    def checkUsername(self,username):
        if username=='':
            return True
        elif len(username)<6 or len(username)>20:
            return True
        else:
            return False

    def checkPassword(self,password):
        if password=='':
            return True
        elif len(password)<6 or len(password)>20:
            return True
        else:
            return False

    def checkUserExist(self,username):
        count=self.db.query(User).filter(User.username==username).count()
        if count>0:
            return True
        else:
            return False

        