from django.urls import path, include

from . import views

urlpatterns =[
	path('register/',views.register_view, name="register_view"),
	path('contactus/',views.contactus_view, name="contactus_view"),
	path('',views.home_view, name="home_view"),
	#path('register/',include('register.urls')),
	#path('register/',views.register_view, name="home_view"),
]
