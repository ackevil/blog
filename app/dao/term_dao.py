from app.dao.base_dao import BaseDao

class TermDao(BaseDao):
    '''termDao'''
    def get_terms_by_termids(self,termids):
        return self.result('select * from terms where term_id in ('+','.join(termids)+')')

    def get_terms(self):
        return self.result('select * from terms where term_refc>0 order by term_refc desc, term_id desc limit 32')