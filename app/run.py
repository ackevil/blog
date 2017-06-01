# -*-coding: UTF-8 -*-
import sys
import os.path

import tornado.web
import tornado.ioloop
from tornado.options import define,options

from url import url # url 映射
from etc import etc # 网站配置

app = tornado.web.Application(handlers = url, **etc)

define("port",default=8000,help="run on the port",type=int)
def main():
    options.parse_command_line()
    print("Starting web server on http://127.0.0.1:%s" % options.port)
    print("Quit the server with CTRL+C")
    app.listen(options.port,xheaders=True)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__" :
    main()