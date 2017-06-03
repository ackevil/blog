import sqlite3
import sys
import os
from collections import OrderedDict
class BaseDao(object):
    ''' base dao  db'''
    def __init__(self, name):
        self.con = sqlite3.connect(os.path.join(sys.path[0], "var", "datas", name + ".sdb"))
        self.con.row_factory = self.__class__.sqlite_dict
        self.con.text_factory = str

    @staticmethod
    def sqlite_dict(cur, row):
        ''' sqlite_dict'''
        return OrderedDict((v[0], row[i]) for i, v in enumerate(cur.description))

    @staticmethod
    def sqlite_rows(cur):
        '''sqlite_rows'''
        return [OrderedDict((v[0], row[i if i in row else v[0]]) \
                for i, v in enumerate(cur.description)) \
                for row in cur.fetchall()]

    def result(self, *args, **kwargs):
        ''' result'''
        cur = self.con.cursor()
        cur.execute(*args, **kwargs)
        ret = cur.fetchall()
        cur.close()
        return ret

    def cursor(self, *args, **kwargs):
        ''' cursor'''
        return self.con.cursor(*args, **kwargs)

    def revert(self, *args, **kwargs):
        '''revert'''
        return self.con.rollback(*args, **kwargs)

    def single(self, *args, **kwargs):
        '''single'''
        cur = self.con.cursor()
        cur.execute(*args, **kwargs)
        ret = cur.fetchone()
        cur.close()
        return ret

    def invoke(self, *args, **kwargs):
        '''invoke'''
        cur = self.con.execute(*args, **kwargs)
        self.con.commit()
        return cur
