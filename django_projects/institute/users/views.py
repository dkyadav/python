from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import Template, Context, RequestContext
import json
from public.register.models import IUsers
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from users.models import Users

from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def populatedata(request):
	#Users.objects.create(username='depak',is_password=True, uid=10, gid =20, fullname='deepak yadav', home='/etc/passwd', shell='/bin/bash')

	filename = "/etc/passwd"
	file = open(filename, "r")
	for line in file:
		mylist = line.split(":")
		
		#if(len(mylist) ==7 ):
		if not line.startswith('#'):
			ispwd = False
			if(mylist[1] == '*'):
				ispwd = True
			Users.objects.create(username=mylist[0],is_password=ispwd, uid=mylist[2], gid =mylist[3], fullname=mylist[4], home=mylist[5], shell=mylist[6])
			#print(mylist[1])
		#if(len(mylist) == 7)
			#print(mylist[1])

	return HttpResponse('Inserted in users')

def logout_view(request):
	print(request.session['id'])
	del request.session['id']
	del request.session['name']
	del request.session['email']
	logout(request)
	return HttpResponseRedirect("/")

def login(request):
	if request.POST:
		un = request.POST.get('username')
		pwd = request.POST.get('password')
		
		row_count = IUsers.objects.filter(username=un,password=pwd).count()

		if row_count == 0:
			retuid = 0
			request.session['id'] = 0
			request.session['name'] = ''
			request.session['email'] = ''
		else:
			userobj = IUsers.objects.get(username=un,password=pwd)
			retuid = userobj.id
			request.session['id'] = retuid
			request.session['name'] = userobj.name
			request.session['email'] = userobj.email


		return HttpResponse(json.dumps({'uid': retuid}), content_type="application/json")
		#return render_to_response('users/test.html', locals())
		#return "hello"

	return render(request,'users/loginform.html',{})


def list(request):
	row_count = IUsers.objects.count()
	if row_count > 0:
		query_set = IUsers.objects.values().order_by('-id')
		print(query_set)
		print("queryert finibnsh")
		retitems = []
		i = 0
		for item in query_set:
			#retitems[0] = {}
			#retitems[0].id = item['id']
			#retitems[i].name = item.name
			#retitems[i].username = item.username
			print(item['id'])
			
			

		#data = json.dumps(query_set)
		print(retitems)
		#jr = JsonResponse({'abc': list(query_set)})
		#print(jr)
		return render(request,'users/list.html',{'abc':query_set})
		#return render(request,'users/list.html',{'abc':json.dumps(retitems)})
		
	return render(request,'users/list.html',{})

