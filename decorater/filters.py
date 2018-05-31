emails = ['deepak', 'yadav', 'kumar','deepanshu']
emailscheck = ('deepak', 'yadav', 'kumar')

list_fil = [];
list_fil = filter(lambda n: 'ee' in n, emails)
#returns an object and makes list_fil as object, ..
#..so we have convert it into list before printing it 
print(type(emails))
print(type(emailscheck))


print(list(list_fil))