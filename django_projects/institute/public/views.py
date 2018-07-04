from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def home_view(request):
	# return render(
 #    		request,
 #    		'reg.html',
 #    		{}
 #    	)

 	return render(
    		request,
    		#'reg.html',
    		'home.html',
    		{'candidate':'all_candidates'}
    	)

