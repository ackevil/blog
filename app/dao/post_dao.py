from app.dao.base_dao import BaseDao

class PostDao(BaseDao):
    '''postDao'''
    def get_post_by_id(self, post_id):
        '''getpostbyid'''
        return self.single('select * from posts where post_id = ?', (post_id, ))
