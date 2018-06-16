from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def all_students(request):
	return HttpResponse('This is a the sample page to list all students.')