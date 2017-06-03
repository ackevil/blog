import tornado
from app.dao.bas_dao import BaseDao
from app.control.basic import BasicControl
class HomeControl(BasicControl):
    def get(self):
        dao=BaseDao("posts")
        print(dao.result('select * from posts'))
        self.render("posts.html")