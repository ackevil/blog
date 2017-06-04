from app.dao.base_dao import BaseDao

class PostDao(BaseDao):
    '''postDao'''
    def get_post_by_id(self, post_id):
        '''getpostbyid'''
        return self.single('select * from posts where post_id = ? ', (post_id, ))
    def get_pre_post_by_postid(self,stime,post_id):
         return self.single('select post_id from posts where post_stat >0 and post_ptms < ? and post_id  < ?  order by post_id desc limit 1', (stime,post_id, ))
    
    def get_next_post_by_postid(self,stime,post_id):
        return self.single('select post_id from posts where post_stat >0 and post_ptms < ? and post_id  > ?  order by post_id asc limit 1', (stime,post_id, ))

    def get_all_post(self,stime,pager):
        return self.result('select * from posts where post_stat > 0 and post_ptms < ? order by post_ptms desc limit ? offset ?', (stime, pager['qnty'], (pager['page']-1)*pager['qnty'], ))

    def get_all_tag_post(self,tag,stime,pager):
        return self.result("select posts.* from posts,post_terms where posts.post_id=post_terms.post_id and term_id=? and post_stat>0 and post_ptms<? order by post_ptms desc limit ? offset ?", (tag['term_id'], stime, pager['qnty'], (pager['page']-1)*pager['qnty'], ))

    def get_all_keyword_post(self,keyword,stime,pager):
        return self.result('select * from posts where post_stat > 0 and post_ptms < ? and (post_title like ? or post_content like ?) order by post_ptms desc limit ? offset ?',(stime,'%'+keyword+'%','%'+keyword+'%',pager['qnty'],(pager['page']-1)*pager['qnty'], ))
    
    def get_all_ptids_by_postid(self,postids):
        return self.result('select post_id,term_id from post_terms where post_id in ('+','.join(postids)+')')

    def get_ptids_by_postid(self,postid):
         return self.result('select post_id,term_id from post_terms where post_id = ? ',(postid,))

    def get_top_posts(self,stime,top_rank):
        return self.result('select post_id,post_title,post_descp from posts where post_stat>0 and post_ptms<? and post_rank>=? order by post_rank desc, post_id desc limit 9', (stime,top_rank,))

    def get_hot_posts(self,stime):
        return self.result('select post_id,post_title,post_descp from posts where post_stat>0 and post_ptms<? order by post_refc desc, post_id desc limit 9', (stime,))        

    def get_new_posts(self,stime):
        return self.result('select post_id,post_title,post_descp from posts where post_stat>0 and post_ptms<? order by post_ptms desc, post_id desc limit 9', (stime,))  

    