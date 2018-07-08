from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from public.register.models import IUsers
import json
import sendgrid
import os
import ssl
from sendgrid.helpers.mail import *

# Create your views here.

ssl._create_default_https_context = ssl._create_unverified_context

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

def contactus_view(request):

	emailSent = {};
	emailSent['status'] = -1
	emailSent['retresult'] = 'not sent'

	if request.POST:
		f_name = request.POST.get('name')
		f_email = request.POST.get('email')
		f_message = request.POST.get('message')

		sg = sendgrid.SendGridAPIClient(apikey='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')
		from_email = Email("support@cricketlocal.com")
		to_email = Email("dkyadav.org@gmail.com")
		subject = "Request: Sendgrid contactUs Python Institute"
		
		#content = Content("text/plain", "Contact us message came from, Name: "+f_name+ " ,Enail: " +f_email+ " .Message: "+f_message);
		content = Content("text/html", "<i>Contact us message came from</i>, <b>Name:</b> "+f_name+ " ,Enail: " +f_email+ " .Message: "+f_message);

		#ssl._create_default_https_context = ssl._create_unverified_context

		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
		print(response.status_code)
		print(response.body)
		print(response.headers)
		
		from_email = Email("dkyadav.org@gmail.com")
		to_email = Email(f_email)
		subject = "Response: Sendgrid contactUs Python Institute"
		content = Content("text/plain", "We got your request and will revert back asap.");
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())

		emailSent['status'] = 1
		emailSent['retresult'] = 'success'

	return render(
    		request,
    		#'reg.html',
    		'contactus/contactus.html',
    		{'emailSent':emailSent}
    	)
 	


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

