#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from sqlalchemy.orm import class_mapper
from models.models import Tag,User,Joke
from handlers.base import BaseHandler

class AdminAddJokeFormHandler(BaseHandler):
    def get(self):
        userid=self.get_argument('userid','')
        title=self.get_argument('title','')
        content=self.get_argument('content','')
        tagid=self.get_argument('tagid','')
        code=self.get_argument('code','')
        
        self.addJoke(userid, tagid, title, content, code)

    def post(self):
        userid=self.get_argument('userid','')
        title=self.get_argument('title','')
        content=self.get_argument('content','')
        tagid=self.get_argument('tagid','')
        code=self.get_argument('code','')
        
        self.addJoke(userid, tagid, title, content, code)
    
    
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
    
    def addJoke(self,userid,tagid,title,content,code):
        tagArr=self.selectAllTag()
        userArr=self.selectAllUser()
        if userid=='' or tagid=='' or content=='' or code=='':
            self.render('admin/addjoke.html',info='',tags=tagArr,users=userArr)
        elif code != 'mingle':
            self.render('admin/addjoke.html',info='Code error',tags=tagArr,users=userArr)
        elif not self.checkUser(userid):
            self.render('admin/addjoke.html',info='Userid error',tags=tagArr,users=userArr)
        elif not self.checkTag(tagid):
            self.render('admin/addjoke.html',info='Tagid error',tags=tagArr,users=userArr)
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
            
            self.render('admin/addjoke.html',info='Success',tags=tagArr,users=userArr)
            
    
    def  selectAllUser(self):
        users=self.db.query(User.userid,User.username)
        userArr=[]
        for user in users:
            dic={}
            dic['userid']=user.userid
            dic['username']=user.username
            userArr.append(dic)
        return userArr

    def selectAllTag(self):
        tags=self.db.query(Tag)
        tagArr=[]
        for tag in tags:
            columns = [c.key for c in class_mapper(tag.__class__).columns]
            dic = dict((c, self.getAttrModel(tag, c)) for c in columns)
            tagArr.append(dic)
        return tagArr
        