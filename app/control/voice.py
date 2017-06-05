from app.control.basic import BasicControl

from app.dao.post_dao import PostDao
from app.dao.talk_dao import TalkDao
class VoiceControl(BasicControl):
    def post(self,post_id):
        post=PostDao("posts").get_post_by_id(post_id)
        if not post :
            self.flash(0,{'msg':'文章不存在'})
            return
        user_id='0'
        rank='0'
        name=self.input('name')
        mail=self.input('mail')
        text=self.input('text')
        time = self.stime()
       
        try:
            tkid=TalkDao("talks").add_talk(post_id,self.request.remote_ip,user_id,name,mail,text,rank,time)
            print("odddk")
            PostDao("posts").update_refc(post_id)
            if float(rank) > 0:
                self.flash(1,{'msg':'评论成功','dat':{'did':tkid}})
            else:
                self.flash(1,{'msg':'评论成功,等待管理员审核'})
            
        except:
            TalkDao("talks").revert()
            PostDao("posts").revert()
            self.flash(0)