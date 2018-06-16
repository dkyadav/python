from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', database='test', password='deepak')
cursor = cnx.cursor()

query = ("SELECT * FROM one ")

cursor.execute(query)

for (name_vch) in cursor:
  print("{}was hired on ".format(
    name_vch))

cursor.close()
cnx.close()


# Create your views here.

def all_courses(request):
	# Render the HTML template index.html with the data in the context variable
    '''
    return render(
        request,
        'index.html',
        context={'test':'hello','test2':'hello world'},
    )
    '''
    all_candidates = []
    all_candidates.append({'name':'Deepak','course':'Python'})
    all_candidates.append({'name':'Ashish','course':'Java'})
    all_candidates.append({'name':'Pintu','course':'PHP'})

    return render(
    		request,
    		'courses/all_courses.html',
    		{'candidate':all_candidates}
    	)
	#return HttpResponse('This is a the sample page to list all courses.')