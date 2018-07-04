from django.urls import path

from . import views

urlpatterns =[
	path('',views.all_courses, name="all_courses"),
	path('list/',views.all_courses_list, name="all_courses"),
]
