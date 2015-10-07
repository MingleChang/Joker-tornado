#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from handlers.api import APIHandler

from handlers.apiRegister import APIRegisterHandler
from handlers.apiLogin import APILoginHandler

from handlers.apiTagInsert import APITagInsertHandler
from handlers.apiTagSelect import APITagSelectHandler

from handlers.apiJokeInsert import APIJokeInsertHandler
from handlers.apiJokeSelect import APIJokeSelectHandler

from handlers.apiCommentInsert import APICommentInsertHandler
from handlers.apiCommentSelect import APICommentSelectHandler

from handlers.adminAddTagForm import AdminAddTagFormHandler
from handlers.adminAddUserForm import AdminAddUserFormHandler
from handlers.adminAddJokeForm import AdminAddJokeFormHandler

url_patterns = [
    (r'/api/register',APIRegisterHandler),
    (r'/api/login',APILoginHandler),
    
    (r'/api/addtag',APITagInsertHandler),
    (r'/api/gettag',APITagSelectHandler),
    
    (r'/api/addjoke',APIJokeInsertHandler),
    (r'/api/getjoke',APIJokeSelectHandler),
    
    (r'/api/addcomment',APICommentInsertHandler),
    (r'/api/getcomment',APICommentSelectHandler),
    
    (r'/admin/addtag',AdminAddTagFormHandler),
    (r'/admin/adduser',AdminAddUserFormHandler),
    (r'/admin/addjoke',AdminAddJokeFormHandler),
       
    (r'/api/.*', APIHandler),
    (r'.*',BaseHandler),
]