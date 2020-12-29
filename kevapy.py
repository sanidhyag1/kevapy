import os, uuid, pickle
from pack.helper import write, load, ttl_check
import sys

class Kevapy:

    def __init__(self, path=None):
        if not path:
            path = os.getcwd()
        file_name = str(uuid.uuid4())[:8] + '.dat'
        self.file_path = os.path.join(path, file_name)
        f = open(self.file_path, 'wb')
        k = {}
        pickle.dump(k, f)
        f.close()

    def create(self, js_object, key, ttl=None):
        if 16000 < sys.getsizeof(js_object):
            print('Error: Size of json object exceeds 16kb')
            return -1
        if len(key) > 32:
            print('Error: Length of key exceeds 32 characters')
            return -1
        try:
            write(self.file_path, js_object, key, ttl)
        except:
            raise Exception('Error: cannot write to this file please try again')
        else:
            print('Done!')

    def read(self, key):
        try:
            data = load(self.file_path)
        except:
            raise Exception('Error: cannot load datastore')
        else:
            try:
                if ttl_check(data[key]['ttl']):
                    return data[key]['obj']
                else:
                    return 'Ttl expired'
            except:
                raise Exception('Error: No such key in datastore')

    def delete(self, key):
        data = load(self.file_path)
        if ttl_check(data[key]['ttl']):
            del data[key]
        else:
            return 'Time to live has expired'
        f = open(self.file_path, 'wb')
        pickle.dump(data, f)
        print('Deleted!')

