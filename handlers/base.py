#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime,date,time
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie("username")
	@property
	def db(self):
		return self.application.db

	def get(self):
		self.write('404')

	def post(self):
		self.write('404')

	def getAttrModel(self,model,attr):
		data=getattr(model, attr)
		if isinstance(data,datetime):
			data=data.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(data,date):
			data=data.strftime('%Y-%m-%d')
		elif isinstance(data,time):
			data=data.strftime('%H:%M:%S')
		return data