import pickle
import datetime

def write(path, js_object, key, ttl=None):
    f = open(path,"rb")
    data = pickle.load(f)
    f.close()
    # adding time to live to current_time to get and expiry_time
    if ttl != None :
        ttl = datetime.datetime.now() + datetime.timedelta(seconds=ttl)
    data[key] = {"obj": js_object, "ttl":ttl}
    #print(data)
    f = open(path, "wb")
    pickle.dump(data, f)
    f.close()

def load(path):
    f = open(path, "rb")
    data = pickle.load(f)
    f.close()
    return data


def ttl_check(ttl):
    if ttl == None:
        return True
    elif ttl == -1:
        return "False"
    return datetime.datetime.now() <= ttl