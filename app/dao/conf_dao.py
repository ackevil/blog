from app.dao.base_dao import BaseDao

class ConfDao(BaseDao):
    '''ConfDao'''
    def obtain(self,name):
        return self.single('select conf_vals from confs where conf_name = ?', (name, ))['conf_vals']
        
