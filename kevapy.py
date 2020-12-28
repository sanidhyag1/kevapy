import json
import os
from random import randint
import uuid



class kevapy:
    def __init__(self, path=None):
        if not path:
            path = os.getcwd()
        else:
            pass
        file_name = str(uuid.uuid4())[:8] + ".json"
        self.file_path = os.path.join(path,file_name)
        
        
        
    def create(self, js_object, key, ttl=None):
        f = open(self.file_path,"a")
        k = {}
        k[key] = js_object
        json.dump(k, f)
        f.close()

    def read(self, key):
        f = open(self.file_path,"r")
        k = json.load(f)
        print(k)
        print(type(k))
        

    def delete(self):
        pass


k = kevapy()
x =  '{"name":"John", "age":30, "city":"New York"}'
print(type(x))
k.create(x, "sanidhya")
k.read("sanidhya")