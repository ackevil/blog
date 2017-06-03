from app.dao.base_dao import BaseDao

class TagDao(BaseDao):
    '''tagDao'''
    def get_tag_by_tnm(self,tnm):
        self.single("select * from terms where term_name = ? limit 1", (str(tnm),))
