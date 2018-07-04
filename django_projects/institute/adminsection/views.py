from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from courses.models import Course
import json

import datetime
import mysql.connector


def course_list_admin(request):

    query_set = Course.objects.values().order_by('-id')

    return render(
            request,
            'addeditcourse.html',
            {'abc':query_set}
        )

def course_list_only_admin(request):

    query_set = Course.objects.values().order_by('-id')

    return render(
            request,
            'courselist.html',
            {'abc':query_set}
        )

def addedit_action(request):
	if request.POST:
		cid = request.POST.get('courseid')
		cn = request.POST.get('cname')
		cd = request.POST.get('cdesc')

		if cid == '0':
			newcourse = Course(name=cn, description=cd)
			print(newcourse)
			newcourse.save()
			newid = newcourse.id

			return HttpResponse(json.dumps({'cid': newid}), content_type="application/json")

		else:
			Course.objects.filter(id = cid).update(name = cn, description=cd)
			return HttpResponse(json.dumps({'cid': cid}), content_type="application/json")			

	else:
		return HttpResponse(json.dumps({'cid': -1}), content_type="application/json")			