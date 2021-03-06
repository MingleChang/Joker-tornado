#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import json
# from sqlalchemy.orm import class_mapper
from models.models import Joke,User,Tag
from handlers.api import APIHandler

class APIJokeSelectHandler(APIHandler):
    def get(self):
        start=self.get_argument('start',0)
        count=self.get_argument('count',10)
        self.select(start,count)

    def post(self):
        start=self.get_argument('start',0)
        count=self.get_argument('count',10)
        self.select(start,count)

    def select(self,start,count):
        jokes=self.db.query(Joke.jokeid,Joke.title,Joke.content,User.username,Tag.content)
        jokes=jokes.filter(Joke.userid==User.userid)
        jokes=jokes.filter(Joke.tagid==Tag.tagid)
        jokes=jokes.offset(start)
        jokes=jokes.limit(count)
        arr=[]
        for joke in jokes:
            dic={};
            dic['jokeid']=joke[0]
            dic['title']=joke[1]
            dic['content']=joke[2]
            dic['username']=joke[3]
            dic['tagcontent']=joke[4]
            arr.append(dic)
        self.status=200
        jsonStr=self.getJsonResult(result=arr,count=len(arr))

        self.write(jsonStr)
    