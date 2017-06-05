from app.dao.base_dao import BaseDao

class TalkDao(BaseDao):
    '''talkDao'''
    def get_new_talks(self,talk_rank):
        return self.result('select * from talks where talk_rank>=? order by talk_id desc limit 9', (talk_rank, ))
    
    def add_talk(self,post_id,remote_ip,user_id,name,mail,text,rank,time):
        return self.invoke('insert into talks (post_id,user_ip,user_id,user_name,user_mail,talk_text,talk_rank,talk_ctms,talk_utms) values (?,?,?,?,?,?,?,?,?)',(post_id,remote_ip,user_id,name,mail,text,rank,time,time,))
    