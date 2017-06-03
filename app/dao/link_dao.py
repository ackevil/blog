from app.dao.base_dao import BaseDao

class LinkDao(BaseDao):
    '''LinkDao'''
    def get_links(self,link_rank):
        return self.result('select * from links where link_rank>=? order by link_rank desc, link_id desc limit 99', (link_rank, ))
        
