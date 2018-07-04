from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

#import json
from public.register.models import IUsers
from courses.models import Course

from django.db.models import Q


def get_all_users(request, id=0):
	print(id)

	if 'id' in request.GET:
		id = int(request.GET['id'])
		users = IUsers.objects.filter(id__gt=id)
	elif int(id) > 0:
		users = IUsers.objects.filter(id__gt=id)
	else:
		users = IUsers.objects.all()

	pObj_dObj = {}

	for us in users:
		id = us.id
		pObj_dObj[id] = {}
		pObj_dObj[id]['name'] = us.name;
		pObj_dObj[id]['username'] = us.username;
		pObj_dObj[id]['email'] = us.email;

	return JsonResponse(pObj_dObj)


def get_all_courses_by_id(request, id=''):
	
	pObj_dObj = {}
	coursesq = {}
	pObj_dObj['result'] = -1;

	if id != '':
		coursesq = Course.objects.filter(id=int(id))
	
	for crs in coursesq:
		pObj_dObj['result'] = 1;
		pObj_dObj['name'] = crs.name;
		pObj_dObj['description'] = crs.description;
		

	return JsonResponse(pObj_dObj)


def get_all_courses(request, name=''):
	print(name)

	if 'name' in request.GET:
		name = int(request.GET['id'])
		coursesq = Course.objects.filter(Q(name__icontains=name) | Q(description__icontains=name))
	elif name != '':
		coursesq = Course.objects.filter(Q(name__icontains=name) | Q(description__icontains=name))
		print(coursesq)
	else:
		coursesq = Course.objects.all()

	pObj_dObj = {}

	for crs in coursesq:
		id = crs.id
		pObj_dObj[id] = {}
		pObj_dObj[id]['name'] = crs.name;
		pObj_dObj[id]['description'] = crs.description;
		

	return JsonResponse(pObj_dObj)
