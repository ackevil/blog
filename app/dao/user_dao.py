from app.dao.base_dao import BaseDao

class UserDao(BaseDao):
    '''userDao'''
    def get_users_by_userids(self,userids):
        return self.result('select * from users where user_id in ('+','.join(userids)+')')