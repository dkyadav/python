from django.urls import path

from . import views

urlpatterns =[
	path('courses/',views.course_list_admin, name="course_list_admin"),
	path('courseslist/',views.course_list_only_admin, name="course_list_only_admin"),
	path('addedit_action/',views.addedit_action, name="addedit_action"),
	#path('list/',views.all_courses_list, name="all_courses"),
]
