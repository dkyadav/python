from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=60)
	description = models.CharField(max_length=100)
	insert = models.DateTimeField(default=timezone.now)
	update = models.DateField(auto_now=True)

	def __str__(self):
		return(str(self.name))