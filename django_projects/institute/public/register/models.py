from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class IUsers(models.Model):
	name = models.CharField(max_length=60)
	username = models.CharField(max_length=60)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=60)
	insert = models.DateTimeField(default=timezone.now)
	update = models.DateField(auto_now=True)
	
	def __str__(self):
		return(str(self.name))

