from app.dao.base_dao import BaseDao

class TalkDao(BaseDao):
    '''talkDao'''
    def get_new_talks(self,talk_rank):
        return self.result('select * from talks where talk_rank>=? order by talk_id desc limit 9', (talk_rank, ))