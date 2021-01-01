# Importing library
from kevapy_lib.kevapy import Kevapy
# Once imported create an instance of the class

k = Kevapy() #Initializes the datastore in the same directory
# k = Kevapy("/home/xyz/") # Optional path for the datastore can be provided

x =  '{ "name":"John", "age":30, "city":"New York"}' #sample Json object
# Json objects can be stored in the database upto a size of 16kb

#k.create(json_object_here, key_here, optional-ttl)

#key should be <= 32 characters
#optional integer ttl(time-to-live) can be specified

k.create(x, "xyzabc",50) #50 seconds from now this will expire
print(k.read("xyzabc")) #return a json object
k.delete("xyzabc")
