import urllib.request as ur
import json
import pprint
from pprint import PrettyPrinter as pp

request = ur.urlopen('http://jsonplaceholder.typicode.com/posts')
#response = request.read().decode('utf-8')
response = request.read()
print(type(response))
convert_py = json.loads(response)
print(type(convert_py))
#print(convert_py)
'''
pobj = pprint.PrettyPrinter()
pobj.pprint(convert_py)
'''
#pprint.PrettyPrinter().pprint(convert_py)

#use this one its working for pp
pp().pprint(convert_py)



for jo in convert_py:
	if jo['userId'] == 3:
		print("Post Id {0} ,UserId: {1}, Title: {2}".format(jo['id'],jo['userId'],jo['title']))


