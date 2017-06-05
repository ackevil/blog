from app.dao.post_dao import PostDao
from app.dao.tag_dao import TagDao
from app.dao.term_dao import TermDao
from app.control.basic import BasicControl
from app.dao.user_dao import UserDao
from app.dao.talk_dao import TalkDao
from app.dao.link_dao import LinkDao
from app.tools.utils import Utils
class HomeControl(BasicControl):
    def get(self, _tnm = None):
        pager = {}
        pager['qnty'] = 5
        pager['page'] = max(int(self.input('page', 1)), 1)
        pager['lgth'] = 0


        stime=self.stime(); #当前时间
        track=''
        keyword = self.input("keyword",None)  #获取 是否是搜索操作
        _tag = None
        _top = False
        if _tnm:
            tag_dao=TagDao("terms")
            _tag=tag_dao.get_tag_by_tnm(_tnm)
        if _tag:
            post_dao=PostDao("posts")
            posts = post_dao.get_all_tag_post(_tag, stime, pager)
            tarck = '标签：'+_tag['term_name']
        elif _tnm:
            self.flash(0,{'sta':404})
            return
        elif keyword:
            post_dao=PostDao("posts")
            posts=post_dao.get_all_keyword_post(keyword,stime,pager)
            tarck = '搜索: '+keyword
        else:
            post_dao=PostDao("posts")
            posts = post_dao.get_all_post(stime, pager)
            if self.input('page',None) is None:
                _top=True
        ptids = {}
        ptags = {}
        psers = {}
        if posts :
            pager['lgth'] =len(posts)
            postids= list(str(i['post_id']) for i in posts)
            ptids = PostDao("posts").get_all_ptids_by_postid(postids)
            if ptids:
                termids=list(str(i['term_id']) for i in ptids)
                terms_list=TermDao("terms").get_terms_by_termids(termids)
                ptags=Utils.array_keyto(terms_list,'term_id')
            ptids=Utils.array_group(ptids,'post_id')
            userids= list(str(i['user_id']) for i in posts)
            users=UserDao("users").get_users_by_userids(userids)
            psers=Utils.array_keyto(users,'user_id')
        keyws_tag=TermDao("terms").get_terms()
        top_rank=self.get_runtime_conf('index_posts_top_rank')
        posts_top=PostDao("posts").get_top_posts(stime,top_rank)
        posts_hot=PostDao("posts").get_hot_posts(stime)
        posts_new=PostDao("posts").get_new_posts(stime)
        posts_rel=[]
        talk_rank=self.get_runtime_conf('posts_talks_min_rank')
        talks_new=TalkDao("talks").get_new_talks(talk_rank)

        if _top:
            link_rank=self.get_runtime_conf('index_links_min_rank')
            links_top=LinkDao("links").get_links(link_rank)
        else:
            links_top = None
        slabs_top=self.jsons(self.get_runtime_conf('slabs'))
        self.render('home.html', track = track, pager = pager, posts = posts, psers = psers, ptids = ptids, ptags = ptags
                , posts_top = posts_top, posts_hot = posts_hot, posts_new = posts_new, posts_rel = posts_rel
                , slabs_top = slabs_top, keyws_tag = keyws_tag, talks_new = talks_new, links_top = links_top)