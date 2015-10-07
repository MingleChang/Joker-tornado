#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import json
# from sqlalchemy.orm import class_mapper
from models.models import Comment,Joke,User
from handlers.api import APIHandler

class APICommentSelectHandler(APIHandler):
    def get(self):
        jokeid=self.get_argument('jokeid','')
        self.selectComment(jokeid)
        
    def post(self):
        jokeid=self.get_argument('jokeid','')
        self.selectComment(jokeid)

    def checkJoke(self,jokeid):
        count=self.db.query(Joke).filter(Joke.jokeid==jokeid).count()
        if count>0:
            return True
        else:
            return False

    def selectComment(self,jokeid):
        if jokeid=='':
            self.status=201
            self.message='jokeid不能为空'
            jsonStr=self.getJsonResult()

            self.write(jsonStr)
        elif not self.checkJoke(jokeid):
            self.status=201
            self.message='该jokeid不存在'
            jsonStr=self.getJsonResult()

            self.write(jsonStr)
        else:
            comments=self.db.query(Comment.commentid,Comment.content,User.username).filter(Comment.jokeid==jokeid).filter(Comment.userid==User.userid).all()
            arr=[]
            for comment in comments:
                dic={}
                dic['commentid']=comment[0]
                dic['content']=comment[1]
                dic['username']=comment[2]
                arr.append(dic)
            self.status=200
            jsonStr=self.getJsonResult(result=arr,count=len(arr))

            self.write(jsonStr)

    
        