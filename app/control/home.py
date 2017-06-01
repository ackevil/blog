import tornado

class HomeControl(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Baby\n")