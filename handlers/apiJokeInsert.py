#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
# from sqlalchemy.orm import class_mapper
from models.models import Joke,Tag,User
from handlers.api import APIHandler

class APIJokeInsertHandler(APIHandler):
    def get(self):
        userid=self.get_argument('userid','')
        title=self.get_argument('title','')
        content=self.get_argument('content','')
        tagid=self.get_argument('tagid','')
        self.addJoke(userid,title,content,tagid)
        
    def post(self):
        userid=self.get_argument('userid','')
        title=self.get_argument('title','')
        content=self.get_argument('content','')
        tagid=self.get_argument('tagid','')
        self.addJoke(userid,title,content,tagid)

    def checkTag(self,tagid):
        count=self.db.query(Tag).filter(Tag.tagid==tagid).count()
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

    def addJoke(self,userid,title,content,tagid):
        if userid=='':
            self.status=201
            self.message='userid不能为空'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        elif tagid=='':
            self.status=201
            self.message='tagid不能为空'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        elif not self.checkUser(userid):
            self.status=201
            self.message='该userid不存在'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        elif not self.checkTag(tagid):
            self.status=201
            self.message='该tagid不存在'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        elif content=='':
            self.status=201
            self.message='content不能为空'
            jsonStr=self.getJsonResult()
            self.write(jsonStr)
        else:
            jokeid=uuid.uuid1().hex
            newjoke=Joke()
            newjoke.jokeid=jokeid
            newjoke.userid=userid
            newjoke.title=title
            newjoke.tagid=tagid
            newjoke.content=content
            
            self.db.add(newjoke)
            self.db.commit()
            self.db.close()

            jokes=self.db.query(Joke.jokeid,Joke.title,Joke.content,User.username,Tag.content).filter(Joke.jokeid==jokeid).filter(Joke.userid==User.userid).filter(Joke.tagid==Tag.tagid).all()
            joke=jokes[0]

            dic={};
            dic['jokeid']=joke[0]
            dic['title']=joke[1]
            dic['content']=joke[2]
            dic['username']=joke[3]
            dic['tagcontent']=joke[4]

            self.status=200
            jsonStr=self.getJsonResult(result=jokes)

            self.write(jsonStr)
        