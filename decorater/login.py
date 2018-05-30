from excel import OpenExcel
from pprint import pprint


excel_obj = OpenExcel('credentials.xlsx')
dic_obj = OpenExcel('checkfrom.xlsx')

print(excel_obj)
pprint(excel_obj)
#print vars(excel_obj)

creds = {}

for row in range(1,5):
	user_row = 'A{}'.format(row)
	username = dic_obj.read(user_row)
	user_row = 'B{}'.format(row)
	password = dic_obj.read(user_row)
	creds[username] = password
	#print ("username:"+username + " || " + "password:"+password)

#creds = {'users1':'p123','u2':'p2'}
print(creds)
pprint(creds)
#print vars(creds)

def check_login(func):
	def anyname(u,p):
		if(u in creds and creds[u] == p):
			return func(u,p)
		else:
			return('login failed')
	return anyname

@check_login
def login(u,p):
	return("Login success")

print(login('u2','p2'))

for row in range(1,5):
	user_row = 'A{}'.format(row)
	username = excel_obj.read(user_row)
	user_row = 'B{}'.format(row)
	password = excel_obj.read(user_row)
	#print ("username:"+username + " || " + "password:"+password)
	print(login(username,password))
