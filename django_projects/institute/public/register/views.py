from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from public.register.models import IUsers
import json

# Create your views here.

def register_view(request):

	if request.POST:
		name = request.POST.get('name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		iu = IUsers(name=name, username=username, email=email, password=password)
		iu.save()
		newid = iu.id

		return HttpResponse(json.dumps({'uid': newid}), content_type="application/json")
	
	return render(
    		request,
    		#'reg.html',
    		'reg.html',
    		{'candidate':'all_candidates'}
    	)
