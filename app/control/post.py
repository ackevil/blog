from app.dao.post_dao import PostDao
from app.dao.tag_dao import TagDao
from app.dao.term_dao import TermDao
from app.control.basic import BasicControl
from app.dao.user_dao import UserDao
from app.dao.talk_dao import TalkDao
from app.dao.link_dao import LinkDao
from app.tools.utils import Utils
class PostControl(BasicControl):
    def get(self, post_id):    
        stime=self.stime(); #当前时间
       
        post=PostDao("posts").get_post_by_id(post_id)
        if not post or ((not self.get_current_user()) and (not post['post_stat'] or post['post_ptms']>=stime)):
            self.flash(0,{'sta':404})
        ptids = {}
        ptags = {}
        psers = {}
        ptids = PostDao("posts").get_ptids_by_postid(post_id)
        if ptids:
            termids=list(str(i['term_id']) for i in ptids)
            terms_list=TermDao("terms").get_terms_by_termids(termids)
            ptags=Utils.array_keyto(terms_list,'term_id')
        ptids=Utils.array_group(ptids,'post_id')
        userid= post['user_id']
        user=UserDao("users").get_user_by_userid(userid)
        psers=Utils.array_keyto(user,'user_id')
        
        post_prev=PostDao("posts").get_pre_post_by_postid(stime,post_id)
        if post_prev:
            post_prev=post_prev['post_id']
        else:
            post_prev = 0
        post_next = PostDao("posts").get_next_post_by_postid(stime,post_id)
        if post_next:
            post_next=post_next['post_id']
        else:
            post_next = 0
        
        keyws_tag=TermDao("terms").get_terms()
        top_rank=self.get_runtime_conf('index_posts_top_rank')
        posts_top=PostDao("posts").get_top_posts(stime,top_rank)
        posts_hot=PostDao("posts").get_hot_posts(stime)
        posts_new=PostDao("posts").get_new_posts(stime)

        posts_rel=None
        talks = None
        talks_new=None
        links_top=None
        slabs_top=None
      
        self.render('detail_post.html', post = post, psers = psers, ptids = ptids, ptags = ptags, talks = talks
                , post_prev = post_prev, post_next = post_next
                , posts_top = posts_top, posts_hot = posts_hot, posts_new = posts_new, posts_rel = posts_rel
                , slabs_top = slabs_top, keyws_tag = keyws_tag, talks_new = talks_new, links_top = links_top)