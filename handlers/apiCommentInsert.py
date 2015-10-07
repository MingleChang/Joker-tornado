#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
# import json
# from sqlalchemy.orm import class_mapper
from models.models import Comment,Joke,User
from handlers.api import APIHandler

class APICommentInsertHandler(APIHandler):
    def get(self):
        jokeid=self.get_argument('jokeid','')
        userid=self.get_argument('userid','')
        content=self.get_argument('content','')
        self.insertComment(jokeid,userid,content)
        
    def post(self):
        jokeid=self.get_argument('jokeid','')
        userid=self.get_argument('userid','')
        content=self.get_argument('content','')
        self.insertComment(jokeid,userid,content)

    def checkJoke(self,jokeid):
        count=self.db.query(Joke).filter(Joke.jokeid==jokeid).count()
        if count>0:
            return True
        else:
            return False

    def checkUser(self,userid):
        count=self.db.query(User).filter(User.userid==userid).count()
        if count>0:
            return True
        else:
            return False

    def insertComment(self,jokeid,userid,content):
        if jokeid=='':
            self.status=201
            self.message='jokeid不能为空'
            jsonStr=self.getJsonResult()

            self.write(jsonStr)
        elif userid=='':
            self.status=201
            self.message='userid不能为空'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        elif content=='':
            self.status=201
            self.message='content不能为空'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        elif not self.checkUser(userid):
            self.status=201
            self.message='该userid不存在'
            jsonStr=self.getJsonResult()

            self.write(jsonStr)
        elif not self.checkJoke(jokeid):
            self.status=201
            self.message='该jokeid不存在'
            jsonStr=self.getJsonResult()

            self.write(jsonStr)
        else:
            commentid=uuid.uuid1().hex;
            newcomment=Comment()
            newcomment.commentid=commentid
            newcomment.userid=userid
            newcomment.jokeid=jokeid
            newcomment.content=content

            self.db.add(newcomment)
            self.db.commit()
            self.db.close()
            
            self.status=200
            jsonStr=self.getJsonResult()

            self.write(jsonStr)
        
