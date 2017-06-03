class Utils(object):
    @staticmethod
    def array_keyto(ary,key):
        ret={}
        for val in ary:
            ret[val[key]] = val
        return ret

    @staticmethod
    def array_group(ary,key):
        ret={}
        for val in ary:
            if val[key] not in ret:
                ret[val[key]]=[]
            ret[val[key]].append(val)
        return ret