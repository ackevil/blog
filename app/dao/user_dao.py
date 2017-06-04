from app.dao.base_dao import BaseDao

class UserDao(BaseDao):
    '''userDao'''
    def get_users_by_userids(self,userids):
        return self.result('select * from users where user_id in ('+','.join(userids)+')')

    def get_user_by_userid(self,userid):
        return self.result('select * from users where user_id = ? ',(userid,))