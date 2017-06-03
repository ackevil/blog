import os
import time

import tornado

class BasicControl(tornado.web.RequestHandler):
    def initialize(self):
        self._caches = {'model':{},'datum':{}}

    def set_default_headers(self):
        self.set_header('server',self.settings['servs'])
        self.set_header('x-frame-options','SAMEORIGIN')
        self.set_header('x-xss-protection','1;mode=block')
        self.set_header('cache_control','no-transform')
    
    def head(self,*args,**kwargs):
        return self.get(*args,**kwargs)

    def write_error(self,status_code,**kwargs):
        if not self.settings['error']:
            self.flash(0,{'sta':status_code})
            return
        return super(BasicControl,self).write_error(status_code,**kwargs)

    def flash(self,isok,resp=None,_ext = ''):
        if resp is None:
            resp={}
        
        if isok:
            resp["err"]=0
        else:
            resp["err"]=1

        if "sta" in resp and resp ["sta"]:
            self.set_status(resp["sta"])
        else:
            resp["sta"]=self.get_status()

        if "msg" not in resp:
            resp["msg"]=self._reason
        if "url" not in resp:
            resp["url"]=""
        if "dat" not in resp:
            resp["dat"]={}
        
        #if _ext == ".json" or self.find_accept("json"):
        #    self.write(tornado.escape.json_encode(resp))
        #else:
            self.render("flash.html",resp=resp)

    def get_current_user(self):
        usid=self.get_cookie("_usid")

    def get_runtime_conf(self,name):
        return None

    def asset(self, name, host = '/', base = 'www', path = 'assets', vers = True):
        pass;
        
    def jsons(self,json):
        pass;
    
    def stime(self):
        return int(time.time())

    def input(self, *args, **kwargs):
        return self.get_argument(*args,**kwargs)