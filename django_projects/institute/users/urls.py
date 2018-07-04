from django.urls import path

from . import views

urlpatterns =[
	path('populate/',views.populatedata, name="userspopulate"),
	path('login/',views.login, name="login"),
	path('logout/',views.logout_view, name="logout_view"),
	path('list/',views.list, name="list"),
	
]
