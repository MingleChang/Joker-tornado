#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from handlers.base import BaseHandler

class APIHandler(BaseHandler):
	status=404
	message=''
	def get(self):
		self.write(self.getJsonResult())

	def post(self):
		self.write(self.getJsonResult())

	def getJsonResult(self,result=None,**kwargs):
		dic={'status':self.status,'message':self.message,'result':result}
		dic.update(kwargs)
		return json.dumps(dic)

	#如果是api，禁用xsrf
	def check_xsrf_cookie(self):
		pass
