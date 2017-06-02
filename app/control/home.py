import tornado
from app.control.basic import BasicControl
class HomeControl(BasicControl):
    def get(self):
        self.render("posts.html")