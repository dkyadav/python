from django.urls import path

from . import views

urlpatterns =[
	#path('get_all_users/<pid>\d+/',views.get_all_users, name="get_all_users"),
	##url(r'^get_all_users/(?P<userid>\d+)/$', 'views.get_all_users', name='user_details'), 
	path('get_all_users/',views.get_all_users, name="get_all_users"),
	path('get_all_users/<slug:id>/',views.get_all_users, name="get_all_users"),

	path('get_all_courses/',views.get_all_courses, name="get_all_courses"),
	path('get_all_courses/search/<slug:name>/',views.get_all_courses, name="get_all_courses"),

	path('get_all_courses/<slug:id>/',views.get_all_courses_by_id, name="get_all_courses_by_id"),

	
]
