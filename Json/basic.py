#reading only a particular field from a json file
import json
import re
from pprint import pprint
a=[]
data = json.load(open('/home/vishal/Documents/userdocId.json'))
print(type(data))
j=0;
aa=""
final=[]
print(type(aa))
for i in data:
    a.append(i)
    aa=a[j]["id"]
    final.append((re.split('[-:]', aa)[1]))
    j+=1
print(final)




#dataset
# [
#   {
#     "id": "user:10"
#   }]