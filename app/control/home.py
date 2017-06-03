from app.dao.base_dao import BaseDao
from app.control.basic import BasicControl
class HomeControl(BasicControl):
    def get(self):
        pager = {}
        pager['qnty'] = 5
        pager['page'] = max(int(self.input('page', 1)), 1)
        pager['lgth'] = 0

        stime=self.stime(); #当前时间
        dao=BaseDao("posts")
        posts=dao.result('select * from posts where post_stat > 0 and post_ptms < ? order by post_ptms desc limit ? offset ?', (stime, pager['qnty'], (pager['page']-1)*pager['qnty'], ))
        self.render("home.html", posts= posts,pager=pager)